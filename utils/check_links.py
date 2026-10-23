"""Check relative inline Markdown link destinations without network access."""

import asyncio
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+\"[^\"]*\")?\s*\)")


def missing_links(path: Path) -> list[str]:
    """Return missing local targets, ignoring code fences, URLs and anchors."""
    text = path.read_text(encoding="utf-8")
    prose: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            prose.append(re.sub(r"`[^`]*`", "", line))
    missing: list[str] = []
    for match in LINK.finditer("\n".join(prose)):
        target = match.group(1) or match.group(2)
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
            continue
        destination = path.parent / unquote(parsed.path)
        if not destination.exists():
            missing.append(target)
    return missing


async def main() -> int:
    """Inspect only the Markdown files supplied by pre-commit."""
    failed = False
    for filename in sys.argv[1:]:
        for target in await asyncio.to_thread(missing_links, Path(filename)):
            print(f"{filename}: missing target {target}")
            failed = True
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
