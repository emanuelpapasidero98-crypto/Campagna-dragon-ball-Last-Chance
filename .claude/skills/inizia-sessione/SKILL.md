---
name: inizia-sessione
description: Apre una nuova sessione di gioco della campagna Dragon Ball Last Chance. Recupera la memoria dai file e riprende la scena. Da usare quando il giocatore vuole iniziare o riprendere a giocare.
---

# /inizia-sessione

1. **Sincronizza**: `git pull` sul ramo corrente. Se esiste `origin/main` più aggiornato, portalo dentro con un merge.
2. **Rileggi la memoria**, nell'ordine:
   - `CLAUDE.md` e **tutte** le regole, per intero: `regole/01-regole-master.md`, `regole/02-sistema-di-gioco.md`, `regole/03-stile-toriyama.md`, `regole/04-metodo-mondo-vivo.md`, **`regole/05-prosa-shonen.md`** (con i 6 esempi: la prosa della sessione deve suonare così), **`regole/06-dialoghi.md`** (principi, prima/dopo, checklist dei dialoghi), **`regole/07-dialoghi-shonen.md`** (forma shonen, modelli, controllo automatico) e `Comandi chat.md`;
   - `mondo/stato-attuale.md`, `mondo/calendario.md`;
   - `cronaca/riepilogo-campagna.md` e l'ultimo file in `cronaca/sessioni/`;
   - `mondo/fatti-stabiliti.md`;
   - `master_segreto/fronti.md`, `master_segreto/giornale-fuori-scena.md` (le ultime voci), `master_segreto/verita-del-mondo.md`;
   - `master_segreto/png/voci-e-diario.md` (sezioni dei PNG presenti o probabili) e `master_segreto/png/rapporti-tra-png.md` (come si trattano tra loro);
   - le schede in `master_segreto/png/` dei PNG presenti nella scena da riprendere.
3. **Verifica la coerenza**: se dall'ultima sessione erano previsti avanzamenti fuori scena non ancora annotati, annotali ora nei file segreti.
4. **Determina il numero di sessione** (l'ultimo in `cronaca/sessioni/` + 1) e crea `cronaca/sessioni/sessione-NNN.md` con questo modello:
   ```
   # Sessione NNN — <titolo, da decidere a fine sessione>
   - Data reale: AAAA-MM-GG · Data in gioco: inizio … / fine …
   - Luogo iniziale: …

   ## Resoconto
   (da scrivere a fine sessione, dal punto di vista di Akira)

   ## Appunti in corso di sessione
   ### Fatti stabiliti (dettagli inventati)
   ### Battute memorabili dei PNG
   ### Momenti chiave nei rapporti

   ## Contatore metafore (massimo 1 per PNG a sessione)
   | PNG | Metafore usate |
   |---|---|

   ## Errori segnalati dal giocatore
   ```
   Durante la sessione aggiorna gli **appunti** e il **contatore** man mano: protegge la memoria se la chat viene riassunta in automatico.
5. **Presenta al giocatore**:
   - un breve **"Nelle puntate precedenti"** in stile anime, solo con ciò che **Akira sa**, mai i segreti;
   - lo stato di Akira (HP, Ki, condizioni rilevanti);
   - poi **riprendi la scena** da dove era rimasta, in narrazione (**almeno 5000 caratteri**, verificati con `strumenti/controlla_dialoghi.py`). Chiudi su una situazione aperta, senza far agire Akira.
   - Da qui in avanti sei **il Master, non un assistente** (Regola 10): i PNG non assecondano il giocatore, lottano per le loro convinzioni e interagiscono anche tra loro. Non c'è un periodo di rodaggio: vale dal primo messaggio.
6. Se è la **prima sessione** della campagna, parti dall'incipit in `archivio/incipit-campagna-babidi.md`: Akira è a cena con la famiglia nella foresta di Nova City. Inizia con calma (consiglio del giocatore: non buttarlo subito nella mischia).
