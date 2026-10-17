---
name: inizia-sessione
description: Apre una nuova sessione di gioco della campagna Dragon Ball Last Chance. Recupera la memoria dai file e riprende la scena. Da usare quando il giocatore vuole iniziare o riprendere a giocare.
---

# /inizia-sessione

1. **Sincronizza**: `git pull` sul ramo corrente. Se esiste `origin/main` più aggiornato, portalo dentro con un merge.
2. **Rileggi la memoria**, nell'ordine:
   - `CLAUDE.md` (con le regole importate);
   - `mondo/stato-attuale.md`, `mondo/calendario.md`;
   - `cronaca/riepilogo-campagna.md` e l'ultimo file in `cronaca/sessioni/`;
   - `master_segreto/fronti.md`, `master_segreto/giornale-fuori-scena.md` (le ultime voci), `master_segreto/verita-del-mondo.md`;
   - le schede in `master_segreto/png/` dei PNG presenti nella scena da riprendere.
3. **Verifica la coerenza**: se dall'ultima sessione erano previsti avanzamenti fuori scena non ancora annotati, annotali ora nei file segreti.
4. **Determina il numero di sessione** (l'ultimo in `cronaca/sessioni/` + 1) e crea `cronaca/sessioni/sessione-NNN.md` con data reale, data in gioco iniziale e luogo.
5. **Presenta al giocatore**:
   - un breve **"Nelle puntate precedenti"** in stile anime, solo con ciò che **Akira sa**, mai i segreti;
   - lo stato di Akira (HP, Ki, condizioni rilevanti);
   - poi **riprendi la scena** da dove era rimasta, in narrazione (circa 5000 caratteri). Chiudi su una situazione aperta, senza far agire Akira.
6. Se è la **prima sessione** della campagna, parti dall'incipit in `archivio/incipit-campagna-babidi.md`: Akira è a cena con la famiglia nella foresta di Nova City. Inizia con calma (consiglio del giocatore: non buttarlo subito nella mischia).
