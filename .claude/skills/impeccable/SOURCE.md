# Source

- Upstream: https://github.com/pbakaus/impeccable (path `.claude/skills/impeccable/`)
- Commit: 919dbeb (skill version 4.5.2)
- Author: Paul Bakaus. License: Apache 2.0 (see `LICENSE` and `NOTICE.md`, copied unchanged).
- Files copied unchanged: `SKILL.md`, `reference/`.
- Also copied unchanged (with the user's approval): `scripts/` (engine launcher,
  live-mode browser scripts, data) and the four `impeccable-*` agents in
  `.claude/agents/`.
- Not installed: the hooks from upstream `.claude/settings.json` (writing them
  was blocked by the environment's safety policy). The engine binary is not
  bundled; the launcher downloads it from the official GitHub release and
  verifies its SHA-256 on first use.
