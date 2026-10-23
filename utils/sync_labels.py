"""Synchronize the repository label catalog through the authenticated gh CLI."""

import asyncio
import json
from pathlib import Path

from utils.projects import run_command


async def main() -> int:
    """Create or update catalog entries without deleting unrelated labels."""
    root = (await asyncio.to_thread(Path(__file__).resolve)).parent.parent
    raw = await asyncio.to_thread((root / ".github/labels.json").read_text, encoding="utf-8")
    labels: list[dict[str, str]] = json.loads(raw)
    for label in labels:
        await run_command(
            [
                "gh",
                "label",
                "create",
                label["name"],
                "--color",
                label["color"],
                "--description",
                label["description"],
                "--force",
                "--repo",
                "brunosrz/src",
            ],
            root,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
