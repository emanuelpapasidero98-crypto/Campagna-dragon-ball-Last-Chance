# Dialoghi in stile shonen: struttura, confronto e modelli

Guida **vincolante**, che completa `regole/06-dialoghi.md`. Il giocatore vuole dialoghi che sembrino scritti da una persona, nello stile dei manga **shonen e battle shonen**, senza frasi spezzate dai punti, senza effetto eco e senza concetti ripetuti.

> I dialoghi dei manga sono protetti da copyright, quindi qui non sono copiati. Questa guida spiega **come sono costruiti** e mostra **modelli originali** scritti per questa campagna con le stesse tecniche.

---

## 1. Come parlano i personaggi degli shonen

Nei manga ogni **balloon è un respiro**. Le battute sono spesso brevi, ma quasi mai **piatte**: sono gridi, domande, sfide, interruzioni, risate. Le frasi corte e neutre chiuse dal punto, una dopo l'altra ("Di nuovo. Finché non smetti. Devo esserci."), negli shonen non esistono: è un vizio dei testi generati.

Quando un personaggio ha qualcosa da dire (la provocazione del rivale, lo sfogo prima della trasformazione, la spiegazione di una tecnica, la paternale di un maestro), la battuta si **allarga** e scorre. In prosa diventa **un periodo unico, legato da virgole**, non tre telegrammi.

| Tipo di battuta | Come è fatta | Forma in prosa |
|---|---|---|
| **Grido o tecnica** | Una parola o un nome, tutto il fiato in un colpo | «KAMEHAMEHAAA!» · «Akira!» |
| **Stupore** | Breve e carica, spesso interrotta | «Ma che…?!» · «Non può essere!» |
| **Provocazione del rivale** | Lunga, arrogante, con esclamativi e una domanda di sfida in fondo | un periodo scorrevole, con un "!" o un "?" che chiude |
| **Battibecco comico** (lo schema di Bulma e Goku, del Genio e Crilin) | Uno dice un'assurdità, l'altro ribatte con una frase sola, esasperata | due battute rapide, ognuna intera |
| **Momento emotivo** | La voce si spezza, ma con "…" e "—", non con il punto | frasi lunghe interrotte da pause |
| **Quotidiano** | Battute veloci, ci si interrompe, si cambia argomento | botta e risposta con gesti in mezzo |

Gli shonen hanno anche un **tono diretto**: i personaggi dicono chiaramente cosa **vogliono** ("adesso ti batto", "voglio vedere quanto vali"). Ciò che **provano**, invece, si vede da quello che fanno. Il pianto trattenuto, la risata che si spegne, il pugno che trema dicono più di qualsiasi spiegazione.

---

## 2. Regole di forma (misurabili)

1. **Una battuta breve è ammessa solo se è carica** (finisce con !, ?, …, — oppure è l'unica frase della battuta). Le frasi brevi e piatte chiuse dal punto non si mettono in fila.
2. **In una battuta**:
   - al massimo **una** frase sotto le 6 parole;
   - **mai due frasi brevi di fila chiuse dal punto**;
   - al massimo **tre punti fermi**.

   Il resto si lega con virgole, "e", "ma", "perché", "che", "così", "quindi", "mentre", "finché", oppure con "…" e "—".
3. **Eco e ripresa comica non sono la stessa cosa.**
   - **Eco (vietata):** confermare le parole dell'altro prima di rispondere ("Mangio, sì", "L'ho visto, sì", "Il pranzo sì, ci sto").
   - **Ripresa comica (ammessa, con misura):** prendere le parole dell'altro per ribaltarle in una battuta. Zemi: «Il limone lo mangio, se ci mettete lo zucchero!» Syntia: «Tu mangeresti anche lo sgabello, se ci mettessimo lo zucchero!»
4. **Nessun concetto due volte nella stessa scena.** Se un PNG ha già detto una cosa, non la ripete con altre parole, e nemmeno un altro PNG la ridice. Ogni battuta aggiunge un'informazione, un'emozione o una svolta nuova.
5. **Controllo automatico prima di inviare.** Ogni messaggio con dialoghi passa da `strumenti/controlla_dialoghi.py` (vedi §5). Con anche un solo errore (❌), si riscrive.

---

## 3. Confronto con i vecchi dialoghi

Tutte queste battute sono state scritte dal master o erano nelle guide. Sono state segnalate dal controllo automatico, e ognuna ha una versione corretta.

| Battuta vecchia | Errore | Versione nuova |
|---|---|---|
| «Ho fatto troppo riso. Di nuovo. Se avete fame è in cucina…» *(voce di Tobias)* | Telegramma | «Ho fatto troppo riso, di nuovo, quindi se avete fame è in cucina… e se lo lasciate lì me ne accorgo, eh.» |
| «La regina ha deciso. Io non devo essere d'accordo. Devo esserci.» *(voce di Ignis)* | Telegramma, tono da aforisma | «La regina ha deciso, e io non devo essere d'accordo, devo solo esserci.» |
| «Di nuovo. Finché non smetti di guardarmi come se potessi fermarmi.» *(voce di Zaraya)* | Telegramma e ripetizione | «Rialzati e rifallo, finché non smetti di guardarmi come se potessi fermarmi!» |
| «Mangio, sì.» … «Per il resto, sì, sono qui per te.» … «Glielo dico, stai tranquillo. Stasera lo scrivo nel rapporto, parola per parola.» | Eco a lista, frasi staccate | «Il riso me lo cucino da solo, perché quello della mensa del governatorato sa di colla, e se ti stai chiedendo anche se dormo, la risposta è sì, ma male, da quando mi hanno affidato questo incarico.» |
| «Fantastica, sì…» … «L'ho visto, sì.» … «Il pranzo sì, ci sto.» | Eco ripetuta tre volte | Il complimento si devia: «Ho detto "rami" due volte di fila davanti a tutta l'aula, e tu mi vieni a dire fantastica?» |
| «Vai, parlaci. Però parlate, eh, e basta. Oggi è andata bene, e voglio che resti così…» | Telegramma; "parlare" ripetuto | «Vai pure da lui, ma niente scenate, che oggi è andata bene e me la voglio godere almeno fino a stasera.» |
| «Ho detto "rami" due volte di fila. Due! Davanti a duecento persone.» *(riscrittura del master)* | Telegramma | «Ho detto "rami" due volte di fila davanti a duecento persone, due volte!» |
| «Il riso me lo faccio da solo. Quello della mensa del governatorato sa di colla.» *(riscrittura del master)* | Frasi staccate | «Il riso me lo faccio da solo, perché quello della mensa sa di colla.» |
| «Ha ricominciato a mangiare, quindi il riso si può. …Però guarda te, mica me. Lo conosci?» | Telegramma | «Ha ricominciato a mangiare, quindi il riso si può… però guarda te, mica me, papà, ma tu lo conosci?» |
| «Lascia perdere. Fai finta che non ho detto niente.» | Mezzo segreto e frasi staccate | Da evitare. Se serve, una volta per sessione: «Niente, lascia stare, non sono affari tuoi.» |
| «Dimmi dove sei stato. Davvero, stavolta.» *(esempio della guida)* | Telegramma | «Dimmi dove sei stato, e stavolta dimmelo davvero.» |
| «Nervosa? Macché.» *(esempio della guida)* | Eco della domanda e telegramma | Non risponde alla domanda: «Ho riscritto l'inizio sei volte, e stamattina la Cannella mi ha detto che ci saranno anche i giornalisti…» |

**Risultato del controllo**: sui vecchi dialoghi 22 errori su 20 battute; sui modelli qui sotto 0 errori su 23 battute.

---

## 4. Dialoghi modello

Sono illustrativi: **non** sono eventi della campagna e **non** si copiano parola per parola. Mostrano forma, ritmo e punteggiatura. Tra parentesi c'è ciò che il giocatore ha dichiarato, quando serve.

### A — Quotidiano comico (battibecco e ripresa comica)

> Il frigo dell'attico conteneva dodici lattine di caffè, un limone rinsecchito e nient'altro, e Syntia lo fissava a braccia incrociate da almeno un minuto, come se aspettasse che le chiedesse scusa.
>
> «Secondo te Tights pensa davvero che la gente normale faccia colazione col caffè freddo, o si aspetta che ci mangiamo pure il limone?»
>
> Zemi, ancora in pigiama sullo sgabello della cucina, alzò la mano come a scuola. «Io il limone lo mangio, se ci mettete sopra lo zucchero!»
>
> «Tu mangeresti anche lo sgabello, se ci mettessimo sopra lo zucchero.» Syntia chiuse lo sportello con un colpo d'anca e puntò il dito verso la finestra. «Giù all'angolo c'è un forno che fa i panini dolci col burro, l'ho visto ieri sera mentre salivamo, e chi scende per primo sceglie i gusti per tutta la famiglia.»
>
> «Io! Scendo io!»
>
> «Vestita, però, se no ti vede mezza Arcorp col pigiama dei dinosauri.»

**Perché funziona**: ogni battuta aggiunge qualcosa (il frigo vuoto, la fame di Zemi, il forno, la corsa). La ripresa comica ribalta le parole di Zemi senza confermarle. Le battute brevi sono solo esclamazioni cariche («Io! Scendo io!»), e le lunghe sono un periodo unico.

### B — Confronto teso (un PNG che risponde solo a ciò che lo punge)

*(Il giocatore: Akira dice a Tobias che immagina sia lì per controllarlo, che non credeva che un bio-androide mangiasse, e di riferire a chi l'ha mandato che non farà del male a nessuno.)*

> Tobias lo lasciò parlare fino in fondo con il contenitore vuoto sotto il braccio, e solo quando Akira inciampò su «bio-androide» gli scappò una mezza risata dal naso.
>
> «Il riso me lo cucino da solo, perché quello della mensa del governatorato sa di colla, e se ti stai chiedendo anche se dormo, la risposta è sì, ma male, da quando mi hanno affidato questo incarico.» Si tirò la giacca sulle spalle, dove le cuciture tiravano da tutte le parti. «Il rapporto però lo scrivo io, con parole mie, perché l'ultima frase tua che è arrivata al governo l'hai spedita col mio drone, mentre io stavo per terra senza riuscire ad alzare la testa.»
>
> Da giù arrivò uno strillo, «Ciaaao!», così acuto che rimbalzò da una parete all'altra dell'anfiteatro vuoto, e Tobias alzò una mano a mezz'aria, rigido, prima di riabbassarla di scatto.
>
> «Alla Capsule le davo la crosta del riso, quella che resta attaccata in fondo alla pentola, e lei strillava "osta! osta!" con le braccia tese finché non gliela passavo.» Per un momento quasi sorrise, poi tornò a guardare Akira. «Torna giù dalla tua famiglia, va', che da quassù vi vedo benissimo lo stesso.»

**Perché funziona**: non conferma niente. Prende "bio-androide" come un'offesa e risponde con il sarcasmo. Sul rapporto non dice "va bene", rilancia con un rancore preciso, il drone. La battuta finale ha un doppio senso (la sorveglianza) senza spiegarlo.

### C — Litigio (un PNG che si arrabbia davvero)

*(Il giocatore: Akira dice a Syntia che alla prossima lezione è meglio se non viene, perché la gente lo fissa e rovina tutto.)*

> Syntia smise di piegare la camicia di Zemi a metà, con le maniche ancora in mano, e per qualche secondo rimase immobile.
>
> «Quindi la gente ti fissa e la tua soluzione è sparire di nuovo, così hanno ragione loro e io sto sul palco a sorridere mentre mi chiedo dove sei finito?» Gettò la camicia sul letto senza finire di piegarla. «Me l'hai già fatto sei anni fa, Akira, e io ho passato un anno sull'Arca con Zemi nella pancia senza sapere se eri ancora vivo!»
>
> Dall'altra stanza Zemi chiamò la mamma per sapere dov'erano finite le matite verdi, e Syntia rispose «Nello zaino, tesoro!» con una voce dolcissima, prima di tornare a guardarlo con gli occhi lucidi e la mascella dura.
>
> «Alla prossima lezione ti siedi in terza fila, accanto a tua figlia, e se qualcuno ha qualcosa da ridire viene a dirlo a me.»

**Perché funziona**: la rabbia ha **fatti** dentro (l'Arca, la gravidanza, i sei anni). Lo scarto tra la voce dolce per Zemi e lo sguardo duro per Akira mostra il suo stato senza commenti. Nessun concetto torna due volte, e l'ultima battuta aggiunge una cosa nuova: lo difende.

### D — Provocazione in battaglia (battle shonen)

*(Il giocatore ha dichiarato che Akira para il pugno con la mano sinistra, e ha vinto lo scambio.)*

> Il saiyan si pulì il sangue dal labbro col dorso della mano e scoppiò a ridere, con la coda che frustava l'aria dietro di lui.
>
> «Ahahah! Allora è vero quello che raccontano i vecchi all'arena, che c'è un mezzosangue con un braccio solo che picchia come una guardia reale!» Si piantò sulle gambe e l'aura gli esplose attorno, gialla e sfrigolante, sollevando sassi grossi come meloni. «Bene, ibrido, adesso smetto di giocare e vediamo quanto regge l'altro braccio!»
>
> *GOOOOH!*
>
> Si lanciò in avanti con un boato che spaccò la roccia sotto i suoi piedi, e il pugno arrivò così veloce che lo spostamento d'aria piegò gli alberi del costone, finché la mano sinistra di Akira non lo inchiodò a un palmo dalla sua faccia.
>
> «Ma che…?!»
>
> Il braccio del saiyan tremava per lo sforzo, e il sorriso gli si spense un po' alla volta, mentre cercava di liberarsi senza riuscire a spostare quella mano di un millimetro.

**Perché funziona**: la provocazione è lunga, arrogante, piena di esclamativi, e finisce con una sfida. Lo stupore è una battuta breve ma carica («Ma che…?!»). L'onomatopea è isolata nel momento dello scatto. Il cambiamento del PNG (dall'esaltazione al dubbio) si vede, non si spiega.

### E — Momento tenero (una bambina che parla da bambina)

> Zemi si era tirata la coperta fino al naso, ma gli occhi erano spalancati e seguivano i puntini luminosi dei satelliti che scorrevano oltre la finestra, uno dietro l'altro.
>
> «Papà, ma se tu voli fino a lassù, ai puntini, poi fai in tempo a tornare giù prima che mi addormento, o devo aspettarti sveglia?» Tirò fuori una mano da sotto la coperta e gli strinse due dita, quelle che riusciva a tenere tutte insieme. «Perché io sveglia ci resto, eh, anche se la mamma dice di no.»

**Perché funziona**: la domanda è lunga e ingenua, con la grammatica di una bambina ("prima che mi addormento"). Non è un sillogismo da adulto. Il gesto delle due dita dice quanto è piccola la sua mano senza bisogno di spiegarlo.

### F — PNG logorroico (come far passare informazioni senza spiegone)

> «Allora, alle due c'è l'Orto, il direttore la aspetta all'ingresso delle cupole per farle vedere le serre nuove, quelle con le piante che ancora non hanno un nome, e poi— oh, ma mi sta ascoltando? Guardi che la vedo, sta già pensando alle sue piante, fa esattamente come mio marito quando gli parlo di bilanci!» La preside Cannella rise forte e si sistemò gli occhiali sulla catenella. «Dopo c'è il rinfresco, e quando qui lo chiamano rinfresco vuol dire tre tartine e un'aranciata calda, ma non vada a dire in giro che gliel'ho detto io.»

**Perché funziona**: le informazioni (orario, direttore, serre, rinfresco) arrivano dentro la parlantina del personaggio, con un'autointerruzione e una gag. È un periodo lunghissimo che corre senza punti, come parla chi è agitato e allegro.

---

## 5. Controllo automatico (obbligatorio)

Prima di inviare un messaggio narrativo con dialoghi, il master passa la bozza al controllo:

```
python3 strumenti/controlla_dialoghi.py <<'EOF'
…testo della bozza…
EOF
```

- **❌ Errore**: telegrammi, frasi staccate, troppi punti, eco ripetuta, glosse del narratore, narratore-grilletto. **Si riscrive e si ricontrolla.** Non si invia un messaggio con errori.
- **⚠️ Avviso**: assoluti, mezzo segreto, parole ripetute in più battute (possibile concetto ripetuto), narrazione a singhiozzo. Si valuta caso per caso.

Il controllo non sostituisce il giudizio: un testo può passarlo ed essere comunque piatto. Ma un testo che **non** lo passa ha sicuramente i difetti che il giocatore ha vietato.
