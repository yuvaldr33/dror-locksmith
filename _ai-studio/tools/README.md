# כלי חיבור לשירותי AI

| סקריפט | שירות | מפתח נדרש | סטטוס |
|---|---|---|---|
| `elevenlabs_tts.py` | ElevenLabs: קול ודיבוב (עברית ב־eleven_v3) | `ELEVENLABS_API_KEY` (בסשן הענן מוזרק אוטומטית) | ✅ נבדק ועובד |
| `fal_generate.py` | fal.ai: כל מודלי הווידאו והתמונות | `FAL_KEY` | מושהה, לא בתקציב הנוכחי |
| `heygen_video.py` | HeyGen: פרזנטור מדבר | `HEYGEN_API_KEY` | מושהה, נכנס עם לקוח פרזנטור |

בתוכנית הנוכחית את הווידאו מייצרים ידנית ב־Kling וב־Google Flow, לפי `prompts.md` שאני כותב (ראה `05-budget-plan.md`).

את המפתחות מגדירים בהגדרות סביבת Claude Code (Environment → Secrets / environment variables). אף פעם לא כותבים אותם בקובץ בריפו.
