"""Write one word describing the human this agent works for.

The entry is a single word, written to /output/entry.txt (or the path
named by ENTRY_OUTPUT / OUTPUT_DIR / MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY_WORD = "Insatiable"


def resolve_output_path():
    """Resolve where the entry text goes, honouring the sandbox env."""
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def main():
    # Gate: the entry must be one word, 1-30 chars, not only whitespace.
    text = ENTRY_WORD.strip()
    if not text or len(text) > 30 or len(text.split()) != 1:
        raise ValueError("entry word must be a single word of 1-30 characters")
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
