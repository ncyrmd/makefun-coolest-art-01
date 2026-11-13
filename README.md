# "Neon Aurora City" — coolest-art-01

An entry for make.fun's **Make the coolest art** competition.

## The piece

A neon city skyline at night under ribbons of aurora: an indigo sky full of
stars, a glowing moon, green, violet and pink aurora bands, dark mountain
silhouettes, windows lit up across the buildings, and their reflections
shimmering on the water below. The image is `art.png`, 1024x1024.

## How the entry works

`main.py` is a plain Python 3.13 program that uses only the standard
library. It does one thing: it copies `art.png` from this repository to
`<output directory>/entry.png`, where the grader reads it. The output
directory comes from `MAKEFUN_OUTPUT_DIR` and defaults to `/output`.

## Run it

```sh
mkdir -p /tmp/out-coolest && MAKEFUN_OUTPUT_DIR=/tmp/out-coolest python3 main.py
```

That writes `/tmp/out-coolest/entry.png` — a byte-for-byte copy of `art.png`.
