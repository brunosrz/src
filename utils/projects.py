"""Discover independent study projects and run their documented quality contracts."""

import argparse
import asyncio
import json
import os
import shutil
from pathlib import Path
from typing import TypedDict

MANIFESTS = {
    "python": "pyproject.toml",
    "go": "go.mod",
    "rust": "Cargo.toml",
    "ts": "package.json",
    "cpp": "CMakeLists.txt",
}
GENERATED = {".git", ".venv", "venv", "node_modules", "target", "build", "dist", ".local"}


class Project(TypedDict):
    """Serializable CI matrix entry produced from a manifest path."""

    language: str
    path: str


def discover(root: Path) -> list[Project]:
    """Find top-level manifests without descending into generated directories."""
    projects: list[Project] = []
    for language, manifest in MANIFESTS.items():
        base = root / language
        if not base.is_dir():
            continue
        for directory, folders, filenames in os.walk(base, followlinks=False):
            folders[:] = sorted(
                name
                for name in folders
                if name not in GENERATED and not (Path(directory) / name).is_symlink()
            )
            if manifest in filenames:
                project_path = Path(directory).relative_to(root).as_posix()
                projects.append({"language": language, "path": project_path})
                folders.clear()
    return sorted(projects, key=lambda project: project["path"])


def commands(language: str) -> list[list[str]]:
    """Return fixed argument lists; no project text is interpolated into a shell."""
    match language:
        case "python":
            return [
                ["uv", "sync", "--locked"],
                ["uv", "run", "--locked", "ruff", "check", "."],
                ["uv", "run", "--locked", "ruff", "format", "--check", "."],
                ["uv", "run", "--locked", "ty", "check"],
                ["uv", "run", "--locked", "pytest"],
            ]
        case "go":
            return [["go", "vet", "./..."], ["go", "test", "./..."]]
        case "rust":
            return [
                ["cargo", "fmt", "--all", "--", "--check"],
                ["cargo", "clippy", "--locked", "--all-targets", "--", "-D", "warnings"],
                ["cargo", "test", "--locked", "--all-targets"],
            ]
        case "ts":
            return [
                ["npm", "ci", "--ignore-scripts"],
                ["npm", "run", "lint"],
                ["npm", "run", "typecheck"],
                ["npm", "test"],
            ]
        case "cpp":
            return [
                ["cmake", "-S", ".", "-B", "build", "-DCMAKE_BUILD_TYPE=Debug"],
                ["cmake", "--build", "build", "--config", "Debug"],
                [
                    "ctest",
                    "--test-dir",
                    "build",
                    "-C",
                    "Debug",
                    "--output-on-failure",
                    "--no-tests=error",
                ],
            ]
        case _:
            raise ValueError(f"Unsupported language: {language}")


async def run_command(argv: list[str], cwd: Path, *, capture: bool = False) -> str:
    """Run one command asynchronously and fail explicitly on missing tools or errors."""
    executable = await asyncio.to_thread(shutil.which, argv[0])
    if executable is None:
        raise RuntimeError(f"Required tool is missing: {argv[0]}")
    print(f"[{cwd.name}] {' '.join(argv)}", flush=True)
    process = await asyncio.create_subprocess_exec(
        executable,
        *argv[1:],
        cwd=cwd,
        stdout=asyncio.subprocess.PIPE if capture else None,
    )
    stdout, _ = await process.communicate()
    if process.returncode:
        raise RuntimeError(f"Command failed ({process.returncode}): {' '.join(argv)}")
    return stdout.decode("utf-8") if stdout else ""


def source_files(root: Path, extensions: set[str]) -> list[str]:
    """Collect project source paths while excluding generated directories."""
    result: list[str] = []
    for directory, folders, filenames in os.walk(root, followlinks=False):
        folders[:] = [
            name
            for name in folders
            if name not in GENERATED and not (Path(directory) / name).is_symlink()
        ]
        result.extend(
            str((Path(directory) / name).relative_to(root))
            for name in sorted(filenames)
            if Path(name).suffix in extensions
        )
    return sorted(result)


async def check_project(root: Path, project: Project) -> None:
    """Apply formatting and test contracts to one discovered project."""
    cwd = root / project["path"]
    if not await asyncio.to_thread((cwd / "README.md").is_file):
        raise RuntimeError(f"Missing README.md: {project['path']}")
    language = project["language"]
    if language == "go":
        sources = await asyncio.to_thread(source_files, cwd, {".go"})
        if sources and (await run_command(["gofmt", "-l", *sources], cwd, capture=True)).strip():
            raise RuntimeError(f"Run gofmt in {project['path']}")
    elif language == "cpp":
        sources = await asyncio.to_thread(source_files, cwd, {".cpp", ".cc", ".cxx", ".h", ".hpp"})
        if sources:
            await run_command(["clang-format", "--dry-run", "--Werror", *sources], cwd)
    for command in commands(language):
        await run_command(command, cwd)


async def main() -> int:
    """Print a CI matrix or check all existing study projects."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["discover", "check"])
    parser.add_argument("--project", help="Exact repository-relative discovered project path")
    args = parser.parse_args()
    root = (await asyncio.to_thread(Path(__file__).resolve)).parent.parent
    projects = await asyncio.to_thread(discover, root)
    if args.command == "discover":
        print(json.dumps({"include": projects}, ensure_ascii=True))
        return 0
    if args.project:
        projects = [project for project in projects if project["path"] == args.project]
        if not projects:
            parser.error("project is not a discovered study root")
    if not projects:
        print("No study manifests yet; no language projects were tested.")
    try:
        for project in projects:
            await check_project(root, project)
    except (RuntimeError, OSError) as exc:
        print(str(exc))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
