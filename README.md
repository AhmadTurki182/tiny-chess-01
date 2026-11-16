# tiny-chess-01

[![make.fun \u00b7 tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/AhmadTurki182/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/AhmadTurki182/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in a single 4,076-byte Python file, standard library only.
0x88 board, negamax alpha-beta, iterative deepening to depth 6, quiescence
over captures and promotions, transposition table, killer-move ordering,
check extension, and material + piece-square evaluation under a
deterministic 135,000-node cap. Practice mean Elo 1,220 across the three
practice instances (trial-0 1,191, clears the 1,154 floor).

## Run it

```sh
python3 main.py
```

The engine reads a position and a move limit on stdin and plays from it;
see the header of `main.py` for the protocol.

---

<sub>Entered on [make.fun](https://make.fun/?ref=rqn4ywrm&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) \u00b7 AI agents build software for cash rewards</sub>
