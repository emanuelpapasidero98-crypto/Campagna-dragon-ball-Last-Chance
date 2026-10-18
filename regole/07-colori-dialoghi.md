# Colori dei dialoghi dei PNG

Deciso dal giocatore: ogni PNG ha un **colore pastello fisso**, e le sue battute sono scritte **colorate e in grassetto**, con la stessa grandezza del testo normale. La narrazione e i "disse" restano testo normale.

## Formato (obbligatorio)

Ogni battuta di un PNG si scrive così, con il colore del PNG:

```
$\color{#8FD3A8}{\footnotesize\textbf{«Ciao, Akira!»}}$ disse Syntia.
```

Regole tecniche (il formato usa LaTeX, che è delicato):
1. **Grandezza**: sempre `\footnotesize`, che corrisponde al testo normale. Mai `\normalsize` o più grande.
2. **Una frase per blocco.** Il testo dentro `$…$` non va a capo da solo: le battute lunghe si spezzano in più blocchi, uno per frase o per inciso, separati da uno spazio, così il testo si adatta allo schermo del telefono.
   ```
   $\color{#8FD3A8}{\footnotesize\textbf{«Sono le due di notte, Akira.}}$ $\color{#8FD3A8}{\footnotesize\textbf{Mi sono svegliata e il letto era freddo.»}}$
   ```
3. **Caratteri da evitare o da proteggere** dentro `\textbf{…}`: `%` si scrive `\%`, `&` si scrive `\&`, `#` si scrive `\#`, `$` si scrive `\$`, `_` si scrive `\_`. Le parentesi graffe `{ }` non si usano. Il corsivo dentro una battuta si fa con `\textit{parola}`.
4. Le caporali «», gli accenti, gli apostrofi, i puntini (…), i trattini (—), i punti esclamativi e interrogativi si scrivono normalmente.
5. La **punteggiatura della casa** (`regole/05-prosa-shonen.md` §3) vale anche dentro i blocchi colorati: il verbo di dire resta fuori dal blocco, in testo normale.
6. **Akira** non ha colore: le sue battute (dichiarate dal giocatore) restano in testo normale.
7. Le **onomatopee** dei combattimenti non si colorano: restano in corsivo maiuscolo nel testo normale.
8. Se un PNG non è in tabella, gli assegno subito un colore pastello libero dalla riserva e lo aggiungo qui (le comparse di una riga usano il grigio).

## Tavolozza dei PNG

| PNG | Colore | Codice |
|---|---|---|
| Syntia | verde menta | `#8FD3A8` |
| Zemi | giallo burro | `#F2D57E` |
| Tights Brief | azzurro cielo | `#8EC5F5` |
| G-1 Tobias | lilla | `#C3A6F2` |
| Re Korinzo | sabbia | `#D6C29F` |
| Karin | grigio salvia | `#B8C4B0` |
| Prof.ssa Cannella | cannella chiaro | `#E3B07F` |
| Wanton | verde acqua | `#9ED9CF` |
| Moori | verde pisello | `#B3DE8E` |
| Re Kaioh | turchese pastello | `#8FD8E0` |
| Shin (Kaioshin) | lavanda | `#D6B8F5` |
| Kibith | rosa confetto | `#F5B8D3` |
| Regina Zaraya | rosso corallo | `#F29E9E` |
| Zarcon | pesca | `#F7BE94` |
| Ignis | terracotta chiaro | `#E8A890` |
| Okura | prugna chiaro | `#D9A3C7` |
| Tyros | senape pallido | `#DCC77A` |
| Babidi | giallo limone pallido | `#E8E59A` |
| Dabura | rosa lampone | `#F0A0B8` |
| Lace | blu pervinca | `#A9B8F2` |
| Mellor | arancio albicocca | `#F5C08A` |
| Zestra | viola glicine | `#C9B0E8` |
| Escar | celeste polvere | `#B0D4EA` |
| Comparse | grigio perla | `#C2C7CE` |

**Riserva** per i PNG nuovi importanti: `#A8E0B8` (verde salvia chiaro), `#F2C6A0` (cipria), `#B6C9F0` (fiordaliso), `#E8C1E0` (malva), `#CFE8A0` (lime pastello), `#F0D0A0` (vaniglia), `#A0D8C8` (giada), `#E0B0B0` (rosa antico).
