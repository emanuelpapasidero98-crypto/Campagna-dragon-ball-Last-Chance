---
name: tira
description: Il giocatore tira 1d10 per Akira, con modificatore e azione. Uso - /tira [modificatore] [azione]. Esempio - /tira -3 Lancia della Giustizia al fianco di Zaraya
disable-model-invocation: true
---

# /tira — il giocatore tira il dado

Il giocatore ha chiesto di tirare. Argomenti: `$ARGUMENTS`

1. Estrai dagli argomenti:
   - il **modificatore**: il primo numero con segno o senza (es. `-3`, `+2`, `2`). Se manca, usa quello che il master aveva indicato nell'ultimo messaggio. Se non c'era, usa 0;
   - il **motivo**: il resto del testo (l'azione dichiarata).
   - Se gli argomenti contengono `x2`, `x3` o simili, usa `--n` per più tiri separati.
2. Esegui **esattamente** questo comando, senza ripeterlo e senza scartare risultati:
   `python3 strumenti/dado.py --chi Akira --mod <MOD> --motivo "<MOTIVO>"`
3. Riporta il risultato **parola per parola** in cima alla risposta.
4. Se il modificatore che il giocatore ha usato è diverso da quello corretto secondo il sistema, segnalalo in `[OOC]` e ricalcola il totale con il modificatore giusto. Il dado naturale resta quello tirato.
5. Poi, da master: tira i dadi dei PNG coinvolti (con lo script), risolvi con il sistema (`regole/02-sistema-di-gioco.md`) mostrando il calcolo in un blocco compatto e narra l'esito, seguendo le regole del master. L'azione dichiarata nel motivo vale come dichiarazione di Akira, ma **non aggiungere** parole o azioni che il giocatore non ha dichiarato.
