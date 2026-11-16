# World of International Organizations｜國際組織世界地圖

輔仁大學全英語課程 **Financial Market and Global Business** 的課堂互動網頁。學生用手機或筆電打開，選擇國際組織，就能在世界地圖上看到成員國。

**網址：** https://chiekang.github.io/world-orgs-map/

## 功能

- **探索：** 21 個組織的成員國地圖。正式成員用深色，其他身分（觀察員、夥伴、候選國、停權）用淺色區分；附宗旨、成立年份、總部、成員占全球 GDP 與人口比重。
- **會議倒數：** 各組織下一次峰會的日期、地點與倒數天數，地圖上用星號標出舉辦城市。
- **最新議題與大事記：** 每個組織 2–3 則近期議題（附課堂討論題與來源），以及 6–8 個歷史里程碑。
- **國家查詢：** 點國家或用搜尋框，查看國旗、GDP、人口，以及該國參加的所有組織。台灣依各組織官方會籍名稱顯示（如 APEC 的 Chinese Taipei）。
- **比較：** 最多 3 個組織疊加比較，另有 G7 vs BRICS、NATO vs SCO、CPTPP vs RCEP 等一鍵對照。
- **排行榜：** 最愛入會的國家、各組織經濟實力比較。
- **測驗：** 經典題、60 秒挑戰、猜猜我是誰。
- 中英文切換；所有資料、地圖與國旗都內建在單一 HTML 檔，不依賴外部網路。

收錄組織：G7、G20、APEC、OECD、WTO、BRICS、RCEP、CPTPP、USMCA、OPEC、UN、NATO、EU、SCO、ASEAN、AU、阿拉伯聯盟、Mercosur、IMF、AIIB、台灣邦交國。

## 資料

資料更新日期：2026-11-16。成員名單、會議與議題由多組研究智能體查證官方來源，再由獨立檢核智能體比對，紀錄見 `data/VERIFICATION.md`。

| 檔案 | 內容 |
|---|---|
| `data/orgs/<id>.json` | 各組織成員名單、身分、簡介、來源 |
| `data/extras/<id>.json` | 下一次會議、最新議題、大事記 |
| `data/countries.json` | 各國中英文名、GDP（IMF WEO 2026 年 10 月版）、人口 |

## 更新網頁

修改 `data/` 或 `src/template.html` 後重新打包：

```bash
npm install
python3 build.py   # 產生 index.html
```

把新的 `index.html` 推上 GitHub，GitHub Pages 會自動更新。
