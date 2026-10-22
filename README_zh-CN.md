<div align="center">

<a href="https://evolink.ai?utm_source=github&utm_medium=banner&utm_campaign=gemini-4-carbon-usecases&utm_content=readme-cover"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/banner/banner-b55a8eaa373d.svg" alt="Gemini 4 Carbon — 社区使用案例" width="760"></a>

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

## 🍌 介绍

收集创作者在早期灰度阶段公开分享、并标注为 Gemini 4 Carbon 的社区演示。

**通过原始来源了解具体任务、可见产物和实际限制。**

## 📊 概览

共 25 个 usecase，覆盖 5 类。转载归并到对应作品；已有产物的对比附在原案例内。

> [!NOTE]
> 型号、生成耗时和质量判断均来自来源自述。Arena 显示名称不能证明后台版本，录屏也不能证明代码可运行、完整交互正确或结果可重复。

<a id="quick-start"></a>
## ⚡ 快速开始

1. 在目录选择任务。
2. 打开视频或图片，再通过案例标题访问原帖。
3. 对照任务与限制判断可见结果。

## 📑 目录

| 案例 | 分类 | 类型 |
|---|---|---|
| [1. 机械花](#case-1) | 机械与三维物体 | Demo |
| [2. 机械蜜蜂](#case-2) | 机械与三维物体 | Demo |
| [3. 机械生物与蛛网](#case-3) | 机械与三维物体 | Demo |
| [4. 水晶柑橘](#case-4) | 机械与三维物体 | Demo |
| [5. 霍格沃茨体素建筑](#case-5) | 体素世界与风景 | Demo |
| [6. 体素城堡风景](#case-6) | 体素世界与风景 | Demo |
| [7. 富士花园](#case-7) | 体素世界与风景 | Demo |
| [8. 体素河流与天气](#case-8) | 体素世界与风景 | Demo |
| [9. 体素宝塔](#case-9) | 体素世界与风景 | Demo |
| [10. 五重体素塔](#case-10) | 体素世界与风景 | Demo |
| [11. 体素灯塔岛](#case-11) | 体素世界与风景 | Demo |
| [12. 机械海怪模型](#case-12) | 体素世界与风景 | Demo |
| [13. 云上列车城市](#case-13) | 体素世界与风景 | Demo |
| [14. 可乐瓶 SVG](#case-14) | SVG 与交互图形 | Demo |
| [15. 交互 PS5 手柄](#case-15) | SVG 与交互图形 | Demo |
| [16. Xbox 风格手柄](#case-16) | SVG 与交互图形 | Demo |
| [17. 跑车 SVG](#case-17) | SVG 与交互图形 | Demo |
| [18. 夕阳海岸鹈鹕骑行](#case-18) | SVG 与交互图形 | Demo |
| [19. 四季鹈鹕骑行](#case-19) | SVG 与交互图形 | Demo |
| [20. 淡彩鹈鹕骑行](#case-20) | SVG 与交互图形 | Demo |
| [21. 海港鹈鹕与 UI 局限](#case-21) | SVG 与交互图形 | Limit |
| [22. 马里奥风格平台游戏](#case-22) | 游戏与动画场景 | Demo |
| [23. 方块世界沙盒](#case-23) | 游戏与动画场景 | Demo |
| [24. 青蛙滑板场景](#case-24) | 游戏与动画场景 | Demo |
| [25. 三模型骑行动画对比](#case-25) | 模型对比 | Evaluation |

## ⚙️ 机械与三维物体

<a id="case-1"></a>
### 案例 1: [机械花](https://x.com/thtbee_/status/2112935205703147750) (作者 [@thtbee_](https://x.com/thtbee_))

**观察 three.js 花朵的材质、光照变化及小蜜蜂。**

创作者自述耗时约 1 小时 43 分钟，并称开放式要求促使模型加入蜜蜂。耗时未经独立测量。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112929911149371392-e21290e5e3a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112929911149371392-e771176b9f52.jpg" alt="机械花 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-2"></a>
### 案例 2: [机械蜜蜂](https://x.com/thtbee_/status/2112971691966267827) (作者 [@thtbee_](https://x.com/thtbee_))

**观察机械蜜蜂动画与八字形运动。**

创作者称精细度较 Argon 改善，并引用旧版测试；没有统一计时或成功率数据。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112971150624276481-08802f1fd200.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112971150624276481-37af1edb658b.jpg" alt="机械蜜蜂 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-3"></a>
### 案例 3: [机械生物与蛛网](https://x.com/hakmgpt/status/2112999946777719116) (作者 [@hakmgpt](https://x.com/hakmgpt))

**观看机械生物、蛛网和带翼装置的多场景视频。**

三个抽样帧显示不同场景。简短正文没有说明提示词、流程，或是否来自同一次生成。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112997765458309120-c7d3c185b9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112997765458309120-bc5f3191664e.jpg" alt="机械生物与蛛网 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-4"></a>
### 案例 4: [水晶柑橘](https://x.com/pankajkumar_dev/status/2112946681977430469) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**观察柑橘模型的分层、光照与动画视角。**

作者自述约 20 分钟，Arena 显示 gemini-4-argon；实际为 Carbon 是作者的判断。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112945233822617600-6e32038ca6b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112945233822617600-ada2f593eab5.jpg" alt="水晶柑橘 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

## 🏞️ 体素世界与风景

<a id="case-5"></a>
### 案例 5: [霍格沃茨体素建筑](https://x.com/dummerspast39/status/2112989454239416450) (作者 [@dummerspast39](https://x.com/dummerspast39))

**从内外视角观察体素城堡。**

来源明确标注 best of 4。这是四次中挑选的结果，不能证明首试成功。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112989347301519360-99b7308b4b0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112989347301519360-42c02806db71.jpg" alt="霍格沃茨体素建筑 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-6"></a>
### 案例 6: [体素城堡风景](https://x.com/Mr_Salio/status/2112856590386643413) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**观察城堡的白天、夜间及俯瞰视角。**

媒体展示另一份城堡产物。发布者与 Opus 的比较属于观点，没有统一基准或生成过程。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112856348719210496-a57ed12eb899.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112856348719210496-b6b5dc0a31f6.jpg" alt="体素城堡风景 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-7"></a>
### 案例 7: [富士花园](https://x.com/doe_naps/status/2112975635337593132) (作者 [@doe_naps](https://x.com/doe_naps))

**探索微缩日式花园及蝴蝶视角。**

来源描述反射、活动人物和微缩世界。抽帧显示多个视角，未测试全部交互。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112972423893221376-421aa3046fa3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112972423893221376-a5bc633b97f3.jpg" alt="富士花园 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-8"></a>
### 案例 8: [体素河流与天气](https://x.com/abhinavflac/status/2112910206644756745) (作者 [@abhinavflac](https://x.com/abhinavflac))

**观察体素河谷的反射和天气变化。**

作者称耗时为 Argon 的 2–3 倍；这是一份没有统一计时协议的个人对比。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112909984925372417-c80bf67ccd5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112909984925372417-5998d70a68db.jpg" alt="体素河流与天气 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-9"></a>
### 案例 9: [体素宝塔](https://x.com/LuminaBench/status/2112822997161562600) (作者 [@LuminaBench](https://x.com/LuminaBench))

**观察宝塔浮岛在多种光照下的细节。**

创作者称视任务不同，耗时为 Argon 的 2–4 倍，不代表整个型号的统一延迟。同一作者还把这座宝塔与另外三份模型输出对比；保留原标签，将对比附在这里，不另计一次 Carbon 生成。

([@LuminaBench](https://x.com/LuminaBench/status/2112829559158800732))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112821820793434112-52372e9a3a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112821820793434112-b673916ea1e4.jpg" alt="体素宝塔 — 1" width="560"></a><br>观看来源视频</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112827630357516288-060bdc9c31b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112827630357516288-76711181a8a7.jpg" alt="体素宝塔 — 2" width="560"></a><br>观看原始模型对比</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-10"></a>
### 案例 10: [五重体素塔](https://x.com/Mr_Salio/status/2112890002619142465) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**观察另一座宝塔的动画光照与近景。**

视频中的宝塔呈现与 LuminaBench 的例子不同。同题材不代表同一次生成。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112889945530445824-a889d183dcfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112889945530445824-be4088fa4d3a.jpg" alt="五重体素塔 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-11"></a>
### 案例 11: [体素灯塔岛](https://x.com/LuminaBench/status/2112844170209399118) (作者 [@LuminaBench](https://x.com/LuminaBench))

**观察灯塔场景的昼夜与天气变化。**

来源赞许体素细节；抽帧可识别具体灯塔场景，没有公开提示词或代码。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112841088444628992-40ce06ef4e5f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112841088444628992-86073f2c1e6c.jpg" alt="体素灯塔岛 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-12"></a>
### 案例 12: [机械海怪模型](https://x.com/HarshithLucky3/status/2112882176912158877) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**观察黄铜机械海怪与潜艇的体素场景。**

来源指定蒸汽朋克海怪、维多利亚潜艇和热液喷口，并称显示为 Argon 的 Arena 检查点实际为 Carbon。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112881879125053440-ed7a36ad009c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112881879125053440-ef964b2745cf.jpg" alt="机械海怪模型 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-13"></a>
### 案例 13: [云上列车城市](https://x.com/SPAC89/status/2112849450993336595) (作者 [@SPAC89](https://x.com/SPAC89))

**探索列车、高架轨道和高塔组成的幻想场景。**

具体任务依据视频识别，正文较泛。正文的发布日期预测及模型排名不是该场景的效果证据。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112848304245481472-f855a4ec4d26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112848304245481472-1988e3f7ab74.jpg" alt="云上列车城市 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

## 🎨 SVG 与交互图形

<a id="case-14"></a>
### 案例 14: [可乐瓶 SVG](https://x.com/dummerspast39/status/2112999200472596959) (作者 [@dummerspast39](https://x.com/dummerspast39))

**观察创作者称为 SVG 的立体可乐瓶展示。**

作者自述在 Arena 耗时约五分钟。录屏显示结果，但没有独立复现 SVG 实现或与 Opus 的比较。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112998739115651072-36c11d258cd7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112998739115651072-92e3c1a11f11.jpg" alt="可乐瓶 SVG — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-15"></a>
### 案例 15: [交互 PS5 手柄](https://x.com/marcthecreatorr/status/2112894985267761333) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**观察手柄 SVG 的近景与不同显示状态。**

作者称等待较久，且 Carbon 显示为 gemini-4-argon。录屏不能独立核验后台型号。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112894899636862976-d5e2bb02aca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112894899636862976-279e5a90cd0e.jpg" alt="交互 PS5 手柄 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-16"></a>
### 案例 16: [Xbox 风格手柄](https://x.com/Mr_Salio/status/2112842066501816466) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**观察细节丰富的 Xbox 风格手柄渲染。**

来源标注 Carbon，并称 Arena 显示为 Argon。后来的资讯帖展示同一手柄设计，归并到本案例。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg" alt="Xbox 风格手柄 — 1" width="560"></a><br>查看来源图片</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg" alt="Xbox 风格手柄 — 2" width="560"></a><br>查看来源图片</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-17"></a>
### 案例 17: [跑车 SVG](https://x.com/auricxofficial/status/2112902209608597810) (作者 [@auricxofficial](https://x.com/auricxofficial))

**观察白色跑车侧面的车轮与车身细节。**

图片展示车辆，关联测试者称其为 SVG 测试。正文没有可运行代码，也未证明交互能力。

([@HarshithLucky3](https://x.com/HarshithLucky3/status/2112904832600477960))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg" alt="跑车 SVG — 1" width="560"></a><br>查看来源图片</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-18"></a>
### 案例 18: [夕阳海岸鹈鹕骑行](https://x.com/dummerspast39/status/2112941964819595479) (作者 [@dummerspast39](https://x.com/dummerspast39))

**观察夕阳海岸背景下的鹈鹕骑车动画。**

来源称产物为 SVG，与 LuminaBench 的海港版场景不同；两者都不视为可复现的代码交付。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112941947727785984-a35fd5a8a21a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112941947727785984-ebb464917b8f.jpg" alt="夕阳海岸鹈鹕骑行 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-19"></a>
### 案例 19: [四季鹈鹕骑行](https://x.com/hamoudi_yo/status/2112933636093919333) (作者 [@hamoudi_yo](https://x.com/hamoudi_yo))

**探索鹈鹕骑车的四季画面。**

来源明确称为四季 SVG，并称 Arena 检查点显示为 Argon。后台身份仍是来源自述。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112933037528772609-fd19e0c4ed54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112933037528772609-ed8b4e1fd852.jpg" alt="四季鹈鹕骑行 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-20"></a>
### 案例 20: [淡彩鹈鹕骑行](https://x.com/abhinavflac/status/2112825133052428378) (作者 [@abhinavflac](https://x.com/abhinavflac))

**观察淡彩鹈鹕自行车场景中的翅膀运动。**

作者强调扑翼和爪子。与其他鹈鹕测试同题，不代表同一份输出。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112824858526814208-cadb280b19f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112824858526814208-57282e71a7ce.jpg" alt="淡彩鹈鹕骑行 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-21"></a>
### 案例 21: [海港鹈鹕与 UI 局限](https://x.com/LuminaBench/status/2112830849771004187) (作者 [@LuminaBench](https://x.com/LuminaBench))

**观察海港鹈鹕 SVG，并考虑可用性与响应时间。**

测试者明确认为 UI 不佳、生成很慢；展示动画时同时保留这些缺点。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112830075997507584-093a4bc78c90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112830075997507584-5f9cde944578.jpg" alt="海港鹈鹕与 UI 局限 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Limit | 日期: 2026-10-21

---

## 🎮 游戏与动画场景

<a id="case-22"></a>
### 案例 22: [马里奥风格平台游戏](https://x.com/LuminaBench/status/2112848294581813473) (作者 [@LuminaBench](https://x.com/LuminaBench))

**观察平台游戏的室外及地下区域录屏。**

创作者自述约 30 分钟、首试成功。录屏不能验证所有碰撞、关卡规则或重启路径。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112846477709967360-9bcb4df969c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112846477709967360-99c390222b65.jpg" alt="马里奥风格平台游戏 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-23"></a>
### 案例 23: [方块世界沙盒](https://x.com/Haleeeemahh/status/2112871860094538053) (作者 [@Haleeeemahh](https://x.com/Haleeeemahh))

**观察带方块工具栏的 Minecraft 风格第一人称世界。**

抽帧显示导航和放置方块。来源称其为显示 Argon 名称的 Carbon 检查点，未测试完整游戏逻辑。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112871560407097344-e1b7609246df.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112871560407097344-37726fd4c849.jpg" alt="方块世界沙盒 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

<a id="case-24"></a>
### 案例 24: [青蛙滑板场景](https://x.com/SPAC89/status/2112845784500629765) (作者 [@SPAC89](https://x.com/SPAC89))

**观察风格化场景中青蛙踩滑板的动画。**

具体任务可从媒体看到，正文较泛。作者对速度的正面感受不是计时测量。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112845628640251904-f1909c90d438.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112845628640251904-700f770e3a57.jpg" alt="青蛙滑板场景 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Demo | 日期: 2026-10-21

---

## 🔬 模型对比

<a id="case-25"></a>
### 案例 25: [三模型骑行动画对比](https://x.com/AI_Screening/status/2112916947923087364) (作者 [@AI_Screening](https://x.com/AI_Screening))

**对照来源组合展示的 Carbon、Argon 与 GPT-6 Astra 骑行动画。**

录屏保留模型标签及对应产物。发布者偏好 Carbon，但没有提供共同设置、重试次数或执行日志。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112916798039642113-7f04c4d03491.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112916798039642113-c1474c749e67.jpg" alt="三模型骑行动画对比 — 1" width="560"></a><br>观看来源视频</td></tr></table>

类型: Evaluation | 日期: 2026-10-21

---

<a id="related-repositories"></a>
## 相关仓库

- [Gemini 3.6 Flash — 指南与使用案例](https://github.com/Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases)
- [Gemini Omni — 指南与提示词](https://github.com/Evolink-AI/awesome-gemini-omni-guide-api-and-prompt)

<a id="acknowledge"></a>
## 🙏 致谢

感谢以下公开分享演示的发布者：

[@thtbee_](https://x.com/thtbee_), [@hakmgpt](https://x.com/hakmgpt), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@dummerspast39](https://x.com/dummerspast39), [@Mr_Salio](https://x.com/Mr_Salio), [@doe_naps](https://x.com/doe_naps), [@abhinavflac](https://x.com/abhinavflac), [@LuminaBench](https://x.com/LuminaBench), [@HarshithLucky3](https://x.com/HarshithLucky3), [@SPAC89](https://x.com/SPAC89), [@marcthecreatorr](https://x.com/marcthecreatorr), [@auricxofficial](https://x.com/auricxofficial), [@hamoudi_yo](https://x.com/hamoudi_yo), [@Haleeeemahh](https://x.com/Haleeeemahh), [@AI_Screening](https://x.com/AI_Screening)

署名依据所链接来源，可能需要更正。若有遗漏署名、重复作品、表述错误或移除需求，请提交 issue。第三方媒体权利归原权利人。
