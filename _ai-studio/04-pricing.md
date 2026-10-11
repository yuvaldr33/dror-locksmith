# סיכום מחירים: מנויים וכלים

**נבדק:** אוקטובר 2026, ממקורות צד־שלישי ומדפי ספקים. מחירים משתנים מהר, אז כדאי לוודא בדף הספק לפני רכישה. המחירים בדולר.

> ⚠️ **עודכן 11.10.2026:** התקציב שנקבע הוא 200–400 ₪ לחודש, ראה `05-budget-plan.md`. הטבלאות כאן הן המפה המלאה לעתיד. השער הנכון הוא בערך 3.1 ₪ לדולר, ולא 3.7 כמו שמופיע בעמודת ₪ בהמשך.

## חבילת התחלה (שלב 1): מה שבאמת צריך
| כלי | תפקיד | מנוי | $/חודש | ₪ בערך |
|---|---|---|---|---|
| **Claude Max 5x** | המנכ״ל וכל הסוכנים | חובה | $100 | 370 |
| **fal.ai** | וידאו ותמונות מכל המודלים (Veo 3.1, Kling, Seedance, Flux, Nano Banana, Recraft) במפתח אחד | לפי שימוש | ~$50–100 | 185–370 |
| **ElevenLabs Creator** | קול, דיבוב בעברית, שיבוט קול לפרזנטורים | חובה | $22 | 80 |
| **HeyGen Creator** | פרזנטור מדבר | חובה לחבילת פרזנטורים | $29 | 107 |
| **Suno Pro** | מוזיקה לפרסומות (כולל רישיון מסחרי) | מומלץ | $10 | 37 |
| **DaVinci Resolve** | עריכה ידנית כשצריך | חינם | $0 | 0 |
| **Netlify / Cloudflare Pages** | אחסון אתרים | חינם להתחלה | $0 | 0 |
| **סה״כ שלב 1** | | | **~$210–260** | **~780–960 ₪** |

## תוספות לשלב הצמיחה
| כלי | למה | $/חודש |
|---|---|---|
| Claude Max 20x | יותר סוכנים במקביל, יותר עבודה | $200 (במקום 5x) |
| Higgsfield Plus | דמויות עקביות בסצנות קולנועיות (Soul ID), יש לו MCP | ~$59 חודשי / $47 שנתי |
| Midjourney Standard | אסתטיקה ייחודית למודבורדים ותמונות | $30 ($24 שנתי) |
| Kling Pro (ישיר) | אם מייצרים הרבה וידאו, יוצא זול יותר מ־fal | $37 |
| Google AI Pro | Veo ו־Nano Banana בממשק Flow, לעבודה ידנית | $19.99 |
| n8n Cloud Starter | אוטומציות לעסק (ליד ← וואטסאפ ← פגישה) | ~€24 (או חינם באחסון עצמי) |
| Vercel Pro | אחסון אתרי לקוחות ב־Next.js (בתוכנית החינמית אסור שימוש מסחרי) | $20 |
| ElevenLabs Pro | נפח קול גדול | $99 (במקום Creator) |
| ChatGPT Plus + Codex | עין שנייה על קוד, תמונות מהירות בצ׳אט | $20 |
| Recraft | לוגואים בווקטור. דרך fal זה ~$0.04–0.30 לתמונה, בלי מנוי | לפי שימוש |
| **סה״כ צמיחה מלא** | | **~$550–650** |

## כמה עולה עבודה אחת (עלות AI בלבד)
| עבודה | חישוב | עלות משוערת |
|---|---|---|
| פרסומת 30 שניות, Veo 3.1 Fast עם אודיו | ~10 שוטים × 6 שנ׳ × 3 טייקים = 180 שנ׳ × $0.15 | **~$27** |
| אותה פרסומת ב־Veo 3.1 Standard | 180 שנ׳ × $0.40 | **~$72** |
| אותה פרסומת ב־Kling 3.0 Pro | 180 שנ׳ × $0.11–0.17 | **~$20–30** |
| לוגו (40 וריאציות וקטור) | 40 × $0.04–0.30 | **$2–12** |
| פרזנטור (גיליון דמות + 5 סרטונים) | תמונות + קרדיטים ב־HeyGen | בתוך המנוי |
| אתר | זמן סוכנים בלבד | בתוך מנוי Claude |

**המסקנה:** עלויות ה־AI לעבודה הן עשרות דולרים, כך שכמעט כל המחיר ללקוח הוא רווח גולמי. את המחיר קובע הערך ללקוח, לא העלות.

## איך לחסוך
- מתחילים בחבילת שלב 1 בלבד, ומוסיפים כלי רק כשיש לקוח שצריך אותו.
- כלי שלא השתמשנו בו 30 יום מבטלים (ops-finance עוקב אחרי זה).
- טייקים זולים קודם (Veo Fast / Kling), ורק על השוט הנבחר מריצים את הגרסה היקרה.

## מקורות
- [Claude Max pricing](https://ai.zenken.co.jp/en/post/claude-pro-vs-max-comparison/)
- [fal – Veo 3.1 pricing](https://fal.ai/models/fal-ai/veo3.1) · [AI API pricing Sep 2026](https://www.teamday.ai/blog/ai-api-pricing-comparison-2026) · [Kling cost per second](https://costgoat.com/pricing/kling)
- [ElevenLabs pricing 2026](https://smallest.ai/blog/elevenlabs-pricing-plans-cost-what-you-get-in-2026)
- [HeyGen pricing 2026](https://www.arcade.software/post/heygen-pricing)
- [Higgsfield pricing 2026](https://www.krea.ai/blog/higgsfield-pricing-explained-2026-unlimited-credits-and-real-monthly-costs)
- [Midjourney pricing 2026](https://diyai.io/ai-tools/midjourney-pricing/)
- [Runway & Kling plans](https://www.costbench.com/compare/runway-vs-kling/) · [Kling plans](https://diyai.io/ai-tools/video-generation/kling-ai-pricing/)
- [Google AI Pro/Ultra & Veo](https://www.hooked.so/compare/veo-3-pricing)
- [n8n pricing 2026](https://sliplane.io/blog/n8n-pricing) · [Suno pricing 2026](https://gptprompts.ai/suno-pricing)
- [Recraft V4 vector](https://invideo.io/blog/recraft-ai-image-generator/)
- [Creative MCP servers (ElevenLabs, fal, Figma, Canva, Higgsfield)](https://www.wireflow.ai/blog/best-ai-image-generation-mcp-tools-in-2026) · [ElevenLabs MCP](https://elevenlabs.io/mcp)
- [Claude Code orchestration patterns](https://thepromptshelf.dev/blog/claude-code-multi-agent-orchestration-patterns-2026/)
