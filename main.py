#!/usr/bin/env python3
"""Write the one-line fortune for the make.fun bounty
'Fortune Cookie for the Liquidated Trader'.

The fortune: an oracular promise that turns on the double meaning
of "fortune" - the wealth, not the luck. Warm and rueful, never cruel.
Gate: 1-160 characters, at most 20 words; this entry is 13 words
and 78 characters, reading whole in a single breath.
"""

import os

ENTRY = "A great fortune awaits you. It is, regrettably, the fortune you had yesterday."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
