---
name: fine-sessione
description: Chiude la sessione di gioco, aggiorna tutta la memoria della campagna (cronaca, stato, schede, voci dei PNG, diario dei rapporti, fatti stabiliti, fronti segreti) e salva su GitHub (main). Da usare quando il giocatore dice che vuole terminare o chiudere la sessione.
---

# /fine-sessione

Il giocatore ha dato il permesso permanente di salvare su GitHub, ramo `main`: **non chiedere conferma**.

Obiettivo: la prossima chat, che non ricorderà nulla di questa, deve poter riprendere **identica**: stessi PNG con la stessa voce, stessi dettagli, stesse conseguenze. Nel dubbio se scrivere una cosa, scrivila.

## 1. Cronaca e stato (pubblici)
- **`cronaca/sessioni/sessione-NNN.md`**: resoconto dettagliato **dal punto di vista di Akira**: cosa ha fatto, detto e scoperto; combattimenti con esito e tiri chiave; PNG incontrati; decisioni prese; data in gioco di inizio e di fine. Completa il **contatore delle metafore** e la sezione "Errori segnalati dal giocatore".
- **`cronaca/riepilogo-campagna.md`**: un paragrafo di sintesi della sessione.
- **`mondo/stato-attuale.md`**: data, luogo, scena in sospeso (esattamente dove si è interrotta, compresa l'ultima cosa detta o fatta), condizioni di Akira, fili aperti noti al giocatore, **Tentativi falliti** (aggiungi quelli nuovi e togli quelli sbloccati da un cambiamento reale della situazione).
- **`mondo/calendario.md`**: una riga per ogni giorno trascorso.
- **`mondo/fatti-stabiliti.md`**: **ogni dettaglio inventato** in questa sessione (luoghi, nomi, oggetti, cibi, animali, ferite, abitudini, frasi rituali, aspetto di PNG minori). Prendili dagli appunti del file di sessione e rileggi la chat per non perderne nessuno.
- **`personaggi/akira.md`**: HP, Ki, ferite, oggetti, crescita (con il motivo).
- **`personaggi/conoscenze-di-akira.md`**: nuove scoperte, con data e modo.

## 2. Memoria segreta del master
- **`master_segreto/png/voci-e-diario.md`**, per ogni PNG che è comparso:
  - **Battute dette in gioco**: 1-3 battute vere della sessione che rappresentano bene la sua voce. Prima di salvarle, passale a `strumenti/controlla_dialoghi.py`: se hanno errori (telegrammi, eco…) vanno riformulate e segnate come *riformulata*, perché il master le userà come modello. Scegli battute che mostrano il **modo** di parlare del PNG, non quelle costruite sul suo mestiere, sulla sua passione o sul suo tic (`regole/06-dialoghi.md`, principio 20);
  - **Diario dei rapporti**: momenti chiave con Akira (litigi, promesse, rancori, debiti, gesti, cose dette che pesano), con sessione e data in gioco;
  - se la voce si è evoluta (un PNG che si è indurito o aperto), aggiorna anche gli esempi di **Voce** e **Non direbbe mai**;
  - i PNG nuovi entrano qui con la loro sezione completa.
- **`master_segreto/png/*.md`** (schede): parametri cambiati (con il motivo), stato fisico, posizione, **cosa sa ora**, prossimo passo. I PNG improvvisati vanno in `improvvisati.md` o in una scheda propria.
- **`master_segreto/fronti.md`**: avanzamenti degli orologi e relativo registro.
- **`master_segreto/giornale-fuori-scena.md`**: tutto ciò che è successo altrove nel tempo trascorso, compresi i salti temporali, con "come Akira può scoprirlo".
- Se il giocatore ha dato nuove indicazioni su regole o stile (`[correzione]`, `[nuova regola]`), verifica che siano scritte in `regole/`.

## 3. Salvataggio su GitHub (main)
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
- Se il ramo corrente è già `main`: `git pull origin main` prima del commit, poi `git push origin main`.
- In caso di conflitto nel merge, per i file di memoria (`mondo/`, `personaggi/`, `cronaca/`, `master_segreto/`) vince la versione della sessione appena giocata. Avvisa il giocatore.
- Se il push fallisce per un problema di rete, riprova fino a 4 volte (attese di 2, 4, 8 e 16 s). Se fallisce per un problema di permessi, dillo chiaramente al giocatore.

## 4. Saluto al giocatore (fuori gioco, breve)
- Titolo dell'episodio e data in gioco raggiunta.
- Conferma del salvataggio (commit e `main`).
- "Nel prossimo episodio…": un'anticipazione **vaga e senza spoiler**, solo con ciò che Akira potrebbe intuire.
