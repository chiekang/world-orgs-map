# Data schema for the "International Organizations World Map" teaching web page

Today's date: 2026-11-16 (Asia/Taipei). Membership must be CURRENT as of today.
Your own knowledge may be outdated (cutoff mid-2026) — always verify with web search,
preferring the organization's OFFICIAL website, then government / reputable news sources.
Check specifically for changes in 2025–2026 (new members, withdrawals, suspensions, reinstatements).

## One JSON file per organization: `data/orgs/<id>.json`

```json
{
  "id": "g7",
  "abbr": "G7",
  "name": { "en": "Group of Seven", "zh": "七大工業國組織" },
  "category": "economic",          // one of: economic | political_security | regional | financial | other
  "founded": "1975",               // year (string)
  "headquarters": { "en": "No permanent secretariat (rotating presidency)", "zh": "無常設秘書處（輪值主席國）" },
  "nature": { "en": "Informal intergovernmental forum", "zh": "非正式政府間論壇" },
  "purpose": { "en": "1–2 plain sentences a university student understands.", "zh": "一到兩句白話說明。" },
  "as_of": "2026-11-16",
  "members": [
    { "iso3": "USA", "status": "member", "joined": "1975" },
    { "iso3": "TWN", "status": "member", "official_name": "Chinese Taipei", "note": "..." }
  ],
  "non_state_members": [
    { "name": { "en": "European Union", "zh": "歐盟" }, "status": "member", "note": "Non-enumerated member" }
  ],
  "status_labels": {
    "member":   { "en": "Member",   "zh": "正式成員" },
    "observer": { "en": "Observer", "zh": "觀察員" }
  },
  "sources": ["https://official-site/members", "https://..."],
  "notes": ["Any ambiguity, recent change, or judgement call — with date and source."]
}
```

### Rules
- `iso3`: ISO 3166-1 alpha-3. Special codes: Taiwan `TWN`, Kosovo `XKX`, Palestine `PSE`,
  Hong Kong `HKG`, Macao `MAC`, Western Sahara / Sahrawi Republic `ESH`, Vatican/Holy See `VAT`.
- `status` values (use only those the organization actually has):
  `member`, `observer`, `dialogue_partner`, `partner`, `associate`, `candidate`,
  `acceding` (accession in progress), `suspended` (member whose participation is suspended),
  `prospective` (e.g. AIIB prospective member), `permanent_guest`.
  Every status you use must appear in `status_labels` with en + zh (Traditional Chinese).
- Only include entities that are countries/territories (with an iso3) in `members`.
  Supranational bodies (EU, African Union, etc.) go in `non_state_members`.
- `official_name`: include ONLY when the organization uses a name different from the common
  English country name (e.g. Taiwan = "Chinese Taipei" in APEC; WTO = "Separate Customs Territory
  of Taiwan, Penghu, Kinmen and Matsu (Chinese Taipei)"; Hong Kong = "Hong Kong, China").
- `zh` = Traditional Chinese as used in Taiwan (e.g. 東協, 上海合作組織, 北大西洋公約組織).
- `joined` is optional but nice to have (year).
- Write valid JSON (no comments). Validate with `python3 -c "import json;json.load(open(PATH))"`.

## Country reference file: `data/countries.json` (separate agent)

```json
{
  "as_of": "2026-11-16",
  "gdp_source": "...", "population_source": "...",
  "countries": [
    { "iso3": "JPN", "iso2": "JP", "iso_numeric": "392",
      "name": { "en": "Japan", "zh": "日本" },
      "gdp_usd": 4.03e12, "gdp_year": 2025,
      "population": 123800000, "pop_year": 2025 }
  ]
}
```
