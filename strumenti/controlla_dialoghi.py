#!/usr/bin/env python3
"""Controllo automatico degli esiti del master.

Prosa di regole/05-prosa-shonen.md (terza persona vicina ad Akira, periodi
scorrevoli) e battute di regole/06-dialoghi.md. Segnala:
- eco delle parole del giocatore (battute dei PNG o narrazione che ripetono il suo messaggio);
- battute-telegramma, battute-catena («…, e…, e…») e battute-monologo;
- PNG senza emozione (battute piatte, senza punteggiatura espressiva);
- frasi fatte, nella narrazione e nelle battute;
- una frase per riga e narrazione a singhiozzo;
- glosse del narratore, narratore-grilletto, linguaggio da terapeuta;
- metafore (quantità figurate, emozioni che «divorano»), similitudini nelle
  battute o più di una nella narrazione;
- tentativi del giocatore (convincere, scoprire, nascondersi, colpire…)
  risolti senza chiamare il tiro;
- esito troppo corto (minimo 5000 caratteri, 3500 con --breve);
- avvisi: battute e frasi lunghe, assoluti, mezzo segreto, tempi verbali,
  accumulo di episodi, ipotesi sentimentali, parole ripetute, narrazione in
  seconda persona o al presente, Akira deciso dal master.

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
                   scambio rapido, la risposta di un PNG in un dialogo a due):
                   minimo 3500 caratteri invece di 5000
  --solo-dialoghi  nessun controllo di lunghezza: per battute singole e per le
                   risposte fuori gioco (un messaggio che contiene /tira salta
                   da solo il controllo di lunghezza)
  --senza-prova "motivo"
                   il giocatore tenta qualcosa ma il master ha deciso che non
                   serve il tiro: il motivo dice quale domanda della prova del
                   tiro (regole/02 §1-bis) ha avuto un no

Prova del tiro: se il messaggio del giocatore contiene un tentativo e la bozza
non chiama il tiro (/tira), il controllo dà errore. Se il messaggio del
giocatore contiene già un tiro (/tira, 🎲), il controllo non si fa.

Battute dei PNG: tra «…». Battute di Akira (riportate pari pari dal giocatore),
voci telepatiche e voci nella testa: tra "…". La lunghezza si conta spazi
compresi, senza i blocchi di calcolo tra ``` e senza le righe fuori gioco tra
parentesi quadre.

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
FRASI_FATTE = [
    (r"\bstomaco\b[^.!?]{0,30}\b(?:strin|stret|chius|chiud|annod|contor|sottosopra)\w*|\b(?:strin|chius|chiud)\w*\s+lo stomaco", "lo stomaco che si stringe"),
    (r"\bnodo (?:alla gola|allo stomaco|in gola)\b", "il nodo alla gola"),
    (r"\bcuore\b[^.!?]{0,25}\b(?:salt\w*|perde|perse|manca|mancò)\s+un battito|\bcuore in gola\b", "il cuore che salta un battito"),
    (r"\bsangue\b[^.!?]{0,20}\b(?:gel|ghiacci)\w*", "il sangue che si gela"),
    (r"\bbrivid\w*", "il brivido"),
    (r"\b(?:tratten|trattien|trattenn)\w*\s+il (?:fiato|respiro)\b|\bfiato sospeso\b|\bfiato (?:gli|le|ti|mi) si mozz\w*", "il fiato trattenuto"),
    (r"\bnocche\b[^.!?]{0,20}\b(?:bianch|sbianc)\w*", "le nocche bianche"),
    (r"\b(?:serr|contra|strins|string)\w*\s+(?:la\s+)?mascella\b|\bmascella\b[^.!?]{0,15}\b(?:serr|contra|indur)\w*", "la mascella serrata"),
    (r"\bdeglut\w*", "deglutire"),
    (r"\b(?:linea|riga) sottile\b", "le labbra in una linea sottile"),
    (r"\bsbatt\w*\s+(?:le\s+)?palpebre\b", "sbattere le palpebre"),
    (r"\b(?:alz|inarc|sollev)\w*\s+(?:un|il)\s+sopracciglio\b", "il sopracciglio alzato"),
    (r"\bocchi al cielo\b", "gli occhi al cielo"),
    (r"\bocchi\b[^.!?]{0,15}\bsi (?:assottigli|ridu|strins|stringo)\w*", "gli occhi che si assottigliano"),
    (r"\bsorriso che non (?:arriv|raggiung)\w*", "il sorriso che non arriva agli occhi"),
    (r"\b(?:sorriso|risata)\s+amar\w*|\bamaramente\b|\brisata senza (?:allegria|gioia)\b", "il sorriso amaro"),
    (r"\b(?:sbuff|risat)\w*\b[^.!?]{0,25}\bdal naso\b|\bdal naso\b[^.!?]{0,15}\b(?:sbuff|risat)\w*", "lo sbuffo dal naso"),
    (r"\bpass\w*\s+una mano\s+(?:tra|fra|nei|sui)\s+(?:i\s+)?capelli\b|\bpass\w*\s+(?:una mano|le mani)\s+sul (?:viso|volto)\b", "la mano tra i capelli"),
    (r"\b(?:respiro|sospiro) profondo\b|\brespir\w*\s+a fondo\b", "il respiro profondo"),
    (r"\b(?:secondo|secondi|momento|momenti|istante|istanti|attimo|attimi|pausa)\s+di troppo\b|\bpausa troppo lunga\b", "il secondo di troppo"),
    (r"\btempo\b[^.!?]{0,15}\b(?:si ferm|sembr\w* fermarsi|si dilat|sembr\w* dilatarsi)\w*", "il tempo che si ferma"),
    (r"\bsilenzio\b[^.!?]{0,10}\b(?:cal[aò]|scese|scende|pesante|assordante|carico|denso|teso)\b", "il silenzio che cala"),
    (r"\baria\b[^.!?]{0,15}\b(?:si fa|si fece|si è fatta|diventa|diventò)\s+(?:pesante|densa|elettrica|irrespirabile)\b", "l'aria che si fa pesante"),
    (r"\bnon c'(?:è|era) niente di \w+ nella (?:sua )?voce\b|(?:^|[.!?…]\s+)(?:È|E'|Era) peggio[.!]", "«non c'è niente di… È peggio.»"),
    (r"\bqualcosa\b[^.!?]{0,20}\bsi (?:rompe|ruppe|spezza|spezzò|incrina|incrinò)\b[^.!?]{0,15}\bdentro\b", "qualcosa che si rompe dentro"),
    (r"\be in quel momento capì\b|\bin quell'istante capì\b", "e in quel momento capì"),
    (r"\bannu\w*\s+(?:grave|lenta)mente\b", "annuire gravemente"),
    (r"\bocchi lucidi\b|\blacrima solitaria\b", "gli occhi lucidi"),
    (r"\bpeso (?:sul|nel) petto\b|\bpetto (?:stretto|che si stringe)\b", "il peso sul petto"),
    (r"\bvoce\b[^.!?]{0,10}\bsi (?:incrin|spezz)\w*|\bvoce rotta\b", "la voce che si spezza"),
    (r"\bun'eternità\b", "un'eternità"),
]
FRASI_FATTE_RX = [(re.compile(rx, re.IGNORECASE | re.MULTILINE), nome) for rx, nome in FRASI_FATTE]
FRASI_FATTE_BATTUTE = [
    "mi fai venire il mal di testa", "dobbiamo parlare", "non è come pensi", "non è quello che sembra",
    "fidati di me", "andrà tutto bene", "ce la faremo", "non sei solo", "non sei sola", "non è il momento",
    "lo sai benissimo", "sai benissimo", "è complicato", "non è colpa tua", "possiamo parlarne",
    "lascia che ti spieghi", "ascoltami bene", "non ci posso credere", "ti conosco troppo bene",
    "sono fiero di te", "sono fiera di te", "non mi lasci scelta", "è finita", "abbiamo un problema",
    "non ne vale la pena",
]
CLICHE = ["ogni parola messa al suo posto", "un momento di troppo", "qualcosa le cambiava", "qualcosa gli cambiava",
          "non sentì niente di tutto questo", "di chi dorme male", "il silenzio era assordante", "l'aria si fece pesante"]
MEZZO_SEGRETO = ["lascia perdere", "fai finta che non", "non ho detto niente", "dimentica quello che"]
ASSOLUTI = ["sempre", "mai", "tutti", "nessuno", "ogni volta"]
TERAPEUTA = [
    "ne hai diritto", "ne hai tutto il diritto", "hai tutto il diritto", "è comprensibile",
    "è normale che tu", "non ti giudico", "voglio essere onest", "ho bisogno che tu sappia",
    "i tuoi sentimenti", "sono qui per te", "capisco come ti senti",
]
VOCABOLARIO_IA = ["palpabile", "un misto di", "in qualche modo", "qualcosa di simile a", "non poté fare a meno"]
METAFORA_QUANTITA = re.compile(
    r"\b(?:un|una|un'|quell'|quel|quella)\s*(?:[a-zà-ÿ]+\s+)?(?:mare|oceano|marea|abisso|velo|uragano)\s+d(?:i\b|')",
    re.IGNORECASE)
METAFORA_EMOZIONE = re.compile(
    r"\b(?:la rabbia|il dolore|la paura|l'odio|la colpa|il senso di colpa|la tristezza|l'angoscia|la vergogna|"
    r"la gelosia|il terrore|la furia|il rimorso|la frustrazione|l'ansia|il panico)\s+(?:ti|gli|le|lo|la|li|si|vi|ci)?\s*"
    r"(?:divor|mord|corrod|trafigg|attanagli|afferr|stritol|consum|lacer|dilani|rod|azzann|graffi|artigli)\w*",
    re.IGNORECASE)
SIMILITUDINE = re.compile(
    r"\bcome (?:un|una|uno|un'|se|il|lo|la|i|gli|le|l')(?![a-zà-ÿ])(?!\s*(?:qualunque|qualsiasi|niente)\b)|\bsimile a\b|\bquasi fosse\b|\balla stregua d",
    re.IGNORECASE)
SIMILITUDINE_BATTUTA = re.compile(r"\bcome (?:(?:un|una|uno)\s+|un')(?!qualunque\b|qualsiasi\b)[a-zà-ÿ]+", re.IGNORECASE)
TENTATIVI = [
    # «cercherò di…» detto da Akira è un'intenzione per dopo, non un tentativo adesso
    ("tentativo", re.compile(r"\b(?:prov|tent|cerc)[a-zà-ÿ]*(?<!rò)\s+(?:a|ad|di)\s", re.IGNORECASE)),
    ("convincere, intimidire, ingannare", re.compile(
        r"\b(?:convinc|persuad|intimid|ingann|bluff|corromp|lusing|implor|supplic|ricatt|minacc)[a-zà-ÿ]*", re.IGNORECASE)),
    ("mentire", re.compile(r"\b(?:mentir[a-zà-ÿ]*|mentend[a-zà-ÿ]*|mentisc[a-zà-ÿ]*|bugi[ae])\b", re.IGNORECASE)),
    ("scoprire, origliare, capire", re.compile(
        r"\b(?:scrut|origli|frug|perquis|indag|esamin|ispezion)[a-zà-ÿ]*|\bspi(?:a|are|ando|erebbe|o)\b|"
        r"\bascolt[a-zà-ÿ]*\s+(?:oltre|dietro|attraverso|di nascosto|meglio)|\btend[a-zà-ÿ]*\s+l'orecchio|"
        r"\bcapire\s+(?:se|cosa|chi|perché|dove|come)\b|\bnot(?:are|i|a)\s+se\b", re.IGNORECASE)),
    ("non farsi scoprire", re.compile(
        r"\bdi nascosto\b|\bfurtiv[a-zà-ÿ]*|\bsgattaiol[a-zà-ÿ]*|\bpedin[a-zà-ÿ]*|\bsenza farsi (?:vedere|sentire|notare|scoprire)\b|"
        r"\b(?:si )?nascond(?:e|ersi|erebbe|endosi)\b", re.IGNORECASE)),
    ("controllo del ki", re.compile(
        r"\b(?:sopprim|soppri|soppress|mascher|nascond|abbass|dos|controll|trattien|tratten|contien|conten|spegn)[a-zà-ÿ]*\s+"
        r"(?:la (?:sua |propria )?aura|l'aura|il (?:suo |proprio )?ki|l'energia)", re.IGNORECASE)),
    ("percepire il ki", re.compile(r"\b(?:percepi|cerc|sond|scandagli)[a-zà-ÿ]*\s+(?:l'aura|le aure|il ki|aure)\b", re.IGNORECASE)),
    ("prova fisica", re.compile(r"\b(?:sollev|scassin|sfond|arrampic|scardin|divell)[a-zà-ÿ]*", re.IGNORECASE)),
    ("combattimento", re.compile(
        r"\b(?:attacc[a-zà-ÿ]*|colpir[a-zà-ÿ]*|colpisc[a-zà-ÿ]*|schiv[a-zà-ÿ]*|parar[a-zà-ÿ]*|scagli[a-zà-ÿ]*|"
        r"(?:sferr|tir|moll|rifil|assest)[a-zà-ÿ]*\s+(?:un|una|un')\s*(?:pugno|calcio|gomitata|ginocchiata|testata|colpo|fendente|montante|gancio|diretto|schiaffo)|"
        r"ki blast|raffica|kamehameha|lancia della giustizia|taiyoken|barriera repulsiva)", re.IGNORECASE)),
]
GIA_TIRATO = re.compile(r"/tira\b|🎲|\bd10\s*=", re.IGNORECASE)
CHIAMA_TIRO = re.compile(r"/tira\b")
GERUNDIO_COMMENTO = re.compile(r",\s*(rivelando|tradendo|dimostrando|segno che|come a dire|quasi a dire|a testimoniare)\b", re.IGNORECASE)
EPISODI = re.compile(r"\b(la sera|la notte|la mattina|quel giorno|il giorno|oggi|ieri|a scuola|a Nova City|al negozio|davanti al muro)\b", re.IGNORECASE)
IPOTESI_SENTIMENTALE = re.compile(r"\b(volevo che|speravo che|sognavo che)\b[^.?!]*\bun giorno\b|\bun giorno, quando\b", re.IGNORECASE)
PASSATO_PENSIERO = re.compile(
    r"\b(avevo|aveva|avevamo) paura\b|\b(temevo|temeva|pensavo|pensava|credevo|credeva|speravo|sperava|immaginavo|ero sicur[oa]|ero convint[oa])\b",
    re.IGNORECASE)
SUBORDINATA = re.compile(r"\b(che|se|appena|quando|finché)\b", re.IGNORECASE)
CONDIZ_CONGIUNT = re.compile(
    r"\b\w+(rei|resti|rebbe|remmo|reste|rebbero|ssi|sse|ssimo|ssero)\b|\b(fosse|fossi|fossero|sia|siano|abbia|abbiano)\b",
    re.IGNORECASE)
AKIRA_DECISO = re.compile(r"\bAkira\s+(?:decise|decide|scelse|sceglie|pensò|pensa|cercò|cerca|volle|vuole|si chiese|si disse)\b")
SECONDA_PERSONA = re.compile(r"\b(?:tuo|tua|tuoi|tue|stringi|allunghi|lanci|guardi|vedi|ti giri|ti alzi|ti volti|ti siedi)\b", re.IGNORECASE)
PRESENTE = re.compile(r"\b(?:guarda|dice|chiede|prende|posa|alza|apre|chiude|torna|resta|sorride|si alza|si gira|si volta|sente|vede|risponde|scuote|abbassa|stringe)\b")
PASSATO_REMOTO = re.compile(r"\b(?:disse|fece|ebbe|vide|sentì|guardò|rispose|chiese|prese|mise|tornò|restò|rimase|alzò|posò|si voltò|si girò|aprì|chiuse|sorrise|scosse|abbassò|strinse)\b")
STOP = set("""
alla allo alle agli dalla dalle dallo della delle dello degli nella nelle nello negli sulla sulle sullo sugli
mentre perché perche quando quello quella quelli quelle questo questa questi queste anche ancora adesso allora
proprio sempre qualcosa niente nulla molto troppo tanto poco dopo prima dentro fuori sopra sotto
essere stato stata sono sei siamo siete hanno avere aveva avevo fatto fare dire detto come cosa cose
""".split())
STOP_ECO = set("""il lo la i gli le l un uno una di d a da in con su per tra fra e ed o ma che non è sono ho hai ha
abbiamo avete hanno mi ti si ci vi ne me te se del dello della dei degli delle al allo alla ai agli alle dal dallo
dalla dai dagli dalle nel nello nella nei negli nelle sul sullo sulla sui sugli sulle io tu lui lei noi voi loro
più già anche come quando dove cosa chi perché poi così questo questa quello quella mio mia tuo tua suo sua
nostro nostra c era sei siamo""".split())

LUNGA_AVVISO = 200       # i testi di riferimento non superano i 205 caratteri per battuta
LUNGA_ERRORE = 300
FRASE_LUNGA = 160        # una frase dentro una battuta
CATENA_FRASE = 120       # una frase con «, e» oltre questa lunghezza è una catena
MINIMO_ESITO = 5000
MINIMO_BREVE = 3500


def normalizza(testo):
    return re.sub(r"\.{3,}", "…", testo)


def battute_png(testo):
    """(numero_riga, battuta) per ogni battuta di PNG tra « e »."""
    out = []
    for m in re.finditer(r"«([^»]*)»", testo):
        riga = testo.count("\n", 0, m.start()) + 1
        out.append((riga, m.group(1).strip()))
    return out


def narrazione(testo):
    return re.sub(r"«[^»]*»|\"[^\"\n]*\"", " ", testo)


def frasi(s):
    return [f.strip() for f in FINE_FRASE.split(s) if f.strip()]


def controlla(testo):
    errori, avvisi = [], []
    bb = battute_png(testo)

    # 1. Battute: catene di «e», monologhi, frasi lunghe.
    for riga, b in bb:
        virgola_e = len(re.findall(r",\s+e\s", b))
        e_totali = len(re.findall(r"\be\s", b))
        frasi_catena = [f for f in frasi(b) if len(f) > CATENA_FRASE and re.search(r",\s+e\s", f)]
        if virgola_e >= 2 or e_totali >= 3 or frasi_catena:
            errori.append(f"riga {riga}: CATENA DI «E», la battuta attacca frasi con «e» per spiegare o giustificare → una cosa per frase, frasi separate da punto o puntini (regole/06): «{b[:80]}»")
        if len(b) > LUNGA_ERRORE:
            errori.append(f"riga {riga}: MONOLOGO, battuta di {len(b)} caratteri → una cosa sola; se il PNG ha altro da dire, una riga di narrazione in mezzo e una battuta nuova: «{b[:70]}»")
        elif len(b) > LUNGA_AVVISO:
            avvisi.append(f"riga {riga}: battuta lunga ({len(b)} caratteri): va divisa? «{b[:70]}»")
        for f in frasi(b):
            if len(f) > FRASE_LUNGA:
                avvisi.append(f"riga {riga}: frase lunga dentro una battuta ({len(f)} caratteri): «{f[:70]}»")
                break

    # 1-bis. Telegrammi: frasi corte e piatte (chiuse dal punto) in fila dentro la stessa battuta.
    piatta = lambda f: f.endswith(".") and not f.endswith("…")
    n_parole = lambda f: len(PAROLA.findall(f))
    for riga, b in bb:
        ff = frasi(b)
        corte = [f for f in ff if n_parole(f) <= 4]
        piatte = [f for f in corte if piatta(f)]
        coppie = [(a, c) for a, c in zip(ff, ff[1:]) if piatta(a) and piatta(c) and n_parole(a) <= 6 and n_parole(c) <= 6]
        if len(piatte) >= 2:
            errori.append(f"riga {riga}: TELEGRAMMA, {len(corte)} frasi corte nella stessa battuta (di cui {len(piatte)} piatte) → una frase intera, o un frammento carico (! ? … —): «{b[:90]}»")
        elif coppie:
            errori.append(f"riga {riga}: FRASI STACCATE, due frasi brevi e piatte di fila chiuse dal punto → uniscile, o rendile cariche: «{coppie[0][0]} {coppie[0][1]}»")
        if sum(1 for f in ff if piatta(f)) >= 4:
            errori.append(f"riga {riga}: TROPPI PUNTI nella stessa battuta → spezza con un'azione o lega le frasi: «{b[:90]}»")
        for f in FRASI_FATTE_BATTUTE:
            if re.search(rf"\b{re.escape(f)}\b", b, re.IGNORECASE):
                errori.append(f"riga {riga}: FRASE FATTA IN BATTUTA \"{f}\" → cosa direbbe QUESTA persona, adesso? (regole/05 §4): «{b[:70]}»")

    # 1-ter. PNG senza emozione: battute senza punteggiatura espressiva.
    espressiva = lambda b: bool(re.search(r"[!?…—]", b)) or bool(re.search(r"\b[A-ZÀ-Ý]{3,}\b", b))
    if len(bb) >= 4:
        quota = sum(1 for _, b in bb if espressiva(b)) / len(bb)
        if quota == 0:
            errori.append(f"PNG SENZA EMOZIONE: nessuna delle {len(bb)} battute ha un esclamativo, una domanda, dei puntini o un'interruzione → si deve sentire cosa provano (regole/06 §2-bis)")
        elif quota < 0.3:
            avvisi.append(f"PNG SENZA EMOZIONE? Solo {round(quota * 100)}% delle battute ha punteggiatura espressiva → copri il nome: si capisce cosa prova chi parla? (regole/06 §2-bis)")

    # 2. Eco in apertura di battuta ("Sì, …", "X, sì").
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

    # 3. Narratore: glosse, frasi fatte, grilletti, Akira in terza persona o deciso, tempo verbale.
    narr = narrazione(testo)
    low = narr.lower()
    for g in GLOSSE:
        if g in low:
            errori.append(f"GLOSSA DEL NARRATORE: \"{g}\" → taglia la spiegazione, lascia parlare battuta e gesto")
    for c in CLICHE:
        if c in low:
            errori.append(f"FRASE FATTA: \"{c}\" → toglila e mostra la cosa concreta")
    n_grilletti = sum(len(re.findall(p, testo)) for p in GRILLETTI)
    if n_grilletti >= 2:
        errori.append(f"NARRATORE-GRILLETTO ripetuto {n_grilletti} volte (una reazione appesa a ogni frase di Akira) → una reazione all'insieme")
    for rx, nome in FRASI_FATTE_RX:
        m = rx.search(narr)
        if m:
            errori.append(f"FRASE FATTA: \"{m.group(0).strip(' .!?…')}\" ({nome}) → scrivi la cosa vera di questa scena, o togli (regole/05 §4)")
    for m in AKIRA_DECISO.finditer(narr):
        avvisi.append(f"AKIRA DECISO DAL MASTER: \"{m.group(0)}\" → decisioni, intenzioni e pensieri li dichiara il giocatore (Regola 5)")
    if len(SECONDA_PERSONA.findall(narr)) >= 3:
        avvisi.append("NARRAZIONE IN SECONDA PERSONA → si racconta in terza persona vicina ad Akira (regole/05 §2, punto 3)")
    if len(PRESENTE.findall(narr)) >= 6 and len(PASSATO_REMOTO.findall(narr)) < 3:
        avvisi.append("NARRAZIONE AL PRESENTE → il racconto è al passato remoto e all'imperfetto (regole/05 §2, punto 3)")
    righe_narr = [r for r in testo.split("\n") if r.strip() and "«" not in r and not r.strip().startswith(("[", "```", "|"))]
    isolate = [r for r in righe_narr if len(PAROLA.findall(r)) <= 25]
    if len(righe_narr) >= 8 and len(isolate) / len(righe_narr) >= 0.6:
        errori.append(f"UNA FRASE PER RIGA: {len(isolate)} paragrafi di narrazione su {len(righe_narr)} sono di una o due frasi corte → paragrafi di più frasi, periodi che scorrono (regole/05 §2)")
    serie = 0
    for f in frasi(re.sub(r"\s*\n\s*", " ", narr)):
        serie = serie + 1 if len(PAROLA.findall(f)) <= 5 else 0
        if serie == 3:
            avvisi.append(f"NARRAZIONE A SINGHIOZZO: tre frasi brevissime di fila → fondile (regole/05 §2): \"{f[:60]}\"")
            break
    trovate = [v for v in VOCABOLARIO_IA if re.search(rf"\b{re.escape(v)}\b", low)]
    if trovate:
        avvisi.append("VOCABOLARIO DA IA: " + ", ".join(f"\"{v}\"" for v in trovate) + " → parole concrete")
    for m in METAFORA_QUANTITA.finditer(narr):
        errori.append(f"METAFORA: \"{m.group(0)}…\" → zero metafore (decisione del giocatore): dì la cosa concreta, cosa si vede, quanto è grande, cosa fa (regole/05 §3)")
    for m in METAFORA_EMOZIONE.finditer(testo):
        errori.append(f"METAFORA: \"{m.group(0)}\" → un'emozione non divora e non morde: mostra cosa fa il corpo, o nomina l'emozione e basta (regole/05 §3)")
    simili = [m.group(0) for m in SIMILITUDINE.finditer(narr)]
    if len(simili) > 1:
        avvisi.append(f"SIMILITUDINI: {len(simili)} nella narrazione (" + ", ".join(f"\"{x}…\"" for x in simili[:5]) + ") → al massimo una per esito, e nessuna metafora: riscrivi con dettagli concreti")
    for riga, b in bb:
        m = SIMILITUDINE_BATTUTA.search(b)
        if m:
            avvisi.append(f"riga {riga}: SIMILITUDINE IN UNA BATTUTA \"{m.group(0)}\" → i PNG parlano concreto, niente immagini: «{b[:70]}»")
    for m in GERUNDIO_COMMENTO.finditer(narr):
        avvisi.append(f"GERUNDIO DI COMMENTO: \"{m.group(0).strip(', ')}\" → la frase spiega cosa significa il gesto: taglia, il gesto basta")

    # 4. Mezzo segreto, assoluti, terapeuta, tempi, accumulo, ipotesi sentimentali.
    tutto_dialogo = " ".join(b for _, b in bb).lower()
    for m in MEZZO_SEGRETO:
        if m in tutto_dialogo:
            avvisi.append(f"MEZZO SEGRETO: \"{m}\" → al massimo una volta per sessione, e solo se motivato")
    for riga, b in bb:
        for a in ASSOLUTI:
            if re.search(rf"\b{a}\b", b.lower()):
                avvisi.append(f"riga {riga}: ASSOLUTO \"{a}\" in una battuta → serve davvero? «{b[:70]}»")
        for t in TERAPEUTA:
            if t in b.lower():
                errori.append(f"riga {riga}: LINGUAGGIO DA TERAPEUTA \"{t}\" → una persona arrabbiata o in colpa non valida le emozioni dell'altro: «{b[:70]}»")
        for f in frasi(b):
            m = PASSATO_PENSIERO.search(f)
            if m:
                resto = f[m.end():]
                if SUBORDINATA.search(resto) and not CONDIZ_CONGIUNT.search(resto):
                    avvisi.append(f"riga {riga}: CONCORDANZA DEI TEMPI, timore o pensiero al passato: il futuro di allora va al condizionale passato, l'ipotesi al congiuntivo trapassato: «{f[:90]}»")
                    break
        episodi = EPISODI.findall(b)
        if len(episodi) >= 3:
            avvisi.append(f"riga {riga}: ACCUMULO DI EPISODI ({', '.join(episodi)}) → un fatto basta: «{b[:70]}»")
        if IPOTESI_SENTIMENTALE.search(b):
            avvisi.append(f"riga {riga}: IPOTESI SENTIMENTALE (\"volevo che un giorno…\") → serve alla scena o solo a commuovere? «{b[:70]}»")

    # 5. Possibili concetti ripetuti: parole piene che tornano in 3+ battute diverse.
    conta = Counter()
    for _, b in bb:
        conta.update({p.lower() for p in PAROLA.findall(b) if len(p) >= 6 and p.lower() not in STOP})
    ripetute = [p for p, n in conta.items() if n >= 3]
    if ripetute:
        avvisi.append("PAROLE RIPETUTE in 3+ battute (controlla che non sia lo stesso concetto detto più volte): " + ", ".join(sorted(ripetute)))

    return errori, avvisi


def parole_eco(t):
    return re.findall(r"[a-zà-ÿ]+", t.lower())


def eco_giocatore(azione, esito):
    """Tratti dell'esito (fuori dalle battute di Akira tra "…") che ripetono il messaggio del giocatore."""
    esito_senza_akira = re.sub(r"\"[^\"\n]*\"", " ", esito)
    pa, pe = parole_eco(azione), parole_eco(esito_senza_akira)
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


def tentativi(azione):
    """Tentativi del giocatore che potrebbero richiedere un tiro (fuori dalle note tra parentesi quadre)."""
    testo = re.sub(r"\[[^\]]*\]", " ", azione)
    trovati = []
    for nome, rx in TENTATIVI:
        m = rx.search(testo)
        if m:
            trovati.append((nome, m.group(0).strip()))
    return trovati


def lunghezza_esito(testo):
    """Caratteri della narrazione, spazi compresi, senza calcoli tra ``` e righe fuori gioco."""
    senza_calcoli = re.sub(r"```.*?```", "", testo, flags=re.DOTALL)
    righe = [r for r in senza_calcoli.split("\n") if not r.strip().startswith("[")]
    return len("\n".join(righe).strip())


def main():
    args = sys.argv[1:]
    breve = solo_dialoghi = False
    senza_prova = None
    file = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--breve":
            breve = True
        elif a == "--solo-dialoghi":
            solo_dialoghi = True
        elif a.startswith("--senza-prova="):
            senza_prova = a.split("=", 1)[1]
        elif a == "--senza-prova":
            senza_prova = args[i + 1] if i + 1 < len(args) else ""
            i += 1
        else:
            file.append(a)
        i += 1
    testo = open(file[0], encoding="utf-8").read() if file else sys.stdin.read()
    testo = normalizza(testo)
    azione = None
    if "===ESITO===" in testo:
        azione, testo = testo.split("===ESITO===", 1)
    errori, avvisi = controlla(testo)
    chiama_tiro = bool(CHIAMA_TIRO.search(testo))
    trovati = []
    if azione is not None and not GIA_TIRATO.search(azione):
        trovati = tentativi(azione)
        if senza_prova is not None:
            if len(senza_prova.strip()) < 15:
                errori.append("--senza-prova senza un motivo vero → scrivi quale domanda della prova del tiro ha avuto un no e perché (regole/02 §1-bis)")
            else:
                print(f"Tiro escluso dal master: {senza_prova.strip()}")
        elif trovati and not chiama_tiro:
            errori.append("TIRO NON VALUTATO: il giocatore tenta qualcosa (" + ", ".join(f"{n}: «{t}»" for n, t in trovati) + ") e la bozza non chiama il tiro → prova del tiro (regole/02 §1-bis, regole/08 fase 1-bis): se Akira tenta di ottenere qualcosa, l'esito è incerto e fallire costa, fermati prima del risultato e chiama la prova (tipo, CD, modificatori) o il tiro di combattimento; se non serve, ripassa il controllo con --senza-prova \"motivo\"")
    if chiama_tiro:
        n_tiro = lunghezza_esito(testo)
        print("Il messaggio chiama un tiro: niente controllo di lunghezza.")
        if n_tiro > 3000:
            avvisi.append(f"il messaggio chiama un tiro ma è lungo {n_tiro} caratteri: hai narrato l'esito? Ci si ferma al momento incerto, prima del risultato")
        if not re.search(r"\bCD\s*\d", testo) and not any(n == "combattimento" for n, _ in trovati):
            avvisi.append("PROVA SENZA CD: per una prova di abilità servono tipo di prova, CD e modificatori voce per voce con il totale (regole/02 §1-bis)")
    if azione is not None:
        tratti = eco_giocatore(azione, testo)
        if len(tratti) >= 2:
            errori.append("ECO DEL GIOCATORE: l'esito ripete parola per parola il suo messaggio fuori dalle battute di Akira (" + " · ".join(f"«{t}»" for t in tratti) + ") → i PNG rispondono al senso con parole loro; le parole di Akira, se servono, si riportano tra \"…\"")
        elif tratti:
            avvisi.append(f"ripresa delle parole del giocatore: «{tratti[0]}» → ammessa una volta, solo se serve")
    elif not solo_dialoghi:
        avvisi.append("manca il messaggio del giocatore prima di ===ESITO===: il controllo dell'eco non è stato fatto")
    if not solo_dialoghi and not chiama_tiro:
        minimo = MINIMO_BREVE if breve else MINIMO_ESITO
        n_car = lunghezza_esito(testo)
        print(f"Lunghezza dell'esito: {n_car} caratteri (minimo {minimo})")
        if n_car < minimo:
            errori.append(f"ESITO TROPPO CORTO: {n_car} caratteri su {minimo} → sviluppa la scena (cosa fanno i PNG, cosa cambia, chi altro reagisce), mai con riempitivi né con battute allungate (regole/08)")
    print(f"Battute dei PNG analizzate: {len(battute_png(testo))}")
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
