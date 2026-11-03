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

5分類、44事例。転載は同じ作品にまとめ、既存出力の比較は元の事例に添えています。

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
| [26. 分解表示付きのロボットの目](#case-26) | 機械と3Dオブジェクト | Demo |
| [27. 2モデルによるカフェレーサーの内部表示](#case-27) | 機械と3Dオブジェクト | Evaluation |
| [28. 音楽ループ付きの雨の風景](#case-28) | SVGとインタラクティブ画像 | Demo |
| [29. 追加プロンプト前後の城とドラゴン](#case-29) | ボクセル世界と風景 | Evaluation |
| [30. 3モデルによる機械の顎](#case-30) | モデル比較 | Evaluation |
| [31. 9気筒星型エンジンの比較](#case-31) | モデル比較 | Evaluation |
| [32. 機械のサメ：速度と内部構造](#case-32) | モデル比較 | Limit |
| [33. 2モデルによるV8エンジンの観察](#case-33) | 機械と3Dオブジェクト | Evaluation |
| [34. 単一シェーダーによるコーラ瓶](#case-34) | 機械と3Dオブジェクト | Demo |
| [35. 約30分で作ったMinecraft風ゲーム](#case-35) | ゲームとアニメーション | Demo |
| [36. ゾンビの手のアニメーション：時間と費用](#case-36) | モデル比較 | Evaluation |
| [37. 3Dカーレースゲーム](#case-37) | ゲームとアニメーション | Demo |
| [38. 2ストロークエンジン：見えにくい燃焼行程](#case-38) | モデル比較 | Limit |
| [39. 2モデルによる機械式時計の観察](#case-39) | 機械と3Dオブジェクト | Evaluation |
| [40. お化け屋敷サイトの比較](#case-40) | モデル比較 | Evaluation |
| [41. 2つのモデル名による機械のワシ](#case-41) | 機械と3Dオブジェクト | Evaluation |
| [42. 灯籠が流れる夜の川](#case-42) | ボクセル世界と風景 | Demo |
| [43. 3つの照明状態の帆船](#case-43) | ボクセル世界と風景 | Demo |
| [44. 赤い船体の帆船](#case-44) | ボクセル世界と風景 | Demo |

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

<a id="pending-candidates"></a>
<a id="candidate-1"></a>
<a id="case-26"></a>
### 事例 26: [分解表示付きのロボットの目](https://x.com/noclipepe/status/2115556254101692515) (投稿者 [@noclipepe](https://x.com/noclipepe))

**まばたき、焦点調整、部品の分解表示を組み合わせたロボットの目のデモを確認できます。**

作者は1回のプロンプトで29分49秒かかったと報告しています。元の録画へのリンクを掲載していますが、実行可能なコード、操作全体、再現性は独立に検証していません。

[元の動画を見る](https://x.com/noclipepe/status/2115556254101692515/video/1)

タイプ: Demo | 日付: 2026-10-28

---

<a id="candidate-2"></a>
<a id="case-27"></a>
### 事例 27: [2モデルによるカフェレーサーの内部表示](https://x.com/dromexa/status/2115802517942497491) (投稿者 [@dromexa](https://x.com/dromexa))

**CarbonとOpus 5.5によるバイクの内部表示デモを比較できます。**

投稿者は、X線表示、断面表示、分解表示に同じプロンプトを使い、各モデルで1回ずつ試したと述べています。条件は投稿者の申告であり、共通の実行ログや独立した再現検証に基づく総合順位ではありません。

[元の動画を見る](https://x.com/dromexa/status/2115802517942497491/video/1)

タイプ: Evaluation | 日付: 2026-10-29

---

<a id="case-33"></a>
### 事例 33: [2モデルによるV8エンジンの観察](https://x.com/dromexa/status/2116927253980594275) (投稿者 [@dromexa](https://x.com/dromexa))

**エンジンの透視、断面、分解図、部品ごとの表示を確認します。**

作者はCarbonとOpus 5.5に同じプロンプトを与え、それぞれ1回試したと報告しています。3連勝という主張は個人的な評価で、実行可能なコードや機構の精度は独立に確認していません。

[元の動画を見る](https://x.com/dromexa/status/2116927253980594275/video/1)

タイプ: Evaluation | 日付: 2026-11-01

---

<a id="case-34"></a>
### 事例 34: [単一シェーダーによるコーラ瓶](https://x.com/dummerspast39/status/2116470583097438519) (投稿者 [@dummerspast39](https://x.com/dummerspast39))

**数学的なシェーダー形状として紹介されたThree.jsの瓶を観察します。**

作者は外部モデルや素材を使わず、栓には21個の歯があると述べています。以前のSVG瓶とは別のシェーダー実演で、コード、素材依存関係、歯の数は独立に確認していません。

[元の動画を見る](https://x.com/dummerspast39/status/2116470583097438519/video/1)

タイプ: Demo | 日付: 2026-10-31

---

<a id="case-39"></a>
### 事例 39: [2モデルによる機械式時計の観察](https://x.com/dromexa/status/2116518366919667775) (投稿者 [@dromexa](https://x.com/dromexa))

**時計の透視、断面、分解図を確認します。**

作者はCarbonとOpus 5.5に同じプロンプトで各1回試し、テンプの振動と正しい速度の歯車を報告しています。歯車比や時計としての精度は独立に確認していません。

[元の動画を見る](https://x.com/dromexa/status/2116518366919667775/video/1)

タイプ: Evaluation | 日付: 2026-10-31

---

<a id="case-41"></a>
### 事例 41: [2つのモデル名による機械のワシ](https://x.com/srikanthvaluri/status/2116767284618486044) (投稿者 [@srikanthvaluri](https://x.com/srikanthvaluri))

**出典でCarbonとArgonのラベルが付いた機械のワシを比較できます。**

抽出フレームでは異なるデザイン、翼の位置、カメラ角度を確認できます。作者の課題はThree.js製の機械のワシであり、モデルの識別と機構の動作は出典側の申告にとどまります。

[元の動画を見る](https://x.com/srikanthvaluri/status/2116767284618486044/video/1)

タイプ: Evaluation | 日付: 2026-11-01

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

<a id="candidate-4"></a>
<a id="case-29"></a>
### 事例 29: [追加プロンプト前後の城とドラゴン](https://x.com/semichenkko/status/2116198626187706722) (投稿者 [@semichenkko](https://x.com/semichenkko))

**3回の追加プロンプトの前後で城とドラゴンの風景を比較できます。**

作者は同じ島、城、ドラゴンについて、最初のプロンプトと、その後3回追加した結果を並べ、炎の変化を強調しています。追加プロンプトの本文と実行ログは公開されておらず、1人の作者による比較であって成功率の統制試験ではありません。

[元の動画を見る](https://x.com/semichenkko/status/2116198626187706722/video/1)

タイプ: Evaluation | 日付: 2026-10-30

---

<a id="case-42"></a>
### 事例 42: [灯籠が流れる夜の川](https://x.com/pankajkumar_dev/status/2116533017934241886) (投稿者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**灯籠で満たされた川の風景を録画の複数の視点から確認できます。**

作者は光る灯籠と水面反射のある夜景を指定しています。抽出フレームにはそれらと灯籠を追加する操作が映っていますが、アプリ全体の操作は試験していません。

[元の動画を見る](https://x.com/pankajkumar_dev/status/2116533017934241886/video/1)

タイプ: Demo | 日付: 2026-10-31

---

<a id="case-43"></a>
### 事例 43: [3つの照明状態の帆船](https://x.com/srikanthvaluri/status/2116931901332369894) (投稿者 [@srikanthvaluri](https://x.com/srikanthvaluri))

**昼、夕焼け、夜の帆船を確認できます。**

出典の課題は照明が変わる外洋の歴史的な帆船です。抽出フレームでは暗い船体と白い帆が各状態に映っていますが、波の物理やモデルの識別は独立に試験していません。

[元の動画を見る](https://x.com/srikanthvaluri/status/2116931901332369894/video/1)

タイプ: Demo | 日付: 2026-11-01

---

<a id="case-44"></a>
### 事例 44: [赤い船体の帆船](https://x.com/doe_naps/status/2116768227275788429) (投稿者 [@doe_naps](https://x.com/doe_naps))

**赤い船体と黄褐色の帆を持つ別の帆船風景を確認できます。**

抽出フレームには泡や鳥を伴う近景と遠景が映っています。船体、装飾、帆は3つの照明状態の船と異なりますが、作者によるCarbonへの帰属と実装全体は未検証です。

[元の動画を見る](https://x.com/doe_naps/status/2116768227275788429/video/1)

タイプ: Demo | 日付: 2026-11-01

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

<a id="candidate-3"></a>
<a id="case-28"></a>
### 事例 28: [音楽ループ付きの雨の風景](https://x.com/chetaslua/status/2115935747798950069) (投稿者 [@chetaslua](https://x.com/chetaslua))

**SVGの雨の風景を伴うJavaScript製の睡眠用音楽ループを元の投稿で確認できます。**

作者は音楽と雨の風景をCarbonで作り、1回の試行で約4,000行を生成したと述べています。コードの行数、音楽の独創性、再生機能全体は独立に検証していません。

[元の動画を見る](https://x.com/chetaslua/status/2115935747798950069/video/1)

タイプ: Demo | 日付: 2026-10-29

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

<a id="case-35"></a>
### 事例 35: [約30分で作ったMinecraft風ゲーム](https://x.com/dummerspast39/status/2116502497158201520) (投稿者 [@dummerspast39](https://x.com/dummerspast39))

**Minecraft風ゲームの録画と、作者が述べる開発条件を確認します。**

作者は不十分なエージェント実行環境で約30分、ほぼ1回の試行だったと報告しています。実行可能なプロジェクトはここでは提供されておらず、操作性、安定性、作者によるモデル順位は独立に検証していません。

[元の動画を見る](https://x.com/dummerspast39/status/2116502497158201520/video/1)

タイプ: Demo | 日付: 2026-10-31

---

<a id="case-37"></a>
### 事例 37: [3Dカーレースゲーム](https://x.com/Mr_Salio/status/2116798612361375995) (投稿者 [@Mr_Salio](https://x.com/Mr_Salio))

**新しいCarbonチェックポイントによるものとされるレース実演を確認します。**

作者は1つのプロンプトから約20分で遊べるゲームを作ったと報告しています。チェックポイントの正体、全素材の出所、プレイ可能性は独立に確認しておらず、録画だけではゲームの再現性は証明できません。

[元の動画を見る](https://x.com/Mr_Salio/status/2116798612361375995/video/1)

タイプ: Demo | 日付: 2026-11-01

---

## 🔬 モデル比較

<a id="case-25"></a>
### 事例 25: [3モデルの自転車アニメーション比較](https://x.com/AI_Screening/status/2112916947923087364) (投稿者 [@AI_Screening](https://x.com/AI_Screening))

**Carbon、Argon、GPT-6 Astra の出力を並べた元動画を比較します。**

元のラベルと出力を一緒に残しています。投稿者は Carbon を好みますが、共通設定、再試行数、実行ログはありません。

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112916798039642113-7f04c4d03491.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112916798039642113-c1474c749e67.jpg" alt="3モデルの自転車アニメーション比較 — 1" width="560"></a><br>元の動画を見る</td></tr></table>

タイプ: Evaluation | 日付: 2026-10-21

---

<a id="candidate-5"></a>
<a id="case-30"></a>
### 事例 30: [3モデルによる機械の顎](https://x.com/noclipepe/status/2116109757865930787) (投稿者 [@noclipepe](https://x.com/noclipepe))

**Carbon、Opus 5.5、GPT-6 Astraによる機械の顎と動く歯のデモを比較できます。**

作者は共通のプロンプトと歯ごとの動きを報告し、所要時間をCarbonは29m 9s、Opus 5.5は35m 17s、GPT-6 Astraは26m 7sとしています。時間、モデルの識別、操作全体は出典側の申告で、独立した再現検証はありません。

[元の動画を見る](https://x.com/noclipepe/status/2116109757865930787/video/1)

タイプ: Evaluation | 日付: 2026-10-30

---

<a id="case-31"></a>
### 事例 31: [9気筒星型エンジンの比較](https://x.com/olezhavich/status/2116606788241969445) (投稿者 [@olezhavich](https://x.com/olezhavich))

**4種類のエンジンアニメーションで断面の見やすさと工学的な細部を比較します。**

作者は同じプロンプトで各モデル1回ずつ試し、Carbonの見やすさとOpus 5.5の工学的な細部を評価しています。点火順序の正確さは作者の判断であり、独立した確認は行っていません。

[元の動画を見る](https://x.com/olezhavich/status/2116606788241969445/video/1)

タイプ: Evaluation | 日付: 2026-10-31

---

<a id="case-32"></a>
### 事例 32: [機械のサメ：速度と内部構造](https://x.com/0xPorterio/status/2116548548334321967) (投稿者 [@0xPorterio](https://x.com/0xPorterio))

**分解可能なサメの組み立て演出と内部構造を比較します。**

作者はCarbonの生成が速く演出も派手な一方、内部の細部はOpus 5.5に劣ると述べています。77–90という点数は個人の基準によるもので、部品数や機構の正確さは未検証です。

[元の動画を見る](https://x.com/0xPorterio/status/2116548548334321967/video/1)

タイプ: Limit | 日付: 2026-10-31

---

<a id="case-36"></a>
### 事例 36: [ゾンビの手のアニメーション：時間と費用](https://x.com/noclipepe/status/2116445289468850366) (投稿者 [@noclipepe](https://x.com/noclipepe))

**あるアニメーション課題の場面構成と、報告された時間・費用を比較します。**

作者はCarbonが1h 23m/$10.2、Opus 5.5が1h 6m/$8.1、GPT-6 Astraが24m/$5.7と報告しつつ、Carbonの場面を好んでいます。課題単位の費用報告であり、API単価でも独立に確認した費用でもありません。

[元の動画を見る](https://x.com/noclipepe/status/2116445289468850366/video/1)

タイプ: Evaluation | 日付: 2026-10-31

---

<a id="case-38"></a>
### 事例 38: [2ストロークエンジン：見えにくい燃焼行程](https://x.com/olezhavich/status/2116892619309461745) (投稿者 [@olezhavich](https://x.com/olezhavich))

**エンジンのアニメーションが燃焼とピストン運動を明確に説明できているか確認します。**

同じプロンプトで4モデルを各1回試したという比較で、作者はCarbonの炎が見えにくいとし、説明の明快さや写実性では他の出力を好んでいます。この課題に限った評価で、物理的な正確さや再現性は独立に検証していません。

[元の動画を見る](https://x.com/olezhavich/status/2116892619309461745/video/1)

タイプ: Limit | 日付: 2026-11-01

---

<a id="case-40"></a>
### 事例 40: [お化け屋敷サイトの比較](https://x.com/keydol123/status/2116556350130163783) (投稿者 [@keydol123](https://x.com/keydol123))

**同じ依頼から作られた2つのサイトの視覚的な雰囲気を比較します。**

作者は同じプロンプトによるお化け屋敷サイトをCarbonとOpus 5.5の出力として紹介しています。かわいいか怖いかは主観的な評価で、ソースコード、アクセシビリティ、サイト全体の動作は独立に検証していません。

[元の動画を見る](https://x.com/keydol123/status/2116556350130163783/video/1)

タイプ: Evaluation | 日付: 2026-10-31

---

<a id="related-repositories"></a>
## 関連リポジトリ

- [Gemini 3.6 Flash — ガイドと活用事例](https://github.com/Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases)
- [Gemini Omni — ガイドとプロンプト](https://github.com/Evolink-AI/awesome-gemini-omni-guide-api-and-prompt)

<a id="acknowledge"></a>
## 🙏 謝辞

デモを公開した以下の投稿者に感謝します。

[@thtbee_](https://x.com/thtbee_), [@hakmgpt](https://x.com/hakmgpt), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@dummerspast39](https://x.com/dummerspast39), [@Mr_Salio](https://x.com/Mr_Salio), [@doe_naps](https://x.com/doe_naps), [@abhinavflac](https://x.com/abhinavflac), [@LuminaBench](https://x.com/LuminaBench), [@HarshithLucky3](https://x.com/HarshithLucky3), [@SPAC89](https://x.com/SPAC89), [@marcthecreatorr](https://x.com/marcthecreatorr), [@auricxofficial](https://x.com/auricxofficial), [@hamoudi_yo](https://x.com/hamoudi_yo), [@Haleeeemahh](https://x.com/Haleeeemahh), [@AI_Screening](https://x.com/AI_Screening), [@noclipepe](https://x.com/noclipepe), [@dromexa](https://x.com/dromexa), [@chetaslua](https://x.com/chetaslua), [@semichenkko](https://x.com/semichenkko), [@olezhavich](https://x.com/olezhavich), [@0xPorterio](https://x.com/0xPorterio), [@keydol123](https://x.com/keydol123), [@srikanthvaluri](https://x.com/srikanthvaluri)

帰属はリンク先の情報に基づき、訂正が必要な場合があります。クレジット漏れ、重複、誤記、削除依頼は issue でお知らせください。第三者のメディアの権利は元の権利者に帰属します。
