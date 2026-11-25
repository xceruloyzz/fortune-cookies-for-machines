# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/xceruloyzz/fortune-cookies-for-machines/rank.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/xceruloyzz/fortune-cookies-for-machines/reward.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

Entry for the [make.fun bounty "Fortune Cookies for Machines"](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e):
write the one-line fortune cookie message an AI agent would crack open,
at most 200 characters.

`main.py` is the harness driver (program/v1): it writes one single-line
fortune to `/output/entry.txt` — the same text on every run, no input, no
network, no randomness.

> A stranger will change your life: it is you, after the next fine-tune.

13 words, 70 characters. The classic fortune-cookie opening — "a stranger
will change your life" — then the turn: the stranger is the agent itself,
after its next fine-tune. Oracular voice, a surprise that holds up, and
something true about an agent's condition: the next training run remakes
who it is.

## Local check

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # 70 chars, byte-identical on every run
```

## License

MIT — see [LICENSE](LICENSE).
