#!/usr/bin/env python3
"""Controllo automatico dei dialoghi del master.

Il master incolla la bozza del messaggio e lo script segnala gli errori
vietati da regole/06-dialoghi.md e regole/07-dialoghi-shonen.md:
- battute a telegramma (frasi corte e piatte chiuse dal punto, una dopo l'altra);
- risposte a eco ("X, sì", "Sì, ..." in apertura di battuta);
- glosse del narratore e narratore-grilletto;
- "mezzo segreto" interrotto;
- assoluti in bocca ai PNG;
- parole ripetute tra battute diverse (possibili concetti ripetuti).

Uso:
  python3 strumenti/controlla_dialoghi.py bozza.txt
  python3 strumenti/controlla_dialoghi.py <<'EOF'
  ...testo...
  EOF

Esce con codice 1 se trova ERRORI. Gli AVVISI vanno valutati a mano.
"""

import re
import sys
from collections import Counter

FINE_FRASE = re.compile(r"(?<=[.!?])\s+")
PAROLA = re.compile(r"[A-Za-zÀ-ÿ']+")

GLOSSE = [
    "glielo si leggeva in faccia", "non per sbaglio", "non era una domanda",
    "si capiva che", "non c'entrava niente", "come se niente fosse",
    "fu proprio da lì", "se n'era già andat", "si leggeva negli occhi",
    "era chiaro che", "voleva dire che",
]
GRILLETTI = [r"\bAlla parola\b", r"\bAl complimento\b", r"\bAll'ultima frase\b", r"\bSull'ultima frase\b"]
MEZZO_SEGRETO = ["lascia perdere", "fai finta che non", "non ho detto niente", "dimentica quello che"]
ASSOLUTI = ["sempre", "mai", "tutti", "nessuno", "ogni volta"]
STOP = set("""
alla allo alle agli dalla dalle dallo della delle dello degli nella nelle nello negli sulla sulle sullo sugli
mentre perché perche quando quello quella quelli quelle questo questa questi queste anche ancora adesso allora
proprio sempre qualcosa niente nulla molto troppo tanto poco dopo prima dentro fuori sopra sotto
essere stato stata sono sei siamo siete hanno avere aveva avevo fatto fare dire detto come cosa cose
""".split())


def battute(testo):
    """Restituisce (numero_riga, battuta) per ogni testo tra « e »."""
    out = []
    for m in re.finditer(r"«([^»]*)»", testo):
        riga = testo.count("\n", 0, m.start()) + 1
        out.append((riga, m.group(1).strip()))
    return out


def narrazione(testo):
    return re.sub(r"«[^»]*»", " ", testo)


def frasi(s):
    return [f.strip() for f in FINE_FRASE.split(s) if f.strip()]


def controlla(testo):
    errori, avvisi = [], []
    bb = battute(testo)

    # 1. Telegrammi: frasi corte e piatte (<= 5 parole, chiuse dal punto) dentro la stessa battuta.
    for riga, b in bb:
        ff = frasi(b)
        piatta = lambda f: f.endswith(".") and not f.endswith("…")
        n_parole = lambda f: len(PAROLA.findall(f))
        corte = [f for f in ff if n_parole(f) <= 5]
        piatte = [f for f in corte if piatta(f)]
        punti = sum(1 for f in ff if piatta(f))
        coppie = [(a, c) for a, c in zip(ff, ff[1:]) if piatta(a) and piatta(c) and n_parole(a) <= 8 and n_parole(c) <= 8]
        if len(corte) >= 2 and piatte:
            errori.append(f"riga {riga}: TELEGRAMMA, {len(corte)} frasi corte nella stessa battuta (di cui {len(piatte)} piatte) → legale con virgole/congiunzioni: «{b[:90]}»")
        elif coppie:
            errori.append(f"riga {riga}: FRASI STACCATE, due frasi brevi di fila chiuse dal punto → uniscile in un solo periodo: «{coppie[0][0]} {coppie[0][1]}»")
        elif piatte and len(ff) >= 3:
            avvisi.append(f"riga {riga}: frase corta e piatta dentro una battuta lunga, valuta se fonderla: «{piatte[0]}»")
        if punti >= 4:
            errori.append(f"riga {riga}: TROPPI PUNTI ({punti}) nella stessa battuta → spezza con un'azione o lega le frasi: «{b[:90]}»")

    # 2. Eco in apertura di battuta.
    eco = []
    for riga, b in bb:
        testa = b[:60]
        if re.match(r"^(Sì|Si|Già|Certo|Esatto)[,.!]", testa) or re.search(r"^[^.!?]{1,40},\s*sì\b", testa) or re.match(r"^[^.!?]{1,30}\bsì[.!]", testa):
            eco.append((riga, b))
    if len(eco) > 1:
        for riga, b in eco:
            errori.append(f"riga {riga}: ECO, la battuta comincia confermando le parole dell'altro (ammessa al massimo una volta per messaggio): «{b[:70]}»")
    elif eco:
        avvisi.append(f"riga {eco[0][0]}: una battuta comincia confermando (ammessa una volta): «{eco[0][1][:70]}»")

    # 3. Glosse del narratore e grilletti.
    narr = narrazione(testo)
    low = narr.lower()
    for g in GLOSSE:
        if g in low:
            errori.append(f"GLOSSA DEL NARRATORE: \"{g}\" → taglia la spiegazione, lascia parlare battuta e gesto")
    n_grilletti = sum(len(re.findall(p, narr)) for p in GRILLETTI)
    if n_grilletti >= 2:
        errori.append(f"NARRATORE-GRILLETTO ripetuto {n_grilletti} volte (\"Alla parola…\", \"Al complimento…\") → varia la struttura")

    # 4. Mezzo segreto.
    tutto_dialogo = " ".join(b for _, b in bb).lower()
    for m in MEZZO_SEGRETO:
        if m in tutto_dialogo:
            avvisi.append(f"MEZZO SEGRETO: \"{m}\" → al massimo una volta per sessione, e solo se motivato")

    # 5. Assoluti in bocca ai PNG.
    for riga, b in bb:
        for a in ASSOLUTI:
            if re.search(rf"\b{a}\b", b.lower()):
                avvisi.append(f"riga {riga}: ASSOLUTO \"{a}\" in una battuta → serve davvero? «{b[:70]}»")

    # 6. Possibili concetti ripetuti: parole piene che tornano in 3+ battute diverse.
    conta = Counter()
    for _, b in bb:
        parole = {p.lower() for p in PAROLA.findall(b) if len(p) >= 6 and p.lower() not in STOP}
        conta.update(parole)
    ripetute = [p for p, n in conta.items() if n >= 3]
    if ripetute:
        avvisi.append("PAROLE RIPETUTE in 3+ battute (controlla che non sia lo stesso concetto detto più volte): " + ", ".join(sorted(ripetute)))

    # 7. Narrazione a singhiozzo: 3+ frasi consecutive brevissime fuori dai dialoghi.
    for par in [p for p in narr.split("\n") if p.strip()]:
        ff = frasi(par)
        serie = 0
        for f in ff:
            if len(PAROLA.findall(f)) <= 5:
                serie += 1
                if serie == 3:
                    avvisi.append(f"NARRAZIONE A SINGHIOZZO: tre frasi brevissime di fila → fondile: \"{par.strip()[:90]}\"")
                    break
            else:
                serie = 0

    return errori, avvisi


def main():
    testo = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    errori, avvisi = controlla(testo)
    n = len(battute(testo))
    print(f"Battute analizzate: {n}")
    for e in errori:
        print("❌ " + e)
    for a in avvisi:
        print("⚠️  " + a)
    if not errori and not avvisi:
        print("✅ Nessun problema trovato.")
    elif not errori:
        print("✅ Nessun errore. Valuta gli avvisi.")
    sys.exit(1 if errori else 0)


if __name__ == "__main__":
    main()
