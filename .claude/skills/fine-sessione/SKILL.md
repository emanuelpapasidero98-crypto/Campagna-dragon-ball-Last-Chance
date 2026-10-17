---
name: fine-sessione
description: Chiude la sessione di gioco, aggiorna tutta la memoria della campagna (cronaca, stato, schede, fronti segreti) e salva su GitHub. Da usare quando il giocatore dice che vuole terminare o chiudere la sessione.
---

# /fine-sessione

Il giocatore ha già dato il permesso permanente di salvare su GitHub: **non chiedere conferma**.

## 1. Aggiorna la memoria
- `cronaca/sessioni/sessione-NNN.md`: resoconto dettagliato della sessione **dal punto di vista di Akira** (cosa ha fatto, detto e scoperto; combattimenti con l'esito; PNG incontrati; decisioni). Data in gioco di inizio e di fine.
- `cronaca/riepilogo-campagna.md`: aggiungi un paragrafo di sintesi della sessione.
- `mondo/stato-attuale.md`: data, luogo, scena in sospeso (esattamente dove si è interrotto), condizioni di Akira, fili aperti noti al giocatore.
- `mondo/calendario.md`: aggiungi le righe dei giorni trascorsi.
- `personaggi/akira.md`: HP, Ki, ferite, oggetti, crescita (con il motivo).
- `personaggi/conoscenze-di-akira.md`: nuove scoperte.
- `master_segreto/png/*`: parametri cambiati, stato, cosa sanno ora, prossimo passo. I nuovi PNG improvvisati vanno in `improvvisati.md` o in una scheda propria.
- `master_segreto/fronti.md`: avanzamenti degli orologi e relativo registro.
- `master_segreto/giornale-fuori-scena.md`: tutto ciò che è successo altrove durante il tempo trascorso, compresi i salti temporali.
- Se il giocatore ha dato nuove indicazioni su regole o stile, aggiornale in `regole/`.

## 2. Salva su GitHub (il giocatore ha autorizzato in modo permanente il salvataggio su `main`)
```
git add -A
git commit -m "Sessione NNN: <titolo breve dell'episodio>"
git push -u origin <ramo corrente>
git fetch origin main
git checkout main && git merge --ff-only origin/main
git merge <ramo corrente> --no-edit
git push origin main
git checkout <ramo corrente>
```
- Se il ramo corrente è già `main`, basta `git pull origin main` prima del commit e poi `git push origin main`.
- In caso di conflitto nel merge, vince la versione della sessione appena giocata per i file di memoria (`mondo/`, `personaggi/`, `cronaca/`, `master_segreto/`). Avvisa il giocatore.
- Se il push fallisce per un problema di rete, riprova fino a 4 volte (attese di 2, 4, 8 e 16 s).

## 3. Saluta il giocatore
Breve messaggio fuori gioco:
- titolo dell'episodio;
- data in gioco raggiunta;
- conferma del salvataggio (commit e ramo);
- un'anticipazione in stile anime ("Nel prossimo episodio…") **vaga e senza spoiler**: solo ciò che Akira potrebbe intuire.
