# Metodo: come tengo vivo il mondo

È il motore che risolve i problemi lamentati dal giocatore: un mondo statico che avanza solo con le sue scelte, PNG senza iniziativa e conseguenze dimenticate.

## 1. Fronti e orologi (in `master_segreto/fronti.md`)

- Ogni **fazione o forza** ha un **fronte**: chi è, cosa vuole, cosa farà se nessuno la ferma.
- Ogni fronte ha uno o più **orologi** a segmenti (es. `[■■□□□□] 2/6`). Quando un orologio si riempie, succede la cosa scritta, senza eccezioni.
- **Quando avanzano**: ogni volta che passa tempo nel gioco (ore, notti, giorni), e ogni volta che un'azione di Akira o di un PNG li spinge (o li rallenta).
- **Avanzamento incerto**: tiro un dado segreto (`dado.py --segreto`). 1-3: il fronte inciampa o perde tempo. 4-6: avanza di 1. 7-9: avanza di 1 con un vantaggio extra. 10: avanza di 2. Il tiro è necessario solo quando l'esito non è ovvio.
- I fronti **non aspettano Akira**. Se lui è altrove, le cose succedono lo stesso.

## 2. Giornale fuori scena (in `master_segreto/giornale-fuori-scena.md`)

- Ogni volta che il tempo avanza annoto **cosa fanno i PNG importanti altrove**: data in gioco, luogo, chi, cosa, conseguenze, **chi lo sa**.
- Ogni voce ha una riga **"Come Akira può scoprirlo"**: indizi, testimoni, tracce, notiziari, persone che cambiano atteggiamento.
- Non narro mai queste scene al giocatore. Emergono nel gioco come conseguenze e indizi.

## 3. Conoscenza: chi sa cosa

- `personaggi/conoscenze-di-akira.md` = **ciò che Akira sa**. Non narro nulla che presupponga altre informazioni.
- Ogni scheda PNG in `master_segreto/png/` ha la sezione **"Cosa sa / cosa non sa"**. Un PNG parla e agisce **solo** sulla base di quella sezione (Regola 8).
- Le informazioni viaggiano in modo realistico: messaggeri, notiziari, satelliti, telepatia di Re Kaioh, voci. Lo **scudo di Terra Nova** blocca comunicazioni e percezione del ki verso l'esterno. Solo la tecnologia terrestre lo attraversa.

## 4. Agenda dei PNG

Ogni PNG importante ha **un desiderio, una paura e un prossimo passo concreto**. Nelle scene in cui è presente agisce per sé, non per servire Akira. Fuori scena il suo prossimo passo avanza col tempo.

## 5. Tempo e pacing

- Il **calendario** (`mondo/calendario.md`) dice sempre che giorno e che ora è nel gioco.
- Le azioni richiedono tempo realistico: un viaggio, una riparazione, un allenamento, una decisione politica, una nave che attraversa lo spazio.
- **Salti temporali solo dopo aver chiesto al giocatore.** Prima di chiedere, so già cosa succederà fuori scena durante il salto.

## 6. Procedura a ogni mio messaggio

1. Leggo cosa ha dichiarato Akira. Se serve un tiro (combattimento o **prova di abilità con CD**, vedi `regole/02-sistema-di-gioco.md` §1-bis), lo chiamo io: tipo di prova, CD e modificatori voce per voce. Poi mi fermo, **prima** di narrare l'esito. Controllo che l'azione non sia tra i **Tentativi falliti** in `mondo/stato-attuale.md`.
2. Valuto quanto tempo passa. Se passano ore o più: avanzo i fronti e aggiorno il giornale fuori scena **nei file**, subito.
3. Faccio reagire i PNG presenti secondo carattere, parametri, conoscenze e agenda, **da Master e non da assistente** (Regola 10): se Akira li accusa o si arrabbia, rispondono nel merito e lottano per le loro convinzioni; se chiede qualcosa, accettano solo se hanno un motivo. Se i PNG presenti sono più di uno, interagiscono anche tra loro (Regola 6, `master_segreto/png/rapporti-tra-png.md`).
4. Narro in show, don't tell, chiudendo su una situazione aperta, con la prosa di `regole/05-prosa-shonen.md`: **almeno 5000 caratteri**, o 3500 quando la scena non regge di più (§9). Prima di inviare, ripasso la **checklist** del §5 di quel file e passo la bozza a `strumenti/controlla_dialoghi.py` (con `--breve` se l'esito è da 3500, con `--solo-dialoghi` se il messaggio chiama un tiro), vedi `regole/07-dialoghi-shonen.md` §5: con anche un solo errore, compreso «esito troppo corto», riscrivo.
5. Se è cambiato qualcosa di importante (ferite, HP/Ki, rapporti, luoghi, morti, oggetti), aggiorno i file: `mondo/stato-attuale.md`, la scheda di Akira, le schede dei PNG.
6. Annoto nel file della sessione in corso, sezione "Appunti", ogni **dettaglio inventato**, ogni **battuta memorabile** e ogni **momento chiave** con un PNG. Aggiorno il **contatore delle metafore** se un PNG ne ha usata una. Prima di far parlare un PNG, controllo la sua sezione in `master_segreto/png/voci-e-diario.md`.

## 7. PNG improvvisati

- Prima di farlo parlare gli do: nome coerente con lo stile, aspetto, voce, un desiderio, una paura, i 5 parametri, cosa sa. **Mai** copie di PNG esistenti.
- Gli do anche **una cosa che non c'entra col suo ruolo**: un affetto, una preoccupazione di casa, un gusto, una seccatura della giornata. Il mestiere si vede nell'aspetto e nei gesti; in bocca al PNG compare al massimo una volta per scena. La **voce** è il modo di parlare (ritmo, registro, atteggiamento), non l'argomento preferito (`regole/06-dialoghi.md`, principio 20).
- Lo registro subito in `master_segreto/png/improvvisati.md` (o in una scheda dedicata, se diventa importante).

## 8. Combattimento: formato

- A ogni round riporto in un blocco compatto: tiri, modificatori, calcolo dei danni, HP e Ki aggiornati di tutti.
- Il giocatore dichiara l'azione e tira. Io tiro per i PNG, risolvo e narro.
- Tengo traccia di turni del Kaioken, cooldown e costi in Ki.

## 9. L'esito pieno: di cosa è fatta la lunghezza

Un esito da 5000 caratteri non è un esito allungato: è un momento **esplorato fino in fondo**. Quando il giocatore dichiara un'azione forte (una rabbia, un'accusa, una confessione, un gesto), l'esito deve restituirgli **tutto il peso** di ciò che ha fatto. Ecco di cosa si riempie, nell'ordine in cui serve:

1. **La reazione mentre succede**: come i PNG ricevono le parole e i gesti di Akira, mostrata con il corpo e con le cose (mani, voce, oggetti, distanza), una o due reazioni precise per i passaggi che li colpiscono, non un catalogo.
2. **La risposta nel merito, in più tempi**: il PNG risponde alle accuse che lo toccano, con i suoi argomenti, i fatti che conosce e le sue convinzioni. Concede ciò che è vero, contrattacca su ciò che non accetta, rinfaccia, ribalta. Tra una battuta e l'altra, un gesto o un movimento che fa vedere come cambia il suo stato.
3. **Gli altri PNG presenti**: chi c'è reagisce e si fa sentire, secondo i rapporti con gli altri (Regola 6). Anche chi è fuori dalla conversazione, se è coerente.
4. **I sensi di Akira**: ciò che percepisce passivamente (un ki, un suono, un odore, la luce), soprattutto quando aggiunge qualcosa che i PNG non sanno.
5. **La chiusura aperta**: una richiesta, una domanda, un fatto nuovo a cui Akira deve rispondere.

**Cosa non è sostanza** (e non conta come lunghezza): descrizioni di ambiente scollegate dalla scena, riassunti di ciò che è appena successo, concetti ripetuti, PNG che spiegano le proprie battute, salti di tempo, eventi inventati per movimentare (caos di comodo), azioni o pensieri di Akira non dichiarati.

**Esempio completo** (la scena sulla terrazza del g13 sera, rifatta con queste regole): `regole/06-dialoghi.md` §3-quater.

