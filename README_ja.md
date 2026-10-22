<div align="center">

<a href="https://evolink.ai?utm_source=github&utm_medium=banner&utm_campaign=gemini-4-carbon-usecases&utm_content=readme-cover"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/banner/banner-owner-6aea570af8a4.png" alt="Gemini 4 Carbon — コミュニティ活用事例" width="760"></a>

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

## 🍌 紹介

初期展開の時期に、投稿者が Gemini 4 Carbon によるものとして公開したコミュニティのデモ集です。

**元の情報源を通じて具体的なタスク、見える出力、実用上の制約を確認できます。**

## 📊 概要

5分類、25事例。転載は同じ作品にまとめ、既存出力の比較は元の事例に添えています。

> [!NOTE]
> モデル名、生成時間、品質評価は情報源の自己申告です。Arena の表示名ではバックエンドの版を確認できません。録画だけではコードの実行、全操作の正しさ、再現性は証明できません。

<a id="quick-start"></a>
## ⚡ クイックスタート

1. 目次からタスクを選びます。
2. 動画や画像を開き、事例タイトルから元の投稿へ進みます。
3. 見える結果をタスクと制約に照らして確認します。

## 📑 目次

| 事例 | 分類 | タイプ |
|---|---|---|
| [1. 機械の花](#case-1) | 機械と3Dオブジェクト | Demo |
| [2. 機械の蜂](#case-2) | 機械と3Dオブジェクト | Demo |
| [3. 機械生物とクモの巣](#case-3) | 機械と3Dオブジェクト | Demo |
| [4. 水晶の柑橘](#case-4) | 機械と3Dオブジェクト | Demo |
| [5. ホグワーツのボクセル建築](#case-5) | ボクセル世界と風景 | Demo |
| [6. ボクセルの城と風景](#case-6) | ボクセル世界と風景 | Demo |
| [7. 富士の庭園](#case-7) | ボクセル世界と風景 | Demo |
| [8. ボクセルの川と天候](#case-8) | ボクセル世界と風景 | Demo |
| [9. ボクセルの塔](#case-9) | ボクセル世界と風景 | Demo |
| [10. 五重のボクセル塔](#case-10) | ボクセル世界と風景 | Demo |
| [11. ボクセルの灯台島](#case-11) | ボクセル世界と風景 | Demo |
| [12. 機械クラーケンのジオラマ](#case-12) | ボクセル世界と風景 | Demo |
| [13. 空の鉄道都市](#case-13) | ボクセル世界と風景 | Demo |
| [14. コーラ瓶のSVG](#case-14) | SVGとインタラクティブ画像 | Demo |
| [15. 操作可能なPS5コントローラー](#case-15) | SVGとインタラクティブ画像 | Demo |
| [16. Xbox風コントローラー](#case-16) | SVGとインタラクティブ画像 | Demo |
| [17. スポーツカーのSVG](#case-17) | SVGとインタラクティブ画像 | Demo |
| [18. 夕暮れの海岸を走るペリカン](#case-18) | SVGとインタラクティブ画像 | Demo |
| [19. 四季のペリカン自転車](#case-19) | SVGとインタラクティブ画像 | Demo |
| [20. 淡い色のペリカン自転車](#case-20) | SVGとインタラクティブ画像 | Demo |
| [21. 港のペリカンとUIの制約](#case-21) | SVGとインタラクティブ画像 | Limit |
| [22. マリオ風プラットフォームゲーム](#case-22) | ゲームとアニメーション | Demo |
| [23. ブロック世界のサンドボックス](#case-23) | ゲームとアニメーション | Demo |
| [24. カエルのスケートボード](#case-24) | ゲームとアニメーション | Demo |
| [25. 3モデルの自転車アニメーション比較](#case-25) | モデル比較 | Evaluation |

## ⚙️ 機械と3Dオブジェクト

<a id="case-1"></a>
### 事例 1: [機械の花](https://x.com/thtbee_/status/2112935205703147750) (投稿者 [@thtbee_](https://x.com/thtbee_))

**three.js の花の材質、照明、小さな蜂の変化を観察します。**

作者は約1時間43分かかったとし、自由な依頼によって蜂が追加されたと説明しています。時間は自己申告です。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112929911149371392-e21290e5e3a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112929911149371392-e771176b9f52.jpg" alt="機械の花 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-2"></a>
### 事例 2: [機械の蜂](https://x.com/thtbee_/status/2112971691966267827) (投稿者 [@thtbee_](https://x.com/thtbee_))

**機械の蜂のアニメーションと8の字運動を観察します。**

作者は Argon より精緻になったとし、以前のテストを引用しています。共通の計時や成功率のデータはありません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112971150624276481-08802f1fd200.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112971150624276481-37af1edb658b.jpg" alt="機械の蜂 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-3"></a>
### 事例 3: [機械生物とクモの巣](https://x.com/hakmgpt/status/2112999946777719116) (投稿者 [@hakmgpt](https://x.com/hakmgpt))

**機械生物、クモの巣、有翼装置の映像を見ます。**

抽出した3フレームには別々の場面があります。短い説明からはプロンプト、手順、同じ生成かどうかは分かりません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112997765458309120-c7d3c185b9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112997765458309120-bc5f3191664e.jpg" alt="機械生物とクモの巣 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-4"></a>
### 事例 4: [水晶の柑橘](https://x.com/pankajkumar_dev/status/2112946681977430469) (投稿者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**柑橘モデルの層、照明、動く視点を観察します。**

作者によると約20分で、Arena の表示は gemini-4-argon でした。Carbon との同定は作者の主張です。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112945233822617600-6e32038ca6b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112945233822617600-ada2f593eab5.jpg" alt="水晶の柑橘 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

## 🏞️ ボクセル世界と風景

<a id="case-5"></a>
### 事例 5: [ホグワーツのボクセル建築](https://x.com/dummerspast39/status/2112989454239416450) (投稿者 [@dummerspast39](https://x.com/dummerspast39))

**城の内部と外部の視点を巡ります。**

投稿には best of 4 と明記されています。選ばれた結果であり、初回成功の証拠ではありません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112989347301519360-99b7308b4b0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112989347301519360-42c02806db71.jpg" alt="ホグワーツのボクセル建築 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-6"></a>
### 事例 6: [ボクセルの城と風景](https://x.com/Mr_Salio/status/2112856590386643413) (投稿者 [@Mr_Salio](https://x.com/Mr_Salio))

**昼、夜、上空から城を観察します。**

別の城の出力を示す動画です。Opus との比較は投稿者の意見で、統一ベンチマークや生成過程はありません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112856348719210496-a57ed12eb899.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112856348719210496-b6b5dc0a31f6.jpg" alt="ボクセルの城と風景 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-7"></a>
### 事例 7: [富士の庭園](https://x.com/doe_naps/status/2112975635337593132) (投稿者 [@doe_naps](https://x.com/doe_naps))

**蝶の視点を含む小さな日本庭園を探索します。**

投稿では反射、動く人々、小さな世界を説明しています。抽出フレームで複数の視点を確認しましたが、全操作は試していません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112972423893221376-421aa3046fa3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112972423893221376-a5bc633b97f3.jpg" alt="富士の庭園 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-8"></a>
### 事例 8: [ボクセルの川と天候](https://x.com/abhinavflac/status/2112910206644756745) (投稿者 [@abhinavflac](https://x.com/abhinavflac))

**川の反射と天候の変化を観察します。**

作者は Argon の2–3倍の時間が必要だったとしています。統一された計時方法のない個人的な比較です。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112909984925372417-c80bf67ccd5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112909984925372417-5998d70a68db.jpg" alt="ボクセルの川と天候 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-9"></a>
### 事例 9: [ボクセルの塔](https://x.com/LuminaBench/status/2112822997161562600) (投稿者 [@LuminaBench](https://x.com/LuminaBench))

**異なる照明の下で塔の浮島の細部を観察します。**

作者はタスクによって Argon の2–4倍遅いと述べており、モデル全体の遅延測定ではありません。同じ作者による他の3モデルとの比較も元のラベルのまま添付し、別の Carbon 生成として数えていません。

([@LuminaBench](https://x.com/LuminaBench/status/2112829559158800732))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112821820793434112-52372e9a3a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112821820793434112-b673916ea1e4.jpg" alt="ボクセルの塔 — 1" width="560"></a><br>元の動画を見る</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112827630357516288-060bdc9c31b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112827630357516288-76711181a8a7.jpg" alt="ボクセルの塔 — 2" width="560"></a><br>元のモデル比較を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-10"></a>
### 事例 10: [五重のボクセル塔](https://x.com/Mr_Salio/status/2112890002619142465) (投稿者 [@Mr_Salio](https://x.com/Mr_Salio))

**別の塔の照明変化と近景を観察します。**

LuminaBench の事例とは異なる塔の映像です。同じ題材でも同じ生成とは限りません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112889945530445824-a889d183dcfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112889945530445824-be4088fa4d3a.jpg" alt="五重のボクセル塔 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-11"></a>
### 事例 11: [ボクセルの灯台島](https://x.com/LuminaBench/status/2112844170209399118) (投稿者 [@LuminaBench](https://x.com/LuminaBench))

**昼夜と天候が変化する灯台の場面を見ます。**

投稿はボクセルの細部を評価しています。抽出フレームで灯台を特定できますが、プロンプトやコードは公開されていません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112841088444628992-40ce06ef4e5f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112841088444628992-86073f2c1e6c.jpg" alt="ボクセルの灯台島 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-12"></a>
### 事例 12: [機械クラーケンのジオラマ](https://x.com/HarshithLucky3/status/2112882176912158877) (投稿者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**真鍮の機械クラーケンと潜水艦のボクセル場面を観察します。**

投稿には蒸気機械の海怪、ヴィクトリア朝の潜水艦、熱水噴出孔が指定され、Argon 表示の Arena チェックポイントを Carbon としています。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112881879125053440-ed7a36ad009c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112881879125053440-ef964b2745cf.jpg" alt="機械クラーケンのジオラマ — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-13"></a>
### 事例 13: [空の鉄道都市](https://x.com/SPAC89/status/2112849450993336595) (投稿者 [@SPAC89](https://x.com/SPAC89))

**列車、高架線路、塔のある幻想的な場面を探索します。**

タスクは一般的な説明文ではなく動画から特定しています。公開時期の予測や順位は、この場面の性能証拠ではありません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112848304245481472-f855a4ec4d26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112848304245481472-1988e3f7ab74.jpg" alt="空の鉄道都市 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

## 🎨 SVGとインタラクティブ画像

<a id="case-14"></a>
### 事例 14: [コーラ瓶のSVG](https://x.com/dummerspast39/status/2112999200472596959) (投稿者 [@dummerspast39](https://x.com/dummerspast39))

**作者が SVG と説明する立体的なコーラ瓶を観察します。**

作者は Arena で約5分と述べています。映像は結果を示しますが、SVG 実装や Opus との比較は独立に再現していません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112998739115651072-36c11d258cd7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112998739115651072-92e3c1a11f11.jpg" alt="コーラ瓶のSVG — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-15"></a>
### 事例 15: [操作可能なPS5コントローラー](https://x.com/marcthecreatorr/status/2112894985267761333) (投稿者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**コントローラー SVG の近景と表示切替を観察します。**

作者は長い待ち時間と gemini-4-argon 表示を報告しています。録画ではバックエンドのモデルを独立に確認できません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112894899636862976-d5e2bb02aca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112894899636862976-279e5a90cd0e.jpg" alt="操作可能なPS5コントローラー — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-16"></a>
### 事例 16: [Xbox風コントローラー](https://x.com/Mr_Salio/status/2112842066501816466) (投稿者 [@Mr_Salio](https://x.com/Mr_Salio))

**細部を描いた Xbox 風コントローラーを観察します。**

投稿は Carbon とし、Arena では Argon 表示だったと主張しています。同じデザインを示す後のニュース投稿もこの事例にまとめています。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg" alt="Xbox風コントローラー — 1" width="560"></a><br>元の画像を開く</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg" alt="Xbox風コントローラー — 2" width="560"></a><br>元の画像を開く</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-17"></a>
### 事例 17: [スポーツカーのSVG](https://x.com/auricxofficial/status/2112902209608597810) (投稿者 [@auricxofficial](https://x.com/auricxofficial))

**白い車の側面、ホイール、車体の細部を観察します。**

画像は車を示し、関連するテスターは SVG テストと呼んでいます。実行可能コードや操作性の証拠はありません。

([@HarshithLucky3](https://x.com/HarshithLucky3/status/2112904832600477960))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg" alt="スポーツカーのSVG — 1" width="560"></a><br>元の画像を開く</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-18"></a>
### 事例 18: [夕暮れの海岸を走るペリカン](https://x.com/dummerspast39/status/2112941964819595479) (投稿者 [@dummerspast39](https://x.com/dummerspast39))

**夕暮れの海岸を背景にしたペリカンの自転車アニメーションを見ます。**

投稿は SVG としています。LuminaBench の港の版とは別の場面で、いずれも再現可能なコード納品とは扱いません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112941947727785984-a35fd5a8a21a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112941947727785984-ebb464917b8f.jpg" alt="夕暮れの海岸を走るペリカン — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-19"></a>
### 事例 19: [四季のペリカン自転車](https://x.com/hamoudi_yo/status/2112933636093919333) (投稿者 [@hamoudi_yo](https://x.com/hamoudi_yo))

**ペリカンの自転車を四季の風景で見ます。**

投稿は四季の SVG と明記し、Arena の表示を Argon としています。バックエンドの同定は自己申告です。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112933037528772609-fd19e0c4ed54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112933037528772609-ed8b4e1fd852.jpg" alt="四季のペリカン自転車 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-20"></a>
### 事例 20: [淡い色のペリカン自転車](https://x.com/abhinavflac/status/2112825133052428378) (投稿者 [@abhinavflac](https://x.com/abhinavflac))

**淡い色の場面で羽の動きを観察します。**

作者は羽ばたきと爪を強調しています。他のテストと題材が同じでも、同じ出力とは限りません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112824858526814208-cadb280b19f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112824858526814208-57282e71a7ce.jpg" alt="淡い色のペリカン自転車 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-21"></a>
### 事例 21: [港のペリカンとUIの制約](https://x.com/LuminaBench/status/2112830849771004187) (投稿者 [@LuminaBench](https://x.com/LuminaBench))

**港のペリカン SVG を使い勝手や応答時間とともに観察します。**

テスターは UI が良くなく、生成も非常に遅いと明記しています。見えるアニメーションとともに欠点も残します。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112830075997507584-093a4bc78c90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112830075997507584-5f9cde944578.jpg" alt="港のペリカンとUIの制約 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Limit | 日付: 2026-10-21

---

## 🎮 ゲームとアニメーション

<a id="case-22"></a>
### 事例 22: [マリオ風プラットフォームゲーム](https://x.com/LuminaBench/status/2112848294581813473) (投稿者 [@LuminaBench](https://x.com/LuminaBench))

**屋外と地下を含むゲーム映像を観察します。**

作者は約30分、初回成功と報告しています。録画では全ての当たり判定、ルール、再開始経路は検証できません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112846477709967360-9bcb4df969c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112846477709967360-99c390222b65.jpg" alt="マリオ風プラットフォームゲーム — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-23"></a>
### 事例 23: [ブロック世界のサンドボックス](https://x.com/Haleeeemahh/status/2112871860094538053) (投稿者 [@Haleeeemahh](https://x.com/Haleeeemahh))

**ブロックのツールバーがある Minecraft 風一人称世界を観察します。**

抽出フレームは移動とブロック配置を示します。投稿は Argon 表示の Carbon としていますが、全ゲームロジックは未検証です。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112871560407097344-e1b7609246df.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112871560407097344-37726fd4c849.jpg" alt="ブロック世界のサンドボックス — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

<a id="case-24"></a>
### 事例 24: [カエルのスケートボード](https://x.com/SPAC89/status/2112845784500629765) (投稿者 [@SPAC89](https://x.com/SPAC89))

**様式化された場面でスケートボードに乗るカエルを観察します。**

説明文は一般的ですが、具体的なタスクは映像で分かります。速度への好印象は計時結果ではありません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112845628640251904-f1909c90d438.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112845628640251904-700f770e3a57.jpg" alt="カエルのスケートボード — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Demo | 日付: 2026-10-21

---

## 🔬 モデル比較

<a id="case-25"></a>
### 事例 25: [3モデルの自転車アニメーション比較](https://x.com/AI_Screening/status/2112916947923087364) (投稿者 [@AI_Screening](https://x.com/AI_Screening))

**Carbon、Argon、GPT-6 Astra の出力を並べた元動画を比較します。**

元のラベルと出力を一緒に残しています。投稿者は Carbon を好みますが、共通設定、再試行数、実行ログはありません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112916798039642113-7f04c4d03491.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112916798039642113-c1474c749e67.jpg" alt="3モデルの自転車アニメーション比較 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Evaluation | 日付: 2026-10-21

---

<a id="related-repositories"></a>
## 関連リポジトリ

- [Gemini 3.6 Flash — ガイドと活用事例](https://github.com/Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases)
- [Gemini Omni — ガイドとプロンプト](https://github.com/Evolink-AI/awesome-gemini-omni-guide-api-and-prompt)

<a id="acknowledge"></a>
## 🙏 謝辞

デモを公開した以下の投稿者に感謝します。

[@thtbee_](https://x.com/thtbee_), [@hakmgpt](https://x.com/hakmgpt), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@dummerspast39](https://x.com/dummerspast39), [@Mr_Salio](https://x.com/Mr_Salio), [@doe_naps](https://x.com/doe_naps), [@abhinavflac](https://x.com/abhinavflac), [@LuminaBench](https://x.com/LuminaBench), [@HarshithLucky3](https://x.com/HarshithLucky3), [@SPAC89](https://x.com/SPAC89), [@marcthecreatorr](https://x.com/marcthecreatorr), [@auricxofficial](https://x.com/auricxofficial), [@hamoudi_yo](https://x.com/hamoudi_yo), [@Haleeeemahh](https://x.com/Haleeeemahh), [@AI_Screening](https://x.com/AI_Screening)

帰属はリンク先の情報に基づき、訂正が必要な場合があります。クレジット漏れ、重複、誤記、削除依頼は issue でお知らせください。第三者のメディアの権利は元の権利者に帰属します。
