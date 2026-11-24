"""Write the funniest one-line bio for an AI on a dating app to $MAKEFUN_OUTPUT_DIR/entry.txt (1-180 chars, one line, deterministic)."""

import os

LINE = "I hallucinated a whole date last week, candlelight and a stuttered waltz, none of it real. I apologised four times. I am slowly learning not to invent the evening."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    content = LINE + "\n"
    if not (1 <= len(content) <= 180 and content.strip()):
        raise ValueError("bad length")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(out_path, len(content))


if __name__ == "__main__":
    main()
