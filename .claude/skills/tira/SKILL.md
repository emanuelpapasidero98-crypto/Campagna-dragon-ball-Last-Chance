---
name: tira
description: Il giocatore tira 1d10 per Akira (combattimento o prova di abilità con CD), con modificatore e azione. Uso - /tira [modificatore] [cd N] [azione]. Esempio - /tira -3 Lancia della Giustizia al fianco di Zaraya
disable-model-invocation: true
---

# /tira — il giocatore tira il dado

Il giocatore ha chiesto di tirare. Argomenti: `$ARGUMENTS`

1. Estrai dagli argomenti:
   - il **modificatore**: il primo numero con o senza segno (es. `-3`, `+2`, `2`). Se manca, usa quello indicato dal master nell'ultimo messaggio; se non c'era, usa 0;
   - la **CD**, se il master ha chiamato una **prova di abilità**: dagli argomenti (`cd 8`, `CD8`) oppure dall'ultimo messaggio del master;
   - il **motivo**: il resto del testo (l'azione dichiarata);
   - se c'è `x2`, `x3`… usa `--n` per più tiri separati.
2. Esegui **esattamente** questo comando, una sola volta, senza scartare risultati:
   - combattimento: `python3 strumenti/dado.py --chi Akira --mod <MOD> --motivo "<MOTIVO>"`
   - prova di abilità: `python3 strumenti/dado.py --chi Akira --mod <MOD> --cd <CD> --motivo "<TIPO DI PROVA>: <MOTIVO>"`
3. Riporta il risultato **parola per parola** in cima alla risposta.
4. Se il modificatore o la CD usati dal giocatore sono diversi da quelli corretti, segnalalo in `[OOC]` e ricalcola l'esito con i valori giusti. Il dado naturale resta quello tirato.
5. Poi, da master:
   - **combattimento**: tira i dadi dei PNG coinvolti (con lo script), risolvi con `regole/02-sistema-di-gioco.md` mostrando il calcolo in un blocco compatto, e narra;
   - **prova di abilità**: narra l'esito in base a superata/fallita e ai critici (`regole/02-sistema-di-gioco.md` §1-bis). Se è fallita, aggiungi il tentativo a **Tentativi falliti** in `mondo/stato-attuale.md`, con cosa servirebbe per riprovare.
   - L'azione nel motivo vale come dichiarazione di Akira, ma **non aggiungere** parole o azioni che il giocatore non ha dichiarato.
