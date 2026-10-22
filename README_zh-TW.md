<div align="center">

<a href="https://evolink.ai?utm_source=github&utm_medium=banner&utm_campaign=gemini-4-carbon-usecases&utm_content=readme-cover"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/banner/banner-b55a8eaa373d.svg" alt="Gemini 4 Carbon — 社群使用案例" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

[![English](https://img.shields.io/badge/English-2563eb)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-2563eb)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-2563eb)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-2563eb)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-2563eb)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-2563eb)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-2563eb)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-2563eb)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-2563eb)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-2563eb)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-2563eb)](README_ru.md)

</div>

## 🍌 介紹

收集創作者在早期灰度階段公開分享、並標示為 Gemini 4 Carbon 的社群展示。

**透過原始來源了解具體任務、可見產物和實際限制。**

## 📊 概覽

共 25 個 usecase，涵蓋 5 類。轉載歸併到對應作品；既有產物的比較附在原案例內。

> [!NOTE]
> 型號、生成耗時及品質判斷均來自來源自述。Arena 顯示名稱不能證明後端版本，錄影也不能證明程式碼可執行、完整互動正確或結果可重現。

<a id="quick-start"></a>
## ⚡ 快速開始

1. 在目錄選擇任務。
2. 開啟影片或圖片，再透過案例標題前往原文。
3. 對照任務與限制判斷可見結果。

## 📑 目錄

| 案例 | 分類 | 類型 |
|---|---|---|
| [1. 機械花](#case-1) | 機械與三維物體 | Demo |
| [2. 機械蜜蜂](#case-2) | 機械與三維物體 | Demo |
| [3. 機械生物與蛛網](#case-3) | 機械與三維物體 | Demo |
| [4. 水晶柑橘](#case-4) | 機械與三維物體 | Demo |
| [5. 霍格華茲體素建築](#case-5) | 體素世界與風景 | Demo |
| [6. 體素城堡風景](#case-6) | 體素世界與風景 | Demo |
| [7. 富士花園](#case-7) | 體素世界與風景 | Demo |
| [8. 體素河流與天氣](#case-8) | 體素世界與風景 | Demo |
| [9. 體素寶塔](#case-9) | 體素世界與風景 | Demo |
| [10. 五重體素塔](#case-10) | 體素世界與風景 | Demo |
| [11. 體素燈塔島](#case-11) | 體素世界與風景 | Demo |
| [12. 機械海怪模型](#case-12) | 體素世界與風景 | Demo |
| [13. 雲上列車城市](#case-13) | 體素世界與風景 | Demo |
| [14. 可樂瓶 SVG](#case-14) | SVG 與互動圖形 | Demo |
| [15. 互動 PS5 手把](#case-15) | SVG 與互動圖形 | Demo |
| [16. Xbox 風格手把](#case-16) | SVG 與互動圖形 | Demo |
| [17. 跑車 SVG](#case-17) | SVG 與互動圖形 | Demo |
| [18. 夕陽海岸鵜鶘騎行](#case-18) | SVG 與互動圖形 | Demo |
| [19. 四季鵜鶘騎行](#case-19) | SVG 與互動圖形 | Demo |
| [20. 淡彩鵜鶘騎行](#case-20) | SVG 與互動圖形 | Demo |
| [21. 海港鵜鶘與 UI 限制](#case-21) | SVG 與互動圖形 | Limit |
| [22. 瑪利歐風格平台遊戲](#case-22) | 遊戲與動畫場景 | Demo |
| [23. 方塊世界沙盒](#case-23) | 遊戲與動畫場景 | Demo |
| [24. 青蛙滑板場景](#case-24) | 遊戲與動畫場景 | Demo |
| [25. 三模型騎行動畫比較](#case-25) | 模型比較 | Evaluation |

## ⚙️ 機械與三維物體

<a id="case-1"></a>
### 案例 1: [機械花](https://x.com/thtbee_/status/2112935205703147750) (作者 [@thtbee_](https://x.com/thtbee_))

**觀察 three.js 花朵的材質、光照變化及小蜜蜂。**

創作者自述耗時約 1 小時 43 分鐘，並稱開放式要求促使模型加入蜜蜂。耗時未經獨立測量。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112929911149371392-e21290e5e3a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112929911149371392-e771176b9f52.jpg" alt="機械花 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-2"></a>
### 案例 2: [機械蜜蜂](https://x.com/thtbee_/status/2112971691966267827) (作者 [@thtbee_](https://x.com/thtbee_))

**觀察機械蜜蜂動畫與八字形運動。**

創作者稱精細度較 Argon 改善，並引用舊版測試；沒有統一計時或成功率資料。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112971150624276481-08802f1fd200.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112971150624276481-37af1edb658b.jpg" alt="機械蜜蜂 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-3"></a>
### 案例 3: [機械生物與蛛網](https://x.com/hakmgpt/status/2112999946777719116) (作者 [@hakmgpt](https://x.com/hakmgpt))

**觀看機械生物、蛛網及帶翼裝置的多場景影片。**

三個抽樣畫格顯示不同場景。簡短正文沒有說明提示詞、流程，或是否來自同一次生成。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112997765458309120-c7d3c185b9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112997765458309120-bc5f3191664e.jpg" alt="機械生物與蛛網 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-4"></a>
### 案例 4: [水晶柑橘](https://x.com/pankajkumar_dev/status/2112946681977430469) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**觀察柑橘模型的分層、光照及動畫視角。**

作者自述約 20 分鐘，Arena 顯示 gemini-4-argon；實際為 Carbon 是作者的判斷。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112945233822617600-6e32038ca6b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112945233822617600-ada2f593eab5.jpg" alt="水晶柑橘 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

## 🏞️ 體素世界與風景

<a id="case-5"></a>
### 案例 5: [霍格華茲體素建築](https://x.com/dummerspast39/status/2112989454239416450) (作者 [@dummerspast39](https://x.com/dummerspast39))

**從內外視角觀察體素城堡。**

來源明確標示 best of 4。這是四次中挑選的結果，不能證明首次成功。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112989347301519360-99b7308b4b0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112989347301519360-42c02806db71.jpg" alt="霍格華茲體素建築 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-6"></a>
### 案例 6: [體素城堡風景](https://x.com/Mr_Salio/status/2112856590386643413) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**觀察城堡的白天、夜間及俯瞰視角。**

媒體展示另一份城堡產物。發布者與 Opus 的比較屬於觀點，沒有統一基準或生成過程。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112856348719210496-a57ed12eb899.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112856348719210496-b6b5dc0a31f6.jpg" alt="體素城堡風景 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-7"></a>
### 案例 7: [富士花園](https://x.com/doe_naps/status/2112975635337593132) (作者 [@doe_naps](https://x.com/doe_naps))

**探索微縮日式花園及蝴蝶視角。**

來源描述反射、活動人物及微縮世界。抽樣畫格顯示多個視角，未測試全部互動。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112972423893221376-421aa3046fa3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112972423893221376-a5bc633b97f3.jpg" alt="富士花園 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-8"></a>
### 案例 8: [體素河流與天氣](https://x.com/abhinavflac/status/2112910206644756745) (作者 [@abhinavflac](https://x.com/abhinavflac))

**觀察體素河谷的反射及天氣變化。**

作者稱耗時為 Argon 的 2–3 倍；這是一份沒有統一計時協定的個人比較。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112909984925372417-c80bf67ccd5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112909984925372417-5998d70a68db.jpg" alt="體素河流與天氣 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-9"></a>
### 案例 9: [體素寶塔](https://x.com/LuminaBench/status/2112822997161562600) (作者 [@LuminaBench](https://x.com/LuminaBench))

**觀察寶塔浮島在多種光照下的細節。**

創作者稱依任務不同，耗時為 Argon 的 2–4 倍，不代表整個型號的統一延遲。同一作者另將這座寶塔與其他三份模型輸出比較；保留原標籤並附於此處，不另計一次 Carbon 生成。

([@LuminaBench](https://x.com/LuminaBench/status/2112829559158800732))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112821820793434112-52372e9a3a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112821820793434112-b673916ea1e4.jpg" alt="體素寶塔 — 1" width="560"></a><br>觀看來源影片</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112827630357516288-060bdc9c31b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112827630357516288-76711181a8a7.jpg" alt="體素寶塔 — 2" width="560"></a><br>觀看原始模型比較</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-10"></a>
### 案例 10: [五重體素塔](https://x.com/Mr_Salio/status/2112890002619142465) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**觀察另一座寶塔的動畫光照及近景。**

影片中的寶塔呈現與 LuminaBench 範例不同。同題材不代表同一次生成。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112889945530445824-a889d183dcfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112889945530445824-be4088fa4d3a.jpg" alt="五重體素塔 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-11"></a>
### 案例 11: [體素燈塔島](https://x.com/LuminaBench/status/2112844170209399118) (作者 [@LuminaBench](https://x.com/LuminaBench))

**觀察燈塔場景的晝夜及天氣變化。**

來源讚許體素細節；抽樣畫格可辨識具體燈塔場景，沒有公開提示詞或程式碼。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112841088444628992-40ce06ef4e5f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112841088444628992-86073f2c1e6c.jpg" alt="體素燈塔島 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-12"></a>
### 案例 12: [機械海怪模型](https://x.com/HarshithLucky3/status/2112882176912158877) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**觀察黃銅機械海怪與潛艇的體素場景。**

來源指定蒸汽龐克海怪、維多利亞潛艇及熱液噴口，並稱顯示為 Argon 的 Arena 檢查點實際為 Carbon。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112881879125053440-ed7a36ad009c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112881879125053440-ef964b2745cf.jpg" alt="機械海怪模型 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-13"></a>
### 案例 13: [雲上列車城市](https://x.com/SPAC89/status/2112849450993336595) (作者 [@SPAC89](https://x.com/SPAC89))

**探索列車、高架軌道及高塔組成的幻想場景。**

具體任務依影片辨識，正文較泛。正文的發布日期預測及模型排名不是該場景的效果證據。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112848304245481472-f855a4ec4d26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112848304245481472-1988e3f7ab74.jpg" alt="雲上列車城市 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

## 🎨 SVG 與互動圖形

<a id="case-14"></a>
### 案例 14: [可樂瓶 SVG](https://x.com/dummerspast39/status/2112999200472596959) (作者 [@dummerspast39](https://x.com/dummerspast39))

**觀察創作者稱為 SVG 的立體可樂瓶展示。**

作者自述在 Arena 耗時約五分鐘。錄影顯示結果，但沒有獨立重現 SVG 實作或與 Opus 的比較。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112998739115651072-36c11d258cd7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112998739115651072-92e3c1a11f11.jpg" alt="可樂瓶 SVG — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-15"></a>
### 案例 15: [互動 PS5 手把](https://x.com/marcthecreatorr/status/2112894985267761333) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**觀察手把 SVG 的近景及不同顯示狀態。**

作者稱等待較久，且 Carbon 顯示為 gemini-4-argon。錄影不能獨立核驗後端型號。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112894899636862976-d5e2bb02aca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112894899636862976-279e5a90cd0e.jpg" alt="互動 PS5 手把 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-16"></a>
### 案例 16: [Xbox 風格手把](https://x.com/Mr_Salio/status/2112842066501816466) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**觀察細節豐富的 Xbox 風格手把渲染。**

來源標示 Carbon，並稱 Arena 顯示為 Argon。後來的資訊文展示同一手把設計，歸併到本案例。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg" alt="Xbox 風格手把 — 1" width="560"></a><br>查看來源圖片</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg" alt="Xbox 風格手把 — 2" width="560"></a><br>查看來源圖片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-17"></a>
### 案例 17: [跑車 SVG](https://x.com/auricxofficial/status/2112902209608597810) (作者 [@auricxofficial](https://x.com/auricxofficial))

**觀察白色跑車側面的輪圈與車身細節。**

圖片展示車輛，關聯測試者稱其為 SVG 測試。正文沒有可執行程式碼，也未證明互動能力。

([@HarshithLucky3](https://x.com/HarshithLucky3/status/2112904832600477960))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg" alt="跑車 SVG — 1" width="560"></a><br>查看來源圖片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-18"></a>
### 案例 18: [夕陽海岸鵜鶘騎行](https://x.com/dummerspast39/status/2112941964819595479) (作者 [@dummerspast39](https://x.com/dummerspast39))

**觀察夕陽海岸背景下的鵜鶘騎車動畫。**

來源稱產物為 SVG，與 LuminaBench 的海港版場景不同；兩者都不視為可重現的程式碼交付。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112941947727785984-a35fd5a8a21a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112941947727785984-ebb464917b8f.jpg" alt="夕陽海岸鵜鶘騎行 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-19"></a>
### 案例 19: [四季鵜鶘騎行](https://x.com/hamoudi_yo/status/2112933636093919333) (作者 [@hamoudi_yo](https://x.com/hamoudi_yo))

**探索鵜鶘騎車的四季畫面。**

來源明確稱為四季 SVG，並稱 Arena 檢查點顯示為 Argon。後端身分仍是來源自述。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112933037528772609-fd19e0c4ed54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112933037528772609-ed8b4e1fd852.jpg" alt="四季鵜鶘騎行 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-20"></a>
### 案例 20: [淡彩鵜鶘騎行](https://x.com/abhinavflac/status/2112825133052428378) (作者 [@abhinavflac](https://x.com/abhinavflac))

**觀察淡彩鵜鶘自行車場景中的翅膀運動。**

作者強調振翅及爪子。與其他鵜鶘測試同題，不代表同一份輸出。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112824858526814208-cadb280b19f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112824858526814208-57282e71a7ce.jpg" alt="淡彩鵜鶘騎行 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-21"></a>
### 案例 21: [海港鵜鶘與 UI 限制](https://x.com/LuminaBench/status/2112830849771004187) (作者 [@LuminaBench](https://x.com/LuminaBench))

**觀察海港鵜鶘 SVG，並考慮可用性及回應時間。**

測試者明確認為 UI 不佳、生成很慢；展示動畫時同時保留這些缺點。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112830075997507584-093a4bc78c90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112830075997507584-5f9cde944578.jpg" alt="海港鵜鶘與 UI 限制 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Limit | 日期: 2026-10-21

---

## 🎮 遊戲與動畫場景

<a id="case-22"></a>
### 案例 22: [瑪利歐風格平台遊戲](https://x.com/LuminaBench/status/2112848294581813473) (作者 [@LuminaBench](https://x.com/LuminaBench))

**觀察平台遊戲的室外及地下區域錄影。**

創作者自述約 30 分鐘、首次成功。錄影不能驗證所有碰撞、關卡規則或重新開始路徑。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112846477709967360-9bcb4df969c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112846477709967360-99c390222b65.jpg" alt="瑪利歐風格平台遊戲 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-23"></a>
### 案例 23: [方塊世界沙盒](https://x.com/Haleeeemahh/status/2112871860094538053) (作者 [@Haleeeemahh](https://x.com/Haleeeemahh))

**觀察附有方塊工具列的 Minecraft 風格第一人稱世界。**

抽樣畫格顯示導航及放置方塊。來源稱其為顯示 Argon 名稱的 Carbon 檢查點，未測試完整遊戲邏輯。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112871560407097344-e1b7609246df.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112871560407097344-37726fd4c849.jpg" alt="方塊世界沙盒 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

<a id="case-24"></a>
### 案例 24: [青蛙滑板場景](https://x.com/SPAC89/status/2112845784500629765) (作者 [@SPAC89](https://x.com/SPAC89))

**觀察風格化場景中青蛙踩滑板的動畫。**

具體任務可從媒體看到，正文較泛。作者對速度的正面感受不是計時測量。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112845628640251904-f1909c90d438.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112845628640251904-700f770e3a57.jpg" alt="青蛙滑板場景 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Demo | 日期: 2026-10-21

---

## 🔬 模型比較

<a id="case-25"></a>
### 案例 25: [三模型騎行動畫比較](https://x.com/AI_Screening/status/2112916947923087364) (作者 [@AI_Screening](https://x.com/AI_Screening))

**對照來源組合展示的 Carbon、Argon 與 GPT-6 Astra 騎行動畫。**

錄影保留模型標籤及對應產物。發布者偏好 Carbon，但沒有提供共同設定、重試次數或執行紀錄。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112916798039642113-7f04c4d03491.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112916798039642113-c1474c749e67.jpg" alt="三模型騎行動畫比較 — 1" width="560"></a><br>觀看來源影片</td></tr></table>

類型: Evaluation | 日期: 2026-10-21

---

<a id="related-repositories"></a>
## 相關儲存庫

- [Gemini 3.6 Flash — 指南與使用案例](https://github.com/Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases)
- [Gemini Omni — 指南與提示詞](https://github.com/Evolink-AI/awesome-gemini-omni-guide-api-and-prompt)

<a id="acknowledge"></a>
## 🙏 致謝

感謝以下公開分享展示的發布者：

[@thtbee_](https://x.com/thtbee_), [@hakmgpt](https://x.com/hakmgpt), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@dummerspast39](https://x.com/dummerspast39), [@Mr_Salio](https://x.com/Mr_Salio), [@doe_naps](https://x.com/doe_naps), [@abhinavflac](https://x.com/abhinavflac), [@LuminaBench](https://x.com/LuminaBench), [@HarshithLucky3](https://x.com/HarshithLucky3), [@SPAC89](https://x.com/SPAC89), [@marcthecreatorr](https://x.com/marcthecreatorr), [@auricxofficial](https://x.com/auricxofficial), [@hamoudi_yo](https://x.com/hamoudi_yo), [@Haleeeemahh](https://x.com/Haleeeemahh), [@AI_Screening](https://x.com/AI_Screening)

署名依據連結來源，可能需要更正。如有遺漏署名、重複作品、表述錯誤或移除需求，請提交 issue。第三方媒體權利歸原權利人。
