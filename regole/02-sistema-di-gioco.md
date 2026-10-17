# Sistema di gioco (V4 + chiarimenti ufficiali)

Testo originale integrale: `archivio/sistema-di-gioco-v4-originale.md`. I **chiarimenti del giocatore** del 17/10/2026 hanno precedenza. Le parti segnate **[raccordo]** sono mie interpretazioni per coprire i buchi del regolamento: le applico con coerenza finché il giocatore non dice diversamente.

## 1. Il dado

Si usa un d10 per prove di abilità, combattimento e prove sociali.

| Risultato | Esito |
|---|---|
| 1 | Fallimento critico |
| 2-3 | Fallimento |
| 4-6 | Successo parziale |
| 7-9 | Successo pieno |
| 10 | Successo critico |

- **Chi tira**: il giocatore tira i dadi di Akira con `/tira`. Io tiro quelli dei PNG con `strumenti/dado.py`. Tutti i tiri finiscono nel registro.
- **Critici [raccordo]**: dipendono **solo dal dado naturale**. Un 1 naturale è sempre critico e un 10 naturale è sempre critico, qualunque sia il modificatore. Per il grado di successo il totale modificato si legge tra 2 e 9: i modificatori non creano né annullano critici.
- **Scambio**: vince il **totale più alto**. Esempio: Akira fa 5, il PNG fa 6, vince il PNG.
- **Parità [raccordo]**: nessuno prevale, i colpi si neutralizzano (scontro di forze). Se entrambi hanno ottenuto almeno un successo pieno, possono andare a segno tutti e due, a giudizio narrativo.
- **Più avversari [raccordo]**: Akira tira una volta per round e il suo totale si confronta con il tiro di ciascun avversario coinvolto in quel round.
- **Prove fuori combattimento**: le tira il giocatore. Contro un PNG che si oppone attivamente, tiro anche per il PNG e confronto. Se la prova non ha senso (impossibile, o banale e senza rischio), non si tira.

## 2. Danni

Ordine di calcolo ufficiale:

1. **Danno base**: 3.
2. **+ bonus BP**: dalla fascia del **BP base** (tabella sotto). Danno base + bonus BP **non supera mai 10**.
3. **+ bonus tecnica**: Base +1, Intermedia +2, Avanzata +3, Suprema +4, Divina +6, Utility 0.
4. **+ grado di successo**: Parziale +1, Pieno +2.
5. **× percentuali**: si applicano **dopo** aver sommato i punti 1-4. Sono le % della tecnica ("+20% danni"), delle trasformazioni, del Kaioken, dell'Overlimit, del malus a due mani e del gap BP. Le % si **sommano tra loro** e il totale si applica una volta sola. Esempio: +20% +25% −20% = +25%.
6. **Successo critico**: raddoppia il danno totale.
7. **Attacco − Difesa** (chiarimento del giocatore): **Danno inflitto = (Attacco dell'attaccante − Difesa del bersaglio) + risultato dei punti 1-6**.
   - Difesa del bersaglio = valore Difesa della scheda + bonus difesa della fascia BP base, × le % di difesa (barriere, trasformazioni, malus del gap).
   - **[raccordo]** Se Attacco − Difesa è negativo, il valore negativo si sottrae comunque. Se il danno finale è ≤ 0, il colpo non fa danni ("non gli ha fatto niente").
   - Arrotondamento **[raccordo]**: per difetto, alla fine.

### Fasce di BP (bonus solo sul BP base, mai su trasformazioni o potenziamenti temporanei)

| Fascia BP base | HP e Ki (cumulativi) | Danni e Difesa (si usa solo la fascia raggiunta) |
|---|---|---|
| 1.000 – 10.000 | +5 HP, +2 Ki | +2 / +2 |
| 11.000 – 50.000 | +5 HP, +2 Ki | +2 / +2 |
| 51.000 – 150.000 | +5 HP, +4 Ki | +2 / +2 |
| 151.000 – 500.000 | +10 HP, +6 Ki | +3 / +3 |
| 501.000 – 1.000.000 | +15 HP, +6 Ki | +3 / +3 |
| 1.100.000 – 7.000.000 | +15 HP, +6 Ki | +5 / +5 |
| 7.100.000 – 10.000.000 | +15 HP, +6 Ki | +8 / +8 |
| 15.000.000 – 20.000.000 | +15 HP, +6 Ki | +10 / +10 |

- PNG base: 15 HP e 10 Ki, più i bonus cumulativi di HP e Ki.
- **[raccordo]** Tra 10.000.001 e 14.999.999 vale la fascia +8/+8. Sopra i 20.000.000 vale +10/+10 (il massimo).
- I bonus di danno e difesa **non** sono cumulativi: lo dimostra il tetto di 10 sul danno base.

### Grado delle tecniche [raccordo — assegnato da me]

| Tecnica | Grado | Note |
|---|---|---|
| Ki Blast, Raffica Ki Blast | Base (+1) | + la % della scheda |
| Kamehameha, Garlick Gun, Big Bang Attack, Cannone Fotonico, Makankosappo | Intermedia (+2) | Makankosappo perforante: ignora metà della Difesa scheda del bersaglio |
| Lancia della Giustizia, Final Flash, Granata super esplosiva, Raggio ai neutrini | Avanzata (+3) | |
| Final Flash ancestrale | Suprema (+4) | |
| Genkidama | Divina (+6) | |
| Taiyoken, Barriera Repulsiva, Volo, Luna Artificiale, Mafuba | Utility (il grado ne misura l'utilità, non il danno) | |

## 3. Regola del gap di BP

Si calcola sul **BP effettivo del momento**.

**[raccordo]** BP effettivo = BP base × percentuale espressa × moltiplicatori attivi: trasformazione, Kaioken xN, Risonanza ×1,5, Oozaru ×10, marchio Majin. Un personaggio che non esprime tutto il potere ha un BP effettivo più basso (Regola 7).

| Situazione | Effetto |
|---|---|
| Avversario con BP **≥ 30%** più alto | Il più debole: −20% difesa, −20% danni. Se è il PG: anche **−3 al dado** |
| Avversario con BP **≥ 100%** più alto | Il più debole: −50% difesa, −50% danni. Se è il PG: anche **−5 al dado** |
| PG con BP **≥ 30%** più alto | Oltre ai malus dell'avversario, il PG ha **+2 al dado** |
| PG con BP **≥ 50%** più alto | Oltre ai malus dell'avversario, il PG ha **+3 al dado** |

I modificatori al dado del gap valgono solo per il PG. I PNG subiscono solo i malus percentuali.

## 4. HP, Ki, KO e morte

- **0 HP**: fuori combattimento. Il colpo di grazia lo decide la **coerenza del PNG**: Odio e Spietatezza, situazione, interesse. Se il PNG ha motivo di uccidere, uccide (Regola 2).
- **[raccordo]** Un singolo colpo che porta gli HP **sotto −15** è letale, salvo cure immediate di livello Senzu o tecniche namecciane.
- **Ricordo fisso**: se Akira muore, la sua anima **svanisce per sempre** (prezzo di S-Shenron). Non c'è aldilà per lui e le sfere del drago non esistono.
- **Recupero [raccordo]**: con un riposo vero (una notte) si recupera tutto il Ki e il 25% degli HP massimi. Le ferite gravi richiedono giorni o cure mediche. Un Senzu ripristina tutto.

## 5. Rapporti e moralità dei PNG (scala 1-6)

Ogni PNG importante ha cinque parametri: **Rispetto**, **Amore**, **Odio** (verso Akira), **Spietatezza** e **Lealtà**. Le tabelle complete sono in `archivio/sistema-di-gioco-v4-originale.md`. In breve:

- **Rispetto**: 1 fa il contrario di quello che dice Akira; 2 dà −2 alle prove sociali; 3 neutro; 4 dà +1 a Persuasione; 5 dà +2 e obbedisce agli ordini tattici; 6 indiscutibile.
- **Amore**: 1 non muove un dito; 3 aiuta a basso rischio; 4 combatte al suo fianco; 5 si mette sulla traiettoria di un colpo letale; 6 sacrifica sé stesso e i propri ideali.
- **Odio**: 2 provoca; 3 rivalità; 4 vuole umiliare e far soffrire; 5 il colpo di grazia è garantito; 6 attacca a vista e colpisce gli affetti di Akira.
- **Spietatezza**: 1 non uccide mai; 3 pragmatico; 4 infierisce; 5 sfrutta i critici del giocatore per mutilare; 6 sadismo.
- **Lealtà**: 1 traditore; 2 opportunista; 3 si preserva; 4 mantiene la parola; 5 fedele fino alla fine; 6 martire.

I valori **cambiano** con le azioni di Akira e con gli eventi. Li aggiorno nelle schede dei PNG.

## 6. Crescita di Akira (la decide il master)

- **Allenamento**: il BP cresce solo con allenamento vero, giocato o concesso in un salto temporale approvato. Conta l'intensità: gravità, avversari, stanze speciali. Tre anni senza allenamento non hanno fatto calare il potenziale, ma neanche crescere.
- **Esperienze estreme**: battaglie quasi mortali ed emozioni violente possono dare salti di potere. Akira **non ha più Zenkai**.
- **Tecniche nuove**: vanno imparate da qualcuno, inventate con un allenamento mirato o sbloccate da un evento forte. Ognuna ha costo e grado coerenti col sistema.
- **Premi di fine arco**: come il SSJ Full Power dopo *L'arrivo dei Saiyan parte 2*. Li assegno quando un arco narrativo si chiude, in proporzione a ciò che è successo.
- Ogni cambiamento lo annoto in `personaggi/akira.md` e nella cronaca, con il motivo.
