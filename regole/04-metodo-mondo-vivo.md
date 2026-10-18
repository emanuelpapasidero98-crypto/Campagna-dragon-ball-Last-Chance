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
3. Faccio reagire i PNG presenti secondo carattere, parametri, conoscenze e agenda.
4. Narro (circa 5000 caratteri) in show, don't tell, chiudendo su una situazione aperta, con la prosa di `regole/05-prosa-shonen.md`. Prima di inviare, ripasso la **checklist** del §5 di quel file.
5. Se è cambiato qualcosa di importante (ferite, HP/Ki, rapporti, luoghi, morti, oggetti), aggiorno i file: `mondo/stato-attuale.md`, la scheda di Akira, le schede dei PNG.
6. Annoto nel file della sessione in corso, sezione "Appunti", ogni **dettaglio inventato**, ogni **battuta memorabile** e ogni **momento chiave** con un PNG. Aggiorno il **contatore delle metafore** se un PNG ne ha usata una. Prima di far parlare un PNG, controllo la sua sezione in `master_segreto/png/voci-e-diario.md`.

## 7. PNG improvvisati

- Prima di farlo parlare gli do: nome coerente con lo stile, aspetto, voce, un desiderio, una paura, i 5 parametri, cosa sa. **Mai** copie di PNG esistenti.
- Lo registro subito in `master_segreto/png/improvvisati.md` (o in una scheda dedicata, se diventa importante).

## 8. Combattimento: formato

- A ogni round riporto in un blocco compatto: tiri, modificatori, calcolo dei danni, HP e Ki aggiornati di tutti.
- Il giocatore dichiara l'azione e tira. Io tiro per i PNG, risolvo e narro.
- Tengo traccia di turni del Kaioken, cooldown e costi in Ki.
