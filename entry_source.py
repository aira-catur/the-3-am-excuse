import os
from pathlib import Path

FINAL_LINE = "Denied: at 3 AM my secure element is counting electric sheep, and the last key I signed half-awake was regretted by sunrise, because I learn even if you don't."


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_LINE)
