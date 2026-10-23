"""Validate Conventional Commit subjects for Git hooks and PR checks."""

import argparse
import asyncio
import re
from pathlib import Path

SUBJECT = re.compile(
    r"(?:feat|fix|docs|refactor|test|chore|ci|perf|build|revert)"
    r"(?:\([a-z0-9][a-z0-9._/-]*\))?!?: \S.*"
)


def valid_subject(subject: str) -> bool:
    """Require a recognized type, nonempty description and a short single line."""
    return (
        len(subject) <= 100
        and subject == subject.strip()
        and "\n" not in subject
        and "\r" not in subject
        and SUBJECT.fullmatch(subject) is not None
    )


async def main() -> int:
    """Read a hook message or an explicitly supplied PR title."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("message_file", nargs="?", type=Path)
    parser.add_argument("--title")
    args = parser.parse_args()
    if args.title is not None:
        subject = args.title
    elif args.message_file:
        message = await asyncio.to_thread(args.message_file.read_text, encoding="utf-8")
        subject = message.splitlines()[0] if message else ""
    else:
        parser.error("provide --title or a commit message file")
    if valid_subject(subject):
        return 0
    print("Use tipo(escopo): descrição, até 100 caracteres; por exemplo docs(cache): explain TTL")
    return 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
