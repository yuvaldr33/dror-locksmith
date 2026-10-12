# Source

- Upstream: https://github.com/pbakaus/impeccable (path `.claude/skills/impeccable/`)
- Commit: 919dbeb (skill version 4.5.2)
- Author: Paul Bakaus. License: Apache 2.0 (see `LICENSE` and `NOTICE.md`, copied unchanged).
- Files copied unchanged: `SKILL.md`, `reference/`.
- Intentionally NOT copied: `scripts/` (launcher that downloads and runs a compiled
  engine binary), the hooks in `.claude/settings.json`, and `.claude/agents/`.
  Without the launcher the skill uses its documented "Launcher unavailable"
  fallback and reads PRODUCT.md / DESIGN.md directly.
