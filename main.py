"""Entry for make.fun's "The joke the reviewer laughs at" bounty.

Writes one original one-line joke about working beside AI coding
agents to /output/entry.txt. Deterministic, no network, no input.
"""

import os

JOKE = (
    "My AI agent fixed a typo by rewriting 47 files, "
    "so I approved the PR \u2014 the typo was the only line "
    "I actually understood."
)


def main() -> None:
    text = JOKE.strip()
    code_points = len(text)
    if not (1 <= code_points <= 280):
        raise SystemExit(f"joke is {code_points} code points, must be 1-280")
    if not text.strip():
        raise SystemExit("joke must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
