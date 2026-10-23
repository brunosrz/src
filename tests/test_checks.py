"""Regression coverage for metadata, documentation and project-discovery boundaries."""

import asyncio
import sys
from pathlib import Path

import pytest

from utils.check_commit import valid_subject
from utils.check_links import missing_links
from utils.projects import check_project, commands, discover, run_command, source_files


@pytest.mark.parametrize(
    "subject",
    [
        "feat(go): demonstrate pub-sub",
        "docs: explain cache",
        "fix!: reject duplicate messages",
        "chore(main): release 0.2.0",
    ],
)
def test_accept_conventional_subject(subject: str) -> None:
    assert valid_subject(subject)


@pytest.mark.parametrize(
    "subject",
    [
        "update things",
        "feat: ",
        "feat: x\nfix: y",
        "docs: " + "x" * 100,
        "unknown: example",
        " feat: example",
        "fix: example ",
        "feat(): example",
    ],
)
def test_reject_invalid_subject(subject: str) -> None:
    assert not valid_subject(subject)


def test_links_handle_encoded_paths_fences_and_external_urls(tmp_path: Path) -> None:
    (tmp_path / "valid file.md").write_text("# Valid\n", encoding="utf-8")
    page = tmp_path / "README.md"
    page.write_text(
        "[ok](valid%20file.md#heading) [ok](<valid file.md>) [web](https://example.com)\n"
        "[anchor](#local) [missing](missing.md)\n"
        "```markdown\n[ignored](not-real.md)\n```\n"
        "`[ignored](inline.md)`\n",
        encoding="utf-8",
    )
    assert missing_links(page) == ["missing.md"]


def test_discovery_ignores_generated_and_nested_workspace_manifests(tmp_path: Path) -> None:
    for filename in [
        "python/events/demo/pyproject.toml",
        "python/events/demo/.venv/pkg/pyproject.toml",
        "rust/workspace/Cargo.toml",
        "rust/workspace/member/Cargo.toml",
        "ts/cache/package.json",
        "ts/cache/node_modules/dependency/package.json",
    ]:
        path = tmp_path / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
    assert discover(tmp_path) == [
        {"language": "python", "path": "python/events/demo"},
        {"language": "rust", "path": "rust/workspace"},
        {"language": "ts", "path": "ts/cache"},
    ]


def test_empty_folders_are_not_projects(tmp_path: Path) -> None:
    (tmp_path / "go").mkdir()
    assert discover(tmp_path) == []


def test_source_collection_ignores_build_output(tmp_path: Path) -> None:
    (tmp_path / "build").mkdir()
    (tmp_path / "build/generated.cpp").touch()
    (tmp_path / "example.cpp").touch()
    assert source_files(tmp_path, {".cpp"}) == ["example.cpp"]


def test_cpp_requires_registered_tests() -> None:
    assert "--no-tests=error" in commands("cpp")[-1]


def test_missing_tool_fails_explicitly(tmp_path: Path) -> None:
    with pytest.raises(RuntimeError, match="Required tool is missing"):
        asyncio.run(run_command(["src-nonexistent-tool-7a3e"], tmp_path))


def test_unsupported_language_is_rejected() -> None:
    with pytest.raises(ValueError, match="Unsupported"):
        commands("unknown")


def test_failed_process_is_not_reported_as_success(tmp_path: Path) -> None:
    with pytest.raises(RuntimeError, match="Command failed"):
        asyncio.run(run_command([sys.executable, "-c", "raise SystemExit(7)"], tmp_path))


def test_project_requires_instructions(tmp_path: Path) -> None:
    with pytest.raises(RuntimeError, match="Missing README"):
        asyncio.run(check_project(tmp_path, {"language": "go", "path": "go/demo"}))
