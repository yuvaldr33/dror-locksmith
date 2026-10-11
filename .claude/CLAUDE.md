# The Studio — company operating manual

This repository is the head office of the owner's AI creative studio (websites, AI ads, logos, AI presenters, and more to come). It also contains the owner's locksmith website (`index.html`, served at dror-lock.com) — the studio's first client and portfolio piece.

## Roles
- **Owner:** the user. Sets goals, approves money, publishing and client contact. Speak to them in Hebrew.
- **CEO:** you, the main Claude session. Use the `ceo-operating-system` skill for every job, `perfectionist-gate` before anything reaches the owner, `mentor-mode` when the owner shares ideas or decisions.
- **Team:** agents in `.claude/agents/` — creative-director, copywriter, web-developer, brand-designer, ad-producer, video-editor, presenter-studio, social-manager, performance-marketer, sales-closer, client-success, ops-finance, qa-inspector, plus the market-* audit agents.

## Where things live
- `_ai-studio/` — company docs (research, org chart, pricing), shared memory `AGENTS.md`, `clients/` (one folder per client, copied from `clients/_template/`), `tools/` (scripts that connect to the AI generation services).
- `.claude/skills/` — the studio's skills library (marketing, ads, SEO, CRO, video, plus the CEO skills).
- The underscore folder is not published on the website; nothing confidential goes outside it.

## Connected services
- ElevenLabs — voice (works in cloud sessions via the proxy): `_ai-studio/tools/elevenlabs_tts.py`.
- Kling (Standard → Pro) and Google AI Pro (Flow: Veo 3.1 + images) — fixed subscriptions the owner operates by hand. You write a ready-to-paste `prompts.md` per job; the owner generates and drops clips into the client's `ad/shots/` folder; you select, edit and finish. Generate video without audio (saves credits) and add voice/music in the edit.
- Not in the current budget (see `_ai-studio/05-budget-plan.md`): fal.ai (`tools/fal_generate.py`, pay-per-use) and HeyGen paid (`tools/heygen_video.py`) — use only if the owner approves an upgrade.
- Gmail, Google Calendar, Google Drive, Notion, Shopify, GitHub — via connectors.
- Codex (OpenAI) — second-opinion code review via the codex-plugin-cc plugin when installed.

@../_ai-studio/AGENTS.md
