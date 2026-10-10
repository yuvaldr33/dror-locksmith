# כלי חיבור לשירותי AI

| סקריפט | שירות | מפתח נדרש | סטטוס |
|---|---|---|---|
| `elevenlabs_tts.py` | ElevenLabs: קול ודיבוב (עברית ב־eleven_v3) | `ELEVENLABS_API_KEY` (בסשן הענן מוזרק אוטומטית) | ✅ נבדק ועובד |
| `fal_generate.py` | fal.ai: כל מודלי הווידאו והתמונות | `FAL_KEY` | ממתין למפתח |
| `heygen_video.py` | HeyGen: פרזנטור מדבר | `HEYGEN_API_KEY` | ממתין למפתח |

את המפתחות מגדירים בהגדרות סביבת Claude Code (Environment → Secrets / environment variables). אף פעם לא כותבים אותם בקובץ בריפו.
