---
name: aggiorna-regole
description: Scarica da GitHub (main) le regole, le guide di stile, gli strumenti e le voci dei PNG aggiornati e li applica alla sessione in corso, senza chiuderla e senza perdere la partita. Da usare quando il giocatore vuole usare le nuove modifiche a metà sessione.
---

# /aggiorna-regole — applica le nuove regole senza chiudere la sessione

Il giocatore ha migliorato le regole in un'altra chat e le vuole subito, **senza perdere niente della partita in corso**. Il permesso di salvare su GitHub è già stato dato: **non chiedere conferma**.

## 1. Metti al sicuro la partita
Prima di toccare qualsiasi cosa, salva **in locale** lo stato attuale della sessione, così niente va perso:
- aggiorna rapidamente `mondo/stato-attuale.md` (scena in sospeso, esattamente dove si è fermata) e gli appunti del file di sessione in `cronaca/sessioni/`;
- poi esegui:
```
git add -A
git commit -m "Sessione NNN: salvataggio prima dell'aggiornamento delle regole"
```
Se non c'è niente da salvare, il commit fallisce: va bene così, vai avanti.

## 2. Scarica e unisci gli aggiornamenti da main
```
git fetch origin main
git merge origin/main --no-edit
```
Se il ramo corrente è `main`, usa `git pull --no-rebase origin main`.

**Se ci sono conflitti**, risolvili file per file con questo criterio:
- **Vince `main`** (le versioni nuove) per: `regole/`, `strumenti/`, `.claude/`, `Comandi chat.md`, `README.md`, `CLAUDE.md`. Per questi file: `git checkout --theirs <file>`.
- **Vince la sessione** (la partita in corso) per: `mondo/`, `personaggi/`, `cronaca/` e tutto `master_segreto/` **tranne** `voci-e-diario.md`. Per questi file: `git checkout --ours <file>`.
- **`master_segreto/png/voci-e-diario.md` va unito a mano.** Le sezioni **Voce** e **Non direbbe mai** vengono da `main`; le sezioni **Battute dette in gioco** e **Diario dei rapporti** tengono tutto ciò che c'è nella sessione, più eventuali voci nuove di `main`.

Poi: `git add -A && git commit --no-edit`.

## 3. Rileggi tutto, per intero
Le regole caricate a inizio sessione sono la versione **vecchia**: vanno sostituite nella tua memoria. Rileggi con lo strumento di lettura, dall'inizio alla fine, **tutti** questi file. Da questo momento valgono solo queste versioni:
- `CLAUDE.md`
- `regole/01-regole-master.md`, `regole/02-sistema-di-gioco.md`, `regole/03-stile-toriyama.md`, `regole/04-metodo-mondo-vivo.md`
- `regole/05-prosa-shonen.md`, `regole/06-dialoghi.md`, `regole/07-psicologia-dei-png.md`, `regole/08-metodo-esito.md`, e ogni altro file nuovo comparso in `regole/` (se un file di regole è sparito da `main`, non vale più)
- `.claude/promemoria-master.md`
- `master_segreto/png/voci-e-diario.md` e `master_segreto/png/rapporti-tra-png.md`, se esiste
- `Comandi chat.md`

Se esistono strumenti nuovi in `strumenti/` (come `controlla_dialoghi.py`), da ora in poi vanno usati come indicano le regole.

## 4. Verifica
- Controlla che `git status` sia pulito e che il merge sia riuscito.
- Prova lo strumento di controllo, se esiste: `python3 strumenti/controlla_dialoghi.py --solo-dialoghi <<'EOF'` con una riga qualsiasi, poi `EOF`.

## 5. Rispondi al giocatore (fuori gioco, breve)
- Una riga di conferma: `[Regole aggiornate da main · partita salvata · scena ferma dove era]`.
- Un elenco di **massimo 5 punti** sulle novità **delle regole pubbliche** (stile, dialoghi, comandi). **Mai** citare il contenuto di `master_segreto/`.
- Se qualcosa non è andato a buon fine (conflitto non risolto, merge fallito), dillo chiaramente.
- **Non narrare niente di nuovo** e non far avanzare la scena: si riprende dalla prossima azione del giocatore, con le regole nuove.
