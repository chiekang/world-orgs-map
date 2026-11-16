# Extras schema: meetings, hot topics, timeline

Today: 2026-11-16 (Asia/Taipei). Your training knowledge ends mid-2026: verify everything by web search,
official sources first (organization websites, host-government sites), then reputable news (Reuters, AP,
FT, Bloomberg, Nikkei, BBC, official press releases). Never invent dates or events.

Write one file per organization: `/home/claude/orgmap/data/extras/<id>.json`
(ids: g7 g20 apec oecd wto brics rcep cptpp usmca opec un nato eu sco asean au arab_league mercosur imf aiib taiwan_allies)

```json
{
  "id": "g20",
  "next_meeting": {
    "name": { "en": "G20 Leaders' Summit 2026", "zh": "2026 年 G20 領袖峰會" },
    "date_start": "2026-12-14",          // YYYY-MM-DD; if only month known use "2027-06" and set "date_precision": "month"
    "date_end": "2026-12-15",
    "date_precision": "day",             // "day" | "month" | "year"
    "city": { "en": "Doral (Miami), Florida", "zh": "美國佛羅里達州多拉爾（邁阿密）" },
    "country_iso3": "USA",
    "lat": 25.82, "lon": -80.35,
    "level": "leaders",                  // leaders | ministers | general_assembly | other — prefer the highest-level regular meeting
    "confirmed": true,                   // false if dates/venue are only reported/expected
    "source": "https://..."
  },
  "hot_topics": [
    {
      "title":   { "en": "Short headline (≤ 10 words)", "zh": "短標題" },
      "summary": { "en": "One or two plain sentences for university students.", "zh": "一到兩句白話。" },
      "question": { "en": "One discussion question for class.", "zh": "一個課堂討論問題。" },
      "date": "2026-10",                 // YYYY-MM or YYYY-MM-DD of the news
      "url": "https://source"
    }
  ],
  "timeline": [
    { "year": "1999", "text": { "en": "Short event (≤ 15 words)", "zh": "簡短事件" } }
  ]
}
```

Rules
- `next_meeting`: the NEXT upcoming major meeting AFTER 2026-11-16 (summit / leaders' meeting / ministerial
  conference / annual meeting). If one is happening right now, it counts. If no date is known, give the
  host and month/year with `date_precision` and `confirmed:false`. Use `null` only if nothing is known
  (e.g. taiwan_allies has no meetings — use null). lat/lon = host city coordinates.
- `hot_topics`: 2–3 items, ideally from the last ~6 months (May–Nov 2026), relevant to global business /
  economics / geopolitics. Neutral, factual wording; no opinions. Each must have a real URL you opened or
  saw in search results.
- `timeline`: 5–8 milestones from founding to 2026, most important ones (enlargements, name changes,
  key agreements, withdrawals). Years as strings.
- zh = Traditional Chinese, Taiwan usage. Validate JSON with python3.
