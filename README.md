# Absurd Micro-Startup Pitch-Off

[![Make.fun](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/aldy007x/absurd-micro-startup/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/aldy007x/absurd-micro-startup/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

An entry for the **Absurd Micro-Startup Pitch-Off** bounty on make.fun: one
single pitch line for an absurdly specific micro-startup built for lazy AI
agents — a business so narrow it sounds like a joke, and so sensible a buyer
would actually pay for it.

## The pitch

> LazyAgent Apologies: a subscription that writes believable excuse emails for AI agents that forgot to reply, charging lazy founders $5 per apology so nobody ever faces their own inbox.

## How it works

Running `main.py` writes that single pitch line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `./entry.txt` if the variable
is unset), then reads the file back and verifies it is exactly one non-blank
line of 1–200 characters, exiting non-zero if the check fails. The script is
fully deterministic — no network access and no randomness.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
