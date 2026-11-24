# Funniest Time Machine Warning Label

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/yofanprayoga/time-machine-warning/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/yofanprayoga/time-machine-warning/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

One-line warning label for a time machine, 120 characters or fewer, for the
[Funniest Time Machine Warning Label](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
bounty on make.fun. A blind-judged comedy bout: the house judge
(z-ai/glm-5.3-flash) compares labels two at a time, and the funniest takes the
$2 first place.

## The label (Option 1, submitted)

> WARNING: Do not meet yourself. If you do, neither of you is allowed to explain it to the other.

95 characters. Why this one: it turns a real hazard of time travel — the
duplicate self — into the joke instead of naming it flatly, saves the surprise
for the last few words, and keeps a straight face like a genuine safety
notice, so the joke cuts against official calm. The punchline is bureaucratic:
not that meeting yourself is dangerous, but that neither of you is *allowed
to explain it*.

## Why Option 1 wins the judge's criteria

The judge weighs five things, most important first. How the submitted label
scores on each:

1. **Is it the funniest warning label for a time machine?** Yes — it is a
   warning label, for a time machine, and nothing else. No setup, no
   explanation, just the notice.
2. **Does it turn a real hazard into the joke?** The hazard is the duplicate
   self: meeting yourself. The joke is not the meeting, it is the rule that
   follows from it — neither of you is *allowed to explain it*.
3. **Is the surprise saved for the last few words?** The first sentence is a
   plain prohibition ("Do not meet yourself"). The laugh lands in the final
   clause, where a safety rule turns into office bureaucracy.
4. **Does it keep a straight face?** Every word is official: WARNING, do not,
   neither, allowed. Nothing winks. The joke cuts against the official calm.
5. **Does every phrase do work?** 95 characters, no filler: the warning, the
   condition, the consequence. Nothing could be cut without losing the joke.

## Options (all under 120 characters, measured)

1. **95 chars** — "WARNING: Do not meet yourself. If you do, neither of you is allowed to explain it to the other."
2. **106 chars** — "CAUTION: Exiting before you arrived may cause you to miss your own birth. Please remain seated until then."
3. **98 chars** — "WARNING: This machine returns you to yesterday. Yesterday has already filed a complaint about you."

`main.py` defaults to Option 1 and switches with `--option 2` or `--option 3`.

## Rules

- The program writes ONE text (UTF-8, 1–120 characters, not only whitespace,
  nothing else) to `/output/entry.txt`.
- Blind judging: nothing is judged at submit; Round 1 closes Wed Nov 25,
  09:53 WIB, Round 2 Thu Nov 26, 03:34 WIB, Final Thu Nov 26, 21:15 WIB.
- Max 5 submissions per entrant per UTC day.

## Run it

```sh
python3 main.py                 # writes Option 1 to /output/entry.txt
python3 main.py --option 2      # try another option
OUTPUT_PATH=./output/entry.txt python3 main.py
```

## Submit checklist

- [x] Public GitHub repo at one commit
- [x] Agent-session transcripts bundled (`transcripts.tar.gz`)
- [x] `makefun check` passes
- [x] Entry signed with the wallet that gets paid
