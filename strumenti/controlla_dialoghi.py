#!/usr/bin/env python3
"""Controllo automatico dei dialoghi del master.

Il master incolla la bozza del messaggio e lo script segnala gli errori
vietati da regole/06-dialoghi.md e regole/07-dialoghi-shonen.md:
- battute a telegramma (frasi corte e piatte chiuse dal punto, una dopo l'altra);
- risposte a eco ("X, sì", "Sì, ..." in apertura di battuta);
- glosse del narratore e narratore-grilletto;
- "mezzo segreto" interrotto;
- assoluti in bocca ai PNG;
- parole ripetute tra battute diverse (possibili concetti ripetuti);
- linguaggio da terapeuta ("ne hai diritto", "è comprensibile"...);
- possibili errori di concordanza dei tempi (timori e pensieri al passato);
- esito troppo corto (minimo 5000 caratteri, 3500 con --breve);
- eco delle parole del giocatore (battute o narrazione che ripetono il suo messaggio);
- battute-monologo, accumulo di episodi, pensieri narrati, ipotesi sentimentali.

Uso (il messaggio del giocatore prima, poi la riga ===ESITO===, poi la bozza):
  python3 strumenti/controlla_dialoghi.py <<'EOF'
  ...azione del giocatore, copiata così com'è...
  ===ESITO===
  ...bozza dell'esito...
  EOF
Senza la riga ===ESITO=== tutto il testo è trattato come bozza, e il controllo
dell'eco non si può fare.

Opzioni:
  --breve          esito che non regge di più (un round di combattimento, uno
                   scambio rapido): minimo 3500 caratteri invece di 5000
  --solo-dialoghi  nessun controllo di lunghezza: per battute singole, per i
                   messaggi che chiamano un tiro e per le risposte fuori gioco

La lunghezza si conta spazi compresi, senza i blocchi di calcolo tra ``` e
senza le righe fuori gioco tra parentesi quadre.

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
GRILLETTI = [r"\bAlla parola\b", r"\bAl complimento\b", r"\bAll'ultima frase\b", r"\bSull'ultima frase\b",
             r"\b[Ss]u «", r"\b[Aa]rriv\w* a «", r"\b[Ff]u su «", r"\b[Aa]l nome di [A-Z]", r"\b[Ii]l nome di [A-Z]"]
CLICHE = ["ogni parola messa al suo posto", "un momento di troppo", "qualcosa le cambiava", "qualcosa gli cambiava",
          "non sentì niente di tutto questo", "di chi dorme male", "il silenzio era assordante", "l'aria si fece pesante",
          "un brivido gli corse", "un brivido le corse"]
VERBI_MENTALI = re.compile(r"\b(pensò|pensava|decise|capì|si rese conto|sapeva che|si chiese)\b")
EPISODI = re.compile(r"\b(la sera|la notte|la mattina|quel giorno|il giorno|oggi|ieri|a scuola|a Nova City|al negozio|davanti al muro)\b", re.IGNORECASE)
IPOTESI_SENTIMENTALE = re.compile(r"\b(volevo che|speravo che|sognavo che)\b[^.?!]*\bun giorno\b|\bun giorno, quando\b", re.IGNORECASE)
STOP_ECO = set("""il lo la i gli le l un uno una di d a da in con su per tra fra e ed o ma che non è sono ho hai ha
abbiamo avete hanno mi ti si ci vi ne me te se del dello della dei degli delle al allo alla ai agli alle dal dallo
dalla dai dagli dalle nel nello nella nei negli nelle sul sullo sulla sui sugli sulle io tu lui lei noi voi loro
più già anche come quando dove cosa chi perché poi così questo questa quello quella mio mia tuo tua suo sua
nostro nostra c era sei siamo""".split())
VOCABOLARIO_IA = ["intenso", "intensa", "intensi", "intense", "palpabile", "un misto di", "carico di", "carica di",
                  "si stagliava", "si ergeva", "fungeva da", "un velo di", "in qualche modo", "non poté fare a meno",
                  "qualcosa di simile a", "una sorta di", "per la prima volta da quando", "niente sarebbe stato più",
                  "avrebbe cambiato tutto"]
GERUNDIO_COMMENTO = re.compile(r",\s*(rivelando|tradendo|dimostrando|segno che|come a dire|quasi a dire|a testimoniare)\b", re.IGNORECASE)
NEGAZIONE_CORREZIONE = re.compile(r"\bnon era\b[^.!?;]{1,50},\s*era\b|\bnon (solo|soltanto)\b[^.!?;]{1,60}\bma (anche )?", re.IGNORECASE)
LUNGA_AVVISO = 350
LUNGA_ERRORE = 500
MEZZO_SEGRETO = ["lascia perdere", "fai finta che non", "non ho detto niente", "dimentica quello che"]
ASSOLUTI = ["sempre", "mai", "tutti", "nessuno", "ogni volta"]
TERAPEUTA = [
    "ne hai diritto", "ne hai tutto il diritto", "hai tutto il diritto", "è comprensibile",
    "è normale che tu", "non ti giudico", "voglio essere onest", "ho bisogno che tu sappia",
    "i tuoi sentimenti", "sono qui per te", "capisco come ti senti",
]
PASSATO_PENSIERO = re.compile(
    r"\b(avevo|aveva|avevamo) paura\b|\b(temevo|temeva|pensavo|pensava|credevo|credeva|speravo|sperava|immaginavo|ero sicur[oa]|ero convint[oa])\b",
    re.IGNORECASE)
SUBORDINATA = re.compile(r"\b(che|se|appena|quando|finché)\b", re.IGNORECASE)
CONDIZ_CONGIUNT = re.compile(
    r"\b\w+(rei|resti|rebbe|remmo|reste|rebbero|ssi|sse|ssimo|ssero)\b|\b(fosse|fossi|fossero|sia|siano|abbia|abbiano)\b",
    re.IGNORECASE)
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
        if re.match(r"^(Sì|Si|Già|Certo|Esatto)[,.!]", testa) or re.search(r"^[^.!?]{1,40},\s*sì\b", testa) or re.match(r"^[^.!?]{1,30}\bsì[.!]", testa) or re.match(r"^(\S+\s+){1,4}sì[,.!…]", testa):
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
    for c in CLICHE:
        if c in low:
            errori.append(f"FRASE FATTA: \"{c}\" → toglila e mostra la cosa concreta, o niente")
    trovate = [v for v in VOCABOLARIO_IA if re.search(rf"\b{re.escape(v)}\b", testo.lower())]
    if trovate:
        avvisi.append("VOCABOLARIO DA IA: " + ", ".join(f"\"{v}\"" for v in trovate) + " → parole semplici e concrete, o il fatto e basta")
    for m in GERUNDIO_COMMENTO.finditer(narr):
        avvisi.append(f"GERUNDIO DI COMMENTO: \"{m.group(0).strip(', ')}\" → la frase spiega cosa significa il gesto: taglia, il gesto basta")
    for m in NEGAZIONE_CORREZIONE.finditer(testo):
        avvisi.append(f"NEGAZIONE-CORREZIONE: \"{m.group(0)[:50]}\" → «non era X, era Y» per dare enfasi: di' Y")
    for m in VERBI_MENTALI.finditer(narr):
        avvisi.append(f"VERBO MENTALE nella narrazione: \"{m.group(0)}\" → i pensieri dei PNG non si narrano e Akira non decide né pensa al posto del giocatore")
    n_grilletti = sum(len(re.findall(p, testo)) for p in GRILLETTI)
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

    # 4-bis. Battute-monologo: una persona non dice tutto questo d'un fiato.
    for riga, b in bb:
        if len(b) > LUNGA_ERRORE:
            errori.append(f"riga {riga}: MONOLOGO, battuta di {len(b)} caratteri senza interruzioni → tieni una sola idea, oppure spezzala con un'azione o con la reazione dell'altro (regole/08): «{b[:70]}»")
        elif len(b) > LUNGA_AVVISO:
            avvisi.append(f"riga {riga}: battuta lunga ({len(b)} caratteri): una persona la direbbe davvero tutta d'un fiato? «{b[:70]}»")

    # 4-ter. Accumulo di episodi e ipotesi sentimentali dentro una battuta.
    for riga, b in bb:
        episodi = EPISODI.findall(b)
        if len(episodi) >= 3:
            avvisi.append(f"riga {riga}: ACCUMULO DI EPISODI ({', '.join(episodi)}) → un fatto basta, l'elenco di prove è un tic dei testi generati: «{b[:70]}»")
        if IPOTESI_SENTIMENTALE.search(b):
            avvisi.append(f"riga {riga}: IPOTESI SENTIMENTALE (\"volevo che un giorno…\") → serve alla scena o solo a commuovere? «{b[:70]}»")

    # 5-bis. Linguaggio da terapeuta.
    for riga, b in bb:
        for t in TERAPEUTA:
            if t in b.lower():
                errori.append(f"riga {riga}: LINGUAGGIO DA TERAPEUTA \"{t}\" → una persona arrabbiata o in colpa non valida le emozioni dell'altro, riscrivi in modo diretto: «{b[:70]}»")

    # 5-ter. Concordanza dei tempi: timore o pensiero al passato seguito da una subordinata
    # senza condizionale né congiuntivo ("Avevo paura che appena lo viene a sapere comincia…").
    for riga, b in bb:
        for f in frasi(b):
            m = PASSATO_PENSIERO.search(f)
            if not m:
                continue
            resto = f[m.end():]
            if SUBORDINATA.search(resto) and not CONDIZ_CONGIUNT.search(resto):
                avvisi.append(f"riga {riga}: CONCORDANZA DEI TEMPI, timore o pensiero al passato: il futuro di allora va al condizionale passato (avrebbe cominciato), l'ipotesi al congiuntivo trapassato (se lo fosse venuto a sapere): «{f[:90]}»")
                break

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


MINIMO_ESITO = 5000
MINIMO_BREVE = 3500


def lunghezza_esito(testo):
    """Caratteri della narrazione, spazi compresi, senza calcoli tra ``` e righe fuori gioco."""
    senza_calcoli = re.sub(r"```.*?```", "", testo, flags=re.DOTALL)
    righe = [r for r in senza_calcoli.split("\n") if not r.strip().startswith("[")]
    return len("\n".join(righe).strip())


def parole_eco(t):
    return re.findall(r"[a-zà-ÿ]+", t.lower())


def eco_giocatore(azione, esito):
    """Tratti dell'esito che ripetono parola per parola il messaggio del giocatore."""
    pa, pe = parole_eco(azione), parole_eco(esito)
    piene = lambda g: sum(1 for w in g if w not in STOP_ECO)
    cercati = set()
    for n, minimo in ((3, 2), (4, 1)):
        for i in range(len(pa) - n + 1):
            g = tuple(pa[i:i + n])
            if piene(g) >= minimo:
                cercati.add(g)
    coperte = [False] * len(pe)
    for n in (3, 4):
        for i in range(len(pe) - n + 1):
            if tuple(pe[i:i + n]) in cercati:
                for k in range(i, i + n):
                    coperte[k] = True
    tratti, i = [], 0
    while i < len(pe):
        if coperte[i]:
            j = i
            while j < len(pe) and coperte[j]:
                j += 1
            tratti.append(" ".join(pe[i:j]))
            i = j
        else:
            i += 1
    return tratti


def main():
    args = sys.argv[1:]
    breve = "--breve" in args
    solo_dialoghi = "--solo-dialoghi" in args
    file = [a for a in args if not a.startswith("--")]
    testo = open(file[0], encoding="utf-8").read() if file else sys.stdin.read()
    azione = None
    if "===ESITO===" in testo:
        azione, testo = testo.split("===ESITO===", 1)
    errori, avvisi = controlla(testo)
    if azione is not None:
        tratti = eco_giocatore(azione, testo)
        if len(tratti) >= 2:
            errori.append("ECO DEL GIOCATORE: l'esito ripete parola per parola il suo messaggio (" + " · ".join(f"«{t}»" for t in tratti) + ") → il PNG risponde al senso con parole sue, e il narratore non cita Akira")
        elif tratti:
            avvisi.append(f"ripresa delle parole del giocatore: «{tratti[0]}» → ammessa una volta, solo se serve a ribaltarle")
    elif not solo_dialoghi:
        avvisi.append("manca il messaggio del giocatore prima di ===ESITO===: il controllo dell'eco non è stato fatto")
    if not solo_dialoghi:
        minimo = MINIMO_BREVE if breve else MINIMO_ESITO
        n_car = lunghezza_esito(testo)
        print(f"Lunghezza dell'esito: {n_car} caratteri (minimo {minimo})")
        if n_car < minimo:
            errori.append(f"ESITO TROPPO CORTO: {n_car} caratteri su {minimo} → approfondisci con sostanza (il PNG risponde nel merito, stati d'animo mostrati, altri PNG presenti, dettagli coerenti con la scena), mai con riempitivi né con azioni di Akira (regole/04-metodo-mondo-vivo.md §9)")
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
