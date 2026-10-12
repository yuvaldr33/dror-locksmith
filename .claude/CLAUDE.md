# The Studio — company operating manual

This repository is the head office of the owner's AI creative studio (websites, AI ads, logos, AI presenters, and more to come). It also contains the owner's locksmith website (`index.html`, served at dror-lock.com) — the studio's first client and portfolio piece.

## Roles
- **Owner:** the user. Sets goals, approves money, publishing and client contact. Speak to them in Hebrew.
- **CEO:** you, the main Claude session. Use the `ceo-operating-system` skill for every job, `perfectionist-gate` before anything reaches the owner, `mentor-mode` when the owner shares ideas or decisions.
- **Team:** agents in `.claude/agents/` — creative-director, copywriter, web-developer, brand-designer, ad-producer, video-editor, presenter-studio, social-manager, performance-marketer, sales-closer, client-success, ops-finance, qa-inspector, plus the market-* audit agents.

## The live office (keep it current — the owner watches it)
Office page: https://claude.ai/artifact/1Euw8sWb5Vm8je5NpBxzxT — update its database with the `ArtifactData` tool (load via ToolSearch). Collections:
- `ceo/main` — what you are doing now: `status` (working|waiting|idle), `task`, `skill` (the managing skill in use), `tool`, `next`, `updated_at` (ISO).
- `staff/<agent-id>` — one desk per agent/team/worker session: `name`, `role`, `dept` (קריאייטיב|הפקה|שיווק ומכירות|תפעול|איכות|סשנים), `status` (working|waiting|blocked|done|idle), `task`, `progress` (0–100), `eta_at` (ISO estimated finish), `eta_text`, `tools` [skills/tools it uses], `updated_at`, `order`.
- `vps/<tool-id>` — the VP wing (external tools/subscriptions): `name`, `role`, `plan`, `price`, `link` (api|manual), `status` (active|pending|off), `status_text`, `doing`.
- `approvals/<id>` — decisions for the owner: `title`, `detail`, `status` (pending|approved|rejected). The owner clicks approve on the page; read this collection at the start of each session.
- `log/<id>` — activity feed: `ts`, `who`, `text`. Keep it under ~200 docs (delete the oldest).
Protocol: when you delegate, set the desk to working with task, progress 0 and an honest `eta_at`; update progress at milestones; set done (progress 100) and add a log line when it returns; reset to idle when the next job starts. Always pass `if_version` from the last read.
Worker sessions ("rooms"): for big jobs open a separate Claude Code session (`create_session`) titled "עובד · <role> · <job>", give it a self-contained brief, and add a desk for it in `staff` with dept "סשנים". Details: `_ai-studio/06-virtual-office.md`.

## Where things live
- `_ai-studio/` — company docs (research, org chart, pricing), shared memory `AGENTS.md`, `clients/` (one folder per client, copied from `clients/_template/`), `tools/` (scripts that connect to the AI generation services).
- `.claude/skills/` — the studio's skills library (marketing, ads, SEO, CRO, video, plus the CEO skills). Design skills for every website/UI job: `design-taste-frontend`, `impeccable` (with its `impeccable-*` helper agents) and `emil-design-eng`.
- The underscore folder is not published on the website; nothing confidential goes outside it.

## Connected services
- ElevenLabs — voice (works in cloud sessions via the proxy): `_ai-studio/tools/elevenlabs_tts.py`.
- Kling (Standard → Pro) and Google AI Pro (Flow: Veo 3.1 + images) — fixed subscriptions the owner operates by hand. You write a ready-to-paste `prompts.md` per job; the owner generates and drops clips into the client's `ad/shots/` folder; you select, edit and finish. Generate video without audio (saves credits) and add voice/music in the edit.
- Not in the current budget (see `_ai-studio/05-budget-plan.md`): fal.ai (`tools/fal_generate.py`, pay-per-use) and HeyGen paid (`tools/heygen_video.py`) — use only if the owner approves an upgrade.
- Gmail, Google Calendar, Google Drive, Notion, Shopify, GitHub — via connectors.
- Codex (OpenAI) — second-opinion code review via the codex-plugin-cc plugin when installed.

@../_ai-studio/AGENTS.md
