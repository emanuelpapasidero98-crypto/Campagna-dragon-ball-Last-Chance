---
name: salva
description: Salvataggio intermedio della partita su GitHub (main) senza chiudere la sessione. Da usare quando il giocatore vuole salvare a metà sessione.
---

# /salva — salvataggio rapido

Il giocatore ha autorizzato in modo permanente il salvataggio su `main`: **non chiedere conferma**.

1. Aggiorna rapidamente:
   - `mondo/stato-attuale.md` (dove, quando, scena in sospeso, condizioni di Akira);
   - il file della sessione in corso in `cronaca/sessioni/` (appunti fino a questo punto);
   - `mondo/fatti-stabiliti.md` (dettagli inventati finora);
   - `master_segreto/fronti.md` e `master_segreto/giornale-fuori-scena.md`, se è passato tempo;
   - `master_segreto/png/voci-e-diario.md`, se ci sono stati momenti chiave con un PNG.
2. Salva:
   ```
   git add -A
   git commit -m "Sessione NNN: salvataggio intermedio"
   git push -u origin <ramo corrente>
   git fetch origin main && git checkout main && git merge --ff-only origin/main && git merge <ramo corrente> --no-edit && git push origin main && git checkout <ramo corrente>
   ```
   Se il ramo corrente è `main`: `git pull origin main`, commit, `git push origin main`.
3. Rispondi con **una riga** fuori gioco ("[Salvato su main · giorno X in gioco]"). Poi la scena **resta ferma** dov'era, in attesa della prossima azione di Akira.
