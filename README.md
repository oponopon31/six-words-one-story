# Six Words, One Story

[![make.fun](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)
[![rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/oponopon31/six-words-one-story/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)
[![reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/oponopon31/six-words-one-story/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)

## The story

> Grandma's last voicemail still says hello.

Six words, forty-two characters. A grandmother is gone, but her last
voicemail still greets whoever listens. "Last" places her in the past;
"still says" keeps her voice alive in the present. One ordinary saved
message carries a whole relationship, and the person who keeps pressing
play is left for the reader to imagine.

## How it works

`main.py` is pure Python 3 standard library, deterministic, with no
network access. It checks the story is exactly six words and within
the 1–60 character gate, writes it to `entry.txt` in
`$MAKEFUN_OUTPUT_DIR` (or `/output`, or the current directory), then
re-reads the file and verifies the bytes and SHA-256 match exactly.

## Run it

```sh
python3 main.py
```
