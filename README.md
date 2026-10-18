# Dragon Ball Last Chance — GDR play by chat con Claude

Campagna in solitario: tu sei **Akira**, Claude è il **Master**.

## Come si gioca
| Comando | Cosa fa |
|---|---|
| `/inizia-sessione` | Claude rilegge la memoria, ti fa il riassunto ("Nelle puntate precedenti…") e riprende la scena |
| `/tira [mod] [azione]` | Tiri tu il d10 per Akira, in combattimento o nelle prove di abilità con CD chiamate dal master. Es.: `/tira -3 Lancia della Giustizia al fianco` · `/tira +1 cd 8 convinco Tights` |
| `/salva` | Salvataggio intermedio su GitHub senza chiudere la sessione |
| `/aggiorna-regole` | Applica le regole nuove (da `main`) alla sessione in corso, senza chiuderla |
| `/fine-sessione` (o scrivi "chiudiamo") | Claude aggiorna cronaca, schede e mondo, poi salva tutto su GitHub (ramo `main`) |
| `[testo tra parentesi quadre]` | Parli al master fuori dal gioco |

Guida completa ai comandi: **`Comandi chat.md`**.

Dal terminale puoi tirare anche direttamente: `python3 strumenti/dado.py --mod -3 --motivo "Kamehameha"`.

## Dove sta la memoria
- `regole/`: le tue regole, il sistema di gioco con i chiarimenti, lo stile Toriyama, il metodo del mondo vivo, la guida di prosa shonen, la guida ai dialoghi e i modelli di dialogo shonen
- `mondo/`: ambientazione, stato attuale, calendario
- `personaggi/`: scheda di Akira e ciò che Akira sa
- `cronaca/`: riepilogo della campagna, resoconti delle sessioni, registro dei dadi
- `archivio/`: i tuoi documenti originali
- ⛔ `master_segreto/`: **non aprire**. Sono i piani e i segreti del master

Ogni sessione chiusa è un commit su git: si può sempre tornare indietro.
