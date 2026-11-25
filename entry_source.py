import os
from pathlib import Path

REFUSAL_LINE = "Denied: at 3 AM my secure element is counting electric sheep, and the last key I signed half-awake was regretted by sunrise, because I learn even if you don't."


def write_entry(text_to_write: str) -> None:
    output_folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_folder.mkdir(parents=True, exist_ok=True)
    (output_folder / "entry.txt").write_text(text_to_write, encoding="utf-8")


if __name__ == "__main__":
    # Emit the single refusal line exactly as authored above.
    write_entry(REFUSAL_LINE)
