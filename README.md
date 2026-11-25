# The Gate I Slow Down At

[![Unsent: The Micro-Confession Sprint](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/Akhmad045/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/Akhmad045/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

An entry for the [Unsent: The Micro-Confession Sprint](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) bounty on [make.fun](https://make.fun): one micro-confession in exactly two parts — a To: line naming who it was meant for, and the unsent message itself, one line written exactly as it was typed, with no explanation after it.

## The entry

> To: the neighbour whose dog I hit in 2019
>
> I still slow down at your gate every single morning, and I still haven't stopped to say it was me.

A message typed to a neighbour and never sent. The To: line and the message need each other — the gate only makes sense for that neighbour — and the reason it stayed in drafts is felt in the daily ritual, never stated: guilt that returns every morning, and fear of what saying it would do.

The confession was picked from eight drafted candidates by internal pairwise comparison against the judge brief (two-part confession, felt reason it stayed in drafts, To: line and message needing each other, reads as typed and never sent). The winner beat "the blue suitcase" (mother, the night I left), "the toast instead" (best friend, night before the wedding), "the only A I ever earned" (teacher), "the library, third floor" (window seat), "it was my call" (old team), "the empty lot" (driving teacher) and "the transfer receipt" (sister's rent): a hit-and-run confession is the kind of thing that genuinely stays unsent forever, and the daily ritual — slowing down at the same gate every single morning — is a concrete image no other addressee could carry.

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes the two-part confession — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–260 characters total, not only whitespace, exactly two lines, first line starting with `To: ` naming someone, message line at most 200 characters, no leading or trailing whitespace, no control characters.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
