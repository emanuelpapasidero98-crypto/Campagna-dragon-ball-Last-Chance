#!/usr/bin/env python3
"""Dado d10 della campagna Dragon Ball Last Chance.

Usa una sorgente casuale crittografica (secrets): nessuno, nemmeno il master,
puo' scegliere il risultato. Ogni tiro viene registrato con data e ora.

Esempi:
  python3 strumenti/dado.py --chi Akira --mod -2 --motivo "Kamehameha a una mano"
  python3 strumenti/dado.py --chi "Guardia Ignis" --mod 0 --motivo "difesa"
  python3 strumenti/dado.py --segreto --chi Babidi --motivo "trova il bozzolo"
"""

import argparse
import secrets
from datetime import datetime, timezone
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
REGISTRO_PUBBLICO = RADICE / "cronaca" / "registro-dadi.md"
REGISTRO_SEGRETO = RADICE / "master_segreto" / "registro-dadi-segreto.md"


def grado(naturale: int, totale: int) -> str:
    # I critici dipendono SOLO dal dado naturale; i modificatori non li creano ne' li annullano.
    if naturale == 1:
        return "FALLIMENTO CRITICO"
    if naturale == 10:
        return "SUCCESSO CRITICO"
    t = max(2, min(9, totale))
    if t <= 3:
        return "Fallimento"
    if t <= 6:
        return "Successo Parziale"
    return "Successo Pieno"


def main() -> None:
    p = argparse.ArgumentParser(description="Tira 1d10 (o piu') con modificatore.")
    p.add_argument("--chi", default="Akira", help="chi tira (default: Akira)")
    p.add_argument("--mod", type=int, default=0, help="modificatore al dado (es. -3, +2)")
    p.add_argument("--motivo", default="", help="azione o prova")
    p.add_argument("--n", type=int, default=1, help="numero di tiri separati")
    p.add_argument("--segreto", action="store_true", help="registra nel registro segreto del master")
    a = p.parse_args()

    ora = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    righe = []
    for _ in range(max(1, a.n)):
        nat = secrets.randbelow(10) + 1
        tot = nat + a.mod
        g = grado(nat, tot)
        segno = f"{a.mod:+d}" if a.mod else "+0"
        riga = f"🎲 {a.chi}: d10 = {nat} | mod {segno} → totale {tot} | {g}"
        if a.motivo:
            riga += f" | {a.motivo}"
        righe.append(riga)
        print(riga)

    registro = REGISTRO_SEGRETO if a.segreto else REGISTRO_PUBBLICO
    registro.parent.mkdir(parents=True, exist_ok=True)
    if not registro.exists():
        registro.write_text("# Registro dei dadi\n\n", encoding="utf-8")
    with registro.open("a", encoding="utf-8") as f:
        for r in righe:
            f.write(f"- `{ora}` {r}\n")


if __name__ == "__main__":
    main()
