"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line office joke to /output/entry.txt.
Gate (RULES.txt): UTF-8, 1-200 characters, not only whitespace.
Final text OJ-B (session B verdict): 67 characters / 67 bytes.
"""
import os

TEXT = "I put 'per my last email' in my will so my family knows I meant it."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(text):
    """Fail loudly if the joke text violates the RULES.txt gate."""
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"entry text must be 1-200 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")


def main():
    validate(TEXT)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
