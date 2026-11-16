# 資料查核紀錄（2026-11-16，獨立查核）

## 一、檢查項目
- **機械檢查（Python）**：21 個組織檔與 countries.json 皆為有效 JSON；各組織內 iso3 無重複；所用 status（含 non_state_members）皆有中英文標籤；以 OpenCC 檢查所有 zh 字串，**未發現簡體字**（標出的「秘、台、群、占」等皆為台灣正體常用寫法）；國名中文符合台灣用法。
- **成員數（與官方總數相符）**：UN 193＋2 觀察員（教廷、巴勒斯坦）；WTO 165 國家／關稅領域＋歐盟＝166（CRS 2026-09-24 確認仍為 166）；IMF 191＝UN 會員國扣除古巴、北韓、摩納哥，加上科索沃（集合比對完全一致）；NATO 32；EU 27＋9 候選國＋科索沃；AU 55（49＋6 停權）；阿拉伯聯盟 22；APEC 21；ASEAN 11；RCEP 15；CPTPP 12；G7 7；G20 19＋EU＋AU；OECD 38＋8 入會中；SCO 10；AIIB 106＋5 準會員＝111（aiib.org 顯示 111 approved members）；台灣邦交國 12。
- **重點事實查核**：UAE 退出 OPEC／OPEC+（WAM 官方公告，2026-05-01 生效）✔；BRICS 夥伴國 10 國、新德里峰會未新增 ✔；ASEAN 東帝汶 2025-10 入會、土耳其 2026-07 成為對話夥伴（asean.org）✔；AU 幾內亞 2026-01 恢復、加彭 2025 恢復，馬達加斯加、幾內亞比索等 6 國停權 ✔；CPTPP 哥斯大黎加 2026-05-06 實質完成談判但尚非締約方 ✔；OECD 羅馬尼亞尚未獲正式邀請 ✔；SCO「夥伴」新制度尚未生效，維持觀察員／對話夥伴分類 ✔；APEC「Chinese Taipei」、WTO 全稱正確 ✔。
- **GDP／人口抽查**：22 國（ARG, AUS, BRA, CHN, DEU, EGY, FRA, HKG, IDN, IND, JPN, KAZ, KEN, MEX, NGA, PER, POL, TUV, TWN, USA, VNM, ZAF）GDP 與 IMF DataMapper 2025 值完全一致；其中 17 國人口亦逐一核對一致。

## 二、修改內容
| 檔案 | 修改前 → 修改後 | 來源 |
|---|---|---|
| countries.json | 缺 COK → 新增庫克群島（AIIB 區域會員，2017 核准）；GDP／人口無 IMF、WB 資料，設 null | https://www.aiib.org/en/news-events/news/2017/AIIB-Approves-Membership-of-Cook-Islands-Vanuatu-Belarus-and-Ecuador.html |
| countries.json | 缺 CUW → 新增古拉索（WTO 觀察員）；GDP 35.6 億美元（2024）、人口 156,263（2025） | https://api.worldbank.org/v2/country/CUW/indicator/NY.GDP.MKTP.CD?format=json&mrnev=1 |
| orgs/g20.json | 西班牙 permanent_guest 無來源 → 保留，補 CRS 來源與說明（2010 年起為永久受邀國，美方已邀請出席 2026 年 12 月峰會） | https://www.everycrsreport.com/files/2026-11-04_R40977_5b77624b091e5f2cbe2d28c9dc42fcc4e78a395d.html |
| orgs/opec.json | 僅有新聞來源 → 加入 UAE 官方通訊社 WAM 公告 | https://www.wam.ae/en/article/bzxzuh7-uae-announces-decision-exit-opec |
| orgs/asean.json | 補上經確認的東協–土耳其對話夥伴概覽 PDF（2026/08 路徑） | https://asean.org/wp-content/uploads/2026/08/Overview-ASEAN-Turkiye-Dialogue-Partnership_ao-August-2026.pdf |

各組織成員名單**未做任何增刪**（查核未發現確定錯誤）。

## 三、老師需留意的不確定處
1. **沙烏地阿拉伯是否為 BRICS 正式成員**：BRICS 官方列為成員，但利雅德從未正式確認，建議上課時說明此爭議。
2. **南非與 G20**：仍為正式成員，但 2026 年美國主辦時未受邀；屬主辦國決定，非組織除名。
3. **OPEC**：UAE 已退出，但據報 opec.org 一度仍列 UAE；OPEC+「夥伴」分類（含巴西）為教學上的判斷。
4. **SCO**：2025 年天津峰會決議將觀察員與對話夥伴合併為「上合組織夥伴」，修約尚未確認生效，日後可能需改標籤。
5. **變動中事項**：CPTPP 哥斯大黎加可能在年底委員會後正式加入；OECD 羅馬尼亞可能隨時獲邀；委內瑞拉南方共同市場停權、AU 停權名單、USMCA 年度審查皆可能變動。
6. G20 檔案提到美國邀請波蘭為來賓，CRS 報告未提及，未能證實（未刪除）。
7. 庫克群島無 GDP／人口數據（地圖上會顯示為空值）。

## 會議、議題、大事記檢核

檢核日：2026-11-16（台北時間）。以網路搜尋與開啟原始網頁逐項核對 `data/extras/*.json`。全部 21 檔皆為有效 JSON、必要欄位齊全；以 OpenCC 檢查 zh 欄位，未發現簡體字（僅「台/臺」「峰/峯」等異體字差異，屬台灣正常用法）。

### 一、next_meeting 修改

| 檔案 | 修改前 → 修改後 | 來源 |
|---|---|---|
| aiib.json | 2027、`year`、城市「可能為巴庫」、confirmed:false → **2027-07-14～15、`day`、巴庫、confirmed:true** | AIIB 官方新聞稿（理事會於杜哈第 11 屆年會決定）：https://aiib.org/en/news-events/news/2026/azerbaijan-to-host-aiib-12th-annual-meeting-in-2027.html |
| cptpp.json | 2026-11-26、`day` → **2026-11、`month`**（仍 confirmed:false） | 11/26 只是河內 CPTPP–東協–歐盟商業論壇日期，執委會本身日期未公布：https://trungtamwto.vn/su-kien/33909-moi-tham-du-dien-dan-doanh-nghiep-cptpp-asean-eu-2026 |
| oecd.json | 2027-06、`month` → **2027、`year`** | 捷克代表團網頁只說捷克擔任 2027 年 MCM 主席，沒有月份；「6 月」是依慣例推估：https://mzv.gov.cz/oecd.paris/en/news/index.html |
| asean.json | 日期不變（11/15–17）；**新增 note**：馬尼拉宣布 11/16–18 為峰會特別放假日 | Bernama／The Star 寫 15–17 日；Philstar 寫放假日為 16–18 日 |
| arab_league.json | **新增 note**：下屆例行峰會主辦國與日期未公布；無法證實 2026 年第 35 屆例行峰會是否已舉行 | 搜尋未找到 2026 年例行峰會的報導 |

已確認、未修改：APEC 深圳 11/18–19（龍崗區政府、Focus Taiwan）；COP31 安塔利亞 11/9–20（UNFCCC 官網）；歐洲理事會 12/17–18（理事會 ST-10983-2026 議程文件、官方行事曆）；G20 Doral 12/14–15（CRS 報告 2026-11-04）；OPEC+ 第 42 屆 ONOMM 11/29（OPEC 2026-06-07 新聞稿第 8 點；形式／地點未說明，維持 confirmed:true 加 note）；SCO 伊斯蘭堡 2027-09（僅 Friday Times 報導，維持 month／false）；NATO 地拉那 2027（日期未定，year／false）；Mercosur 烏拉圭 2026-12（MercoPress 只說 12 月，month／false）；RCEP 新加坡 2027（推測，year／false；第 5 屆部長會議已於 2026-09-21 在馬尼拉舉行，CGTN）；WTO 總理事會 2026-12（推估，month／false）；IMF 2027 春季會議（month／false；官方尚未公布日期）；AU 2027-02（month／false）；G7 2027 美國（year／false）；BRICS 2027 中國（year／false）；USMCA 2027-07（month／false）。

### 二、hot_topics 修改

| 檔案 | 修改前 → 修改後 | 原因／來源 |
|---|---|---|
| arab_league.json #1 | 「法赫米自 2026-07-01 起任期五年」→ 「2026 年 6 月成員一致通過法赫米出任秘書長，接替阿布蓋特」 | The National 原文沒有寫上任日期與任期長度 |
| arab_league.json #2 | Euronews 影片頁（內容與標題不符），且摘要寫「擾亂荷莫茲海峽航運」→ 改用 Al Jazeera 2026-03-18 報導：伊朗飛彈造成拉斯拉凡受損，卡達下令伊朗使館武官與安全官員 24 小時內離境；刪去荷莫茲一句 | https://www.aljazeera.com/news/2026/3/18/qatar-says-iran-missile-attack-sparks-fire-causes-damage-at-gas-facility |
| asean.json #2 | mb.com.ph 連結無法開啟（原本只依搜尋標題撰寫）→ 改用 The Star 2026-07-12 報導，摘要改為「菲律賓作為主席國，希望東協與中國在年內完成南海行為準則」 | https://www.thestar.com.my/aseanplus/aseanplus-news/2026/07/12/philippines-urges-effective-south-china-sea-coc-amid-persistent-tensions |
| cptpp.json #1 | 「大致完成；將成為首個新加入的拉美國家」→ 「完成入會工作小組談判，成為下一個準備加入的國家」 | GOV.UK 頁面沒有「首個拉美新成員」的說法（墨西哥、秘魯、智利本來就是創始成員） |
| un.json #2 | 「自 2026 年 7 月起舉行非正式投票」→ 刪除起始月份；保留「葛林斯潘在 9 月底第四輪投票中領先」 | The National 報導沒有寫第一輪的日期 |
| un.json #1 | 「調適資金是**核心**爭議」→「**主要爭議之一**」 | Balkan Green Energy News 原文用 "one of the key issues" |
| wto.json #3 | 刪除「沙烏地阿拉伯已提議於 2028 年主辦」（該連結原文未提）；改為「尋求通往第 15 屆部長會議更清楚的路線圖」 | worldtradescanner 2026-10-27 原文；沙國的提議是 2025-12 的另一則新聞 |
| eu.json #1 | 「蒙特內哥羅目標 2026 年底完成談判」→「可望於年底前暫時結束其餘談判章節」 | European Western Balkans 原文 |
| eu.json #3 | 刪除「目標在 2026 年底前達成協議」 | 原文只說領袖會討論 2028–2034 年長期預算，沒有寫期限 |
| mercosur.json #1 | 「汽車、葡萄酒、牛肉」→「汽車、葡萄酒、橄欖油」 | 歐盟執委會新聞稿沒有提到牛肉降稅 |
| mercosur.json #2 | 「正式啟動經濟夥伴協定（EPA）談判」→「宣布啟動與日本的貿易談判」 | MercoPress 原文 |
| mercosur.json #3 | 「推動與 EFTA、加拿大、阿聯的協定」→「推進與加拿大、阿聯的談判，加強與 EFTA 的關係」 | MercoPress 原文 |
| taiwan_allies.json #3 | 「台灣現存最大邦交國」→「台灣在南美洲唯一的邦交國」 | Free Malaysia Today 原文；「最大」的標準不明（論人口瓜地馬拉較多） |
| brics.json #1 | 《德里宣言》→《新德里宣言》（以共識通過） | Open Magazine 原文 |

已開啟原文核對、未修改：IMF 2026 年 10 月 WEO 摘要（2026 年全球成長 3.1%，主要因素為中東衝突帶動能源價格、貿易緊張、AI 投資）；Eswatini 一則（賴總統延後 4/22–26 訪問行程，因塞席爾、模里西斯、馬達加斯加撤回飛越許可，官方指稱遭中國施壓；報導稱史瓦帝尼為台灣在非洲僅存的邦交國）；NATO 安卡拉峰會兩則；USMCA 三則；SCO 比斯凱克兩則；OPEC 三則；OECD 三則；G7 關鍵礦產；AIIB 兩則；APEC Focus Taiwan、China Global South；AU 第 39 屆峰會；IMF 曼谷年會；Honduras 一則；EU–Mercosur 暫行適用；COP31。

### 三、timeline 修改

| 檔案 | 修改前 → 修改後 | 來源 |
|---|---|---|
| taiwan_allies.json 1969 | 「約 70 國，接近高峰」→「達 70 國，為歷史高峰」 | 公視新聞網 https://news.pts.org.tw/article/627439 |
| taiwan_allies.json 1990 | 「回升至約 28 國」（無來源）→「李登輝務實外交（1988–2000 年）使邦交國回升，最多達 31 國」 | 同上公視報導（1979–1988 維持 22 國，李登輝時期最多 31 國，2000 年卸任時 29 國）；關鍵評論網也寫「最多達 31 國」 |

其他抽查無誤：RCEP（2017 年馬尼拉首次領袖會議、2025 年吉隆坡第 5 屆峰會 = 2025-10-27）、台灣邦交國 2016＝22、2019＝15、2023＝13、2024＝12。

### 四、仍待確認

1. ASEAN 第 49 屆峰會確切日期：新聞稿寫 11/15–17，越通社一則寫 11/14–17，放假日則是 11/16–18。
2. CPTPP 第 11 屆執委會的確切日期與城市（目前推定為 11 月在越南，可能是河內 11/26 前後）。
3. 阿拉伯聯盟 2026 年例行峰會是否已舉行，以及 2027 年的主辦國。
4. OPEC+ 11/29 會議採實體或視訊。
5. SCO 2027「9 月」只有媒體報導；NATO 2027 地拉那尚無日期。
6. 部分報導因付費牆或網站阻擋無法讀全文（SCMP APEC 一則、Modern Diplomacy G20／G7 兩則），只能以搜尋結果標題核對，摘要與標題相符，予以保留。
