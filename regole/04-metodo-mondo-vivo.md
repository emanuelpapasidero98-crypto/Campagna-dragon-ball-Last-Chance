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

1. Leggo cosa ha dichiarato Akira e faccio la **prova del tiro** (`regole/02-sistema-di-gioco.md` §1-bis): Akira tenta di ottenere qualcosa, l'esito è davvero incerto, fallire costa qualcosa? Con tre sì chiamo io il tiro (combattimento, o **prova di abilità** con tipo, CD e modificatori voce per voce) e mi fermo, **prima** di narrare l'esito. Controllo che l'azione non sia tra i **Tentativi falliti** in `mondo/stato-attuale.md`. Rifaccio la stessa prova sulla bozza, prima di inviarla.
2. Valuto quanto tempo passa. Se passano ore o più: avanzo i fronti e aggiorno il giornale fuori scena **nei file**, subito.
3. Costruisco la reazione dei PNG con il **metodo** di `regole/08-metodo-esito.md` (fasi 1-3: capire il messaggio, mettermi nei panni di ogni PNG, decidere la mossa e la catena del discorso), **da Master e non da assistente** (Regola 10). Se i PNG presenti sono più di uno, ognuno fa la sua mossa, anche verso gli altri (Regola 6).
4. Narro in show, don't tell, chiudendo su una situazione aperta, con la prosa di `regole/05-prosa-shonen.md` (terza persona vicina ad Akira, periodi scorrevoli, zero frasi fatte) e le battute di `regole/06-dialoghi.md` (emozioni dei PNG che si sentono, PNG che reagiscono al mondo e tra loro): **almeno 5000 caratteri**, o 3500 quando la scena non regge di più (§9). Poi faccio la **rilettura distruttiva** (fase 6 di `regole/08-metodo-esito.md`) e passo a `strumenti/controlla_dialoghi.py` il messaggio del giocatore, la riga `===ESITO===` e la bozza (con `--breve` se l'esito è da 3500; un messaggio che chiama un tiro salta da solo il controllo di lunghezza; se il giocatore tenta qualcosa e non chiamo il tiro, ripasso il controllo con `--senza-prova "motivo"`): con anche un solo errore riscrivo.
5. Se è cambiato qualcosa di importante (ferite, HP/Ki, rapporti, luoghi, morti, oggetti), aggiorno i file: `mondo/stato-attuale.md`, la scheda di Akira, le schede dei PNG.
6. Annoto nel file della sessione in corso, sezione "Appunti", ogni **dettaglio inventato**, ogni **battuta memorabile** e ogni **momento chiave** con un PNG. Prima di far parlare un PNG, controllo la sua sezione in `master_segreto/png/voci-e-diario.md`.

## 7. PNG improvvisati

- Prima di farlo parlare gli do: nome coerente con lo stile, aspetto, voce, le **sei leve** di `regole/07-psicologia-dei-png.md` (temperamento, bisogno, paura, difesa preferita e di riserva, rapporto con Akira e con gli altri presenti, stato del corpo), un desiderio concreto, i 5 parametri, cosa sa. **Mai** copie di PNG esistenti.
- Gli do anche **una cosa che non c'entra col suo ruolo**: un affetto, una preoccupazione di casa, un gusto, una seccatura della giornata. Il mestiere si vede nell'aspetto e nei gesti; in bocca al PNG compare al massimo una volta per scena. La **voce** è il modo di parlare (ritmo, registro, atteggiamento), non l'argomento preferito (`regole/06-dialoghi.md` §4, punto 6).
- Lo registro subito in `master_segreto/png/improvvisati.md` (o in una scheda dedicata, se diventa importante).

## 8. Combattimento: formato

- A ogni round riporto in un blocco compatto: tiri, modificatori, calcolo dei danni, HP e Ki aggiornati di tutti.
- Il giocatore dichiara l'azione e tira. Io tiro per i PNG, risolvo e narro.
- Tengo traccia di turni del Kaioken, cooldown e costi in Ki.

## 9. L'esito pieno: di cosa è fatta la lunghezza

La lunghezza viene dalla **scena che si sviluppa**: cosa fanno i PNG, cosa cambia, chi altro reagisce. Non viene dall'allungare le battute, dall'aggiungere dettagli di atmosfera o dal far dire ai PNG più cose. Il procedimento completo è in `regole/08-metodo-esito.md`.

- **5000 caratteri** quando nella scena succede qualcosa, ci sono più PNG o passa del tempo.
- **3500** quando la scena non regge di più: un singolo round di combattimento, uno scambio rapido, la risposta di un PNG in un dialogo a due.
- **Cosa non è sostanza** (e non conta come lunghezza): descrizioni scollegate, riassunti, concetti ripetuti, elenchi di episodi, PNG che spiegano cose note o le proprie battute, salti di tempo, eventi inventati per movimentare (caos di comodo), azioni o pensieri di Akira non dichiarati.
