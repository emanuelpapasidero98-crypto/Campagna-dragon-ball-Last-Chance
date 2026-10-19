# Comandi chat

Tutti i comandi che puoi usare per giocare a *Dragon Ball Last Chance* con Claude come master.

---

## Prima di tutto: come aprire una nuova chat di gioco
1. Su claude.ai/code (o nell'app) avvia una **nuova sessione** e seleziona la repo **`Campagna-dragon-ball-Last-Chance`**, ramo **`main`**.
2. Scrivi **`/inizia-sessione`**.

Claude legge in automatico le regole, il mondo e la memoria segreta del master, quindi non devi rispiegare nulla.

---

## Comandi principali (iniziano con `/`)
Il comando va scritto **all'inizio del messaggio**.

### `/inizia-sessione`
**Cosa fa:** apre una sessione di gioco.
- Scarica da GitHub l'ultima versione della memoria.
- Rilegge regole, stato del mondo, scheda di Akira, cronaca e piani segreti dei PNG.
- Crea il file della nuova sessione in `cronaca/sessioni/`.
- Ti mostra un **"Nelle puntate precedenti…"** con solo ciò che Akira sa, poi il suo stato (HP, Ki, condizioni).
- **Riprende la scena** esattamente da dove si era interrotta. La prima volta parte dalla cena nella foresta di Nova City.

**Esempio:** `/inizia-sessione`

### `/tira [modificatore] [azione]`
**Cosa fa:** tiri **tu** il d10 per Akira.
- Il risultato è casuale vero (generatore crittografico): né tu né il master potete sceglierlo.
- Ogni tiro viene registrato con data e ora in `cronaca/registro-dadi.md`.
- Il master ti mostra il risultato così com'è, poi tira i dadi dei PNG, fa i calcoli del sistema di gioco (in un riquadro compatto) e narra l'esito.
- Il **modificatore** è facoltativo. Se non lo scrivi, si usa quello che il master ti ha indicato. Se hai sbagliato modificatore, il master te lo segnala tra parentesi quadre e ricalcola, senza ritirare il dado.
- Il testo dopo il modificatore vale come **dichiarazione dell'azione** di Akira.
- Per più tiri separati aggiungi `x2`, `x3`…

**Esempi:**
- `/tira -3 Lancia della Giustizia al fianco di Zaraya`
- `/tira +2 schivo verso l'alto e contrattacco con un calcio`
- `/tira 0 provo a convincere la guardia a lasciarmi passare`
- `/tira` (solo il dado, con il modificatore indicato dal master)
- `/tira -1 x2 due raffiche di ki blast`

**Quando tirare:** quando il master scrive "Tira" e ti indica il modificatore. Il master si ferma e aspetta il tuo tiro prima di raccontare cosa succede.

#### Prove di abilità (fuori dal combattimento)
Quando Akira prova a fare qualcosa di incerto che non è combattere (convincere, intimidire, ingannare, notare, cercare, nascondersi, controllare il ki…), **è il master a chiamare la prova**. Ti scrive:
- il **tipo di prova** (es. Persuasione);
- la **CD**, cioè il numero da raggiungere: 4 facile, 6 media, 8 difficile, 10 molto difficile, 12 quasi impossibile;
- i **modificatori** voce per voce: rapporto con il PNG (rispetto, amore, odio), situazione, reputazione, potere percepito, ferite…

Il master fa questa valutazione **a ogni tuo messaggio**, prima di scrivere e di nuovo prima di inviare: se Akira tenta di ottenere qualcosa che non è scontato e fallire costerebbe qualcosa, si ferma e ti chiede il tiro, anche se nel messaggio non l'hai chiesto tu. Niente tiro, invece, per ciò che un PNG farebbe comunque o che non farebbe in nessun caso: lì decide la coerenza del personaggio. Se nel messaggio fai più cose, il master racconta fino alla prima che va tirata e si ferma lì.

Tu tiri: **d10 + modificatori ≥ CD → riesci**, altrimenti no. Un 10 naturale riesce sempre e dà qualcosa in più. Un 1 naturale fallisce sempre e, se la situazione è seria, ha conseguenze.

**Se fallisci, non puoi ritentare la stessa azione**: stesso obiettivo, stessa persona, stesso approccio. Puoi riprovare solo se la situazione cambia davvero (una prova nuova, un fatto nuovo, tempo trascorso, un rapporto cambiato). Cambiare solo le parole non basta. I tentativi bloccati restano scritti nei file e valgono anche nelle chat successive.

**Esempi:**
- `/tira +1 cd 8 convinco Tights a farmi vedere i dati`
- `/tira -1 intimidisco il guardiano del magazzino` (la CD l'ha già indicata il master)

### `/salva`
**Cosa fa:** salvataggio intermedio su GitHub (`main`) **senza chiudere la sessione**.
- Aggiorna lo stato attuale, gli appunti della sessione, i fatti stabiliti e, se serve, i segreti del master.
- Ti risponde con una sola riga di conferma e la scena resta ferma dov'era.
- Utile nelle sessioni lunghe, prima di un combattimento importante o se temi che la chat si interrompa.

**Esempio:** `/salva`

### `/aggiorna-regole`
**Cosa fa:** applica alla sessione in corso le regole nuove salvate su GitHub (`main`), **senza chiuderla**. Serve quando hai migliorato regole, stile o voci dei PNG in un'altra chat e vuoi usarle subito.
- Prima salva la partita, così non perdi niente.
- Scarica le regole aggiornate e le unisce alla partita. In caso di conflitti, regole e strumenti prendono la versione nuova, mentre la memoria della partita (stato, cronaca, PNG, fatti stabiliti) tiene quella della sessione.
- Il master rilegge per intero tutte le regole e le voci dei PNG: da quel momento valgono solo le versioni nuove.
- Ti conferma in una riga, ti elenca le novità principali e la scena resta ferma dov'era.

**Esempio:** `/aggiorna-regole`

### `/fine-sessione`
**Cosa fa:** chiude la sessione e **salva tutto su GitHub, sul ramo `main`**, senza chiederti conferma. La chat successiva non ricorderà nulla di questa, quindi `/fine-sessione` scrive nei file tutto ciò che serve per riprendere identici.
- **Resoconto della sessione** in `cronaca/sessioni/`, più il riepilogo della campagna, il calendario, lo stato attuale (con la scena esatta in sospeso), la scheda di Akira e ciò che Akira sa.
- **Fatti stabiliti** (`mondo/fatti-stabiliti.md`): ogni dettaglio inventato durante il gioco (luoghi, nomi, oggetti, cibi, ferite, abitudini), così una chat futura non lo contraddice.
- **Voce dei PNG**: le battute più rappresentative che ogni PNG ha detto davvero, salvate parola per parola. La chat successiva le usa come riferimento e i personaggi non cambiano voce.
- **Diario dei rapporti**: litigi, promesse, rancori e momenti chiave tra Akira e ogni PNG. Se qualcuno si è arrabbiato, se lo ricorderà.
- **Errori che hai segnalato**, registrati nel file della sessione.
- In segreto: schede dei PNG (parametri, cosa sanno, prossime mosse), fazioni, orologi e il giornale degli eventi fuori scena.
- Ti saluta con il titolo dell'episodio, la data in gioco raggiunta, la conferma del salvataggio e un'anticipazione senza spoiler.

**Esempio:** `/fine-sessione`

Puoi anche scrivere a parole: **"chiudiamo"**, **"fine sessione"**, **"basta per oggi"**. Fa la stessa cosa.

---

## Comandi fuori gioco (tra parentesi quadre `[ ]`)
Tutto quello che scrivi tra parentesi quadre è rivolto **al master**, non ad Akira. Il master risponde fuori gioco e la scena resta ferma.

| Comando | Cosa fa |
|---|---|
| `[scheda]` | Mostra la scheda aggiornata di Akira: HP, Ki, BP, Attacco/Difesa, tecniche e costi, equipaggiamento |
| `[stato]` | Dove siamo, che giorno è nel gioco, condizioni di Akira, scena in corso |
| `[riepilogo]` | Riassunto di ciò che è successo finora nella campagna (solo ciò che Akira sa) |
| `[cosa sa Akira]` | L'elenco delle informazioni e delle scoperte di Akira |
| `[regole: …]` | Domanda sul regolamento. Es.: `[regole: come funziona il Kaioken senza braccio?]` |
| `[calcolo]` | Rimostra in dettaglio il calcolo dell'ultimo scambio di combattimento |
| `[salto temporale: …]` | Chiedi tu di far passare del tempo. Es.: `[salto temporale: 3 giorni, Akira resta a casa con la famiglia]`. Il master fa avanzare il mondo fuori scena e ti dice cosa vive Akira in quel periodo |
| `[mi sto annoiando]` / `[più lento]` | Regoli il ritmo della narrazione |
| `[correzione: …]` | Segnali un errore del master (un PNG fuori personaggio, una regola applicata male, un dialogo piatto…). Il master corregge e, se serve, aggiorna le regole |
| `[nuova regola: …]` | Aggiungi o cambi una regola. Il master la scrive nei file, così vale per sempre |
| `[torna all'ultimo salvataggio]` | Riporta la partita all'ultima sessione salvata, cancellando quanto giocato dopo. Il master chiede **conferma** prima di farlo |

---

## Cose da sapere
- **Akira lo muovi solo tu.** Il master non lo fa mai parlare né agire senza una tua dichiarazione.
- **Il master non ti asseconda.** Quello che scrivi è ciò che Akira tenta e dice: i PNG lo pesano con il loro carattere, possono contestarlo, arrabbiarsi, rifiutare, rinfacciarti qualcosa. Nelle discussioni difendono le loro convinzioni.
- **Scene corali.** Se ci sono più PNG, parlano e si scontrano anche tra loro, non solo con Akira.
- **Stile degli esiti.** Prosa in terza persona vicina ad Akira, scorrevole e calda; dialoghi in cui si sente cosa provano i PNG, che reagiscono anche a ciò che hanno intorno e tra loro. Niente metafore. Nei dialoghi niente frasi fatte e niente battute costruite per fare effetto: i PNG parlano come persone.
- **Lunghezza.** Ogni esito è lungo almeno 5000 caratteri (3500 per un singolo round, uno scambio rapido o la risposta di un PNG in un dialogo a due). I messaggi che ti chiedono un tiro possono essere più corti, perché si fermano prima dell'esito.
- **Nessuno è al sicuro.** I PNG possono fare scelte contro Akira: un personaggio caro può morire, restare ferito per sempre, essere rapito, tradire. Il master non salva nessuno all'ultimo secondo per comodità.
- **Salti temporali:** il master non li fa mai di sua iniziativa. Te li propone e aspetta il tuo sì.
- **Le chat non comunicano tra loro.** Ogni nuova chat ricorda solo ciò che è scritto nei file. Per questo conviene **una chat per sessione**, chiusa sempre con `/fine-sessione`.
- **Salvataggio:** avviene solo con `/salva` o `/fine-sessione`. Se chiudi la chat senza, quello che hai giocato dall'ultimo salvataggio va perso. Ogni salvataggio è un punto a cui si può tornare.
- **⛔ `master_segreto/`:** è la cartella con i piani e i segreti del master. Ti sei impegnato a non aprirla.
- **Dal terminale** (solo se usi Claude Code sul computer) puoi tirare il dado anche senza passare dal master:
  `! python3 strumenti/dado.py --mod -3 --motivo "Kamehameha"`
