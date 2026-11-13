<div align="center">

<a href="https://evolink.ai?utm_source=github&utm_medium=banner&utm_campaign=gemini-4-carbon-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/banner/banner-owner-6aea570af8a4.png" alt="Gemini 4 Carbon — Community use cases" width="760"></a>

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

## 🍌 Introduction

Examples of Gemini 4 Carbon published by the community and Google, alongside evaluations that explain how results were measured.

**Explore concrete tasks, visible outputs and practical limits through their original sources.**

## 📊 Overview

50 use cases across 5 categories. Reposts are grouped with their underlying work; comparisons of the same output are kept with its case.

> [!NOTE]
> Model names, generation times and quality judgments are source-reported. An Arena display name does not establish the backend version. A recording does not prove runnable code, complete interaction or repeatable success.

<a id="quick-start"></a>
## ⚡ Quick Start

1. Choose a task in the Menu.
2. Open its video or image, then follow the source-linked case title.
3. Compare the visible result with the stated task and limitations.

## 📑 Menu

| Case | Category | What it shows | Type |
|---|---|---|---|
| [Mechanical flower](#case-1) | Mechanical and 3D Objects | Inspect a three.js flower with changing materials, lighting and a small bee. | Demo |
| [Mechanical bee](#case-2) | Mechanical and 3D Objects | Inspect a mechanical bee animation and its figure-eight movement. | Demo |
| [Mechanical creatures and a spiderweb](#case-3) | Mechanical and 3D Objects | Explore a video sequence of mechanical creatures, a spiderweb and a winged device. | Demo |
| [Crystal citrus](#case-4) | Mechanical and 3D Objects | Inspect an interactive citrus model with layers, lighting and animated views. | Demo |
| [Hogwarts voxel build](#case-5) | Voxel Worlds and Scenery | Explore a voxel castle through changing interior and exterior views. | Demo |
| [Voxel castle landscape](#case-6) | Voxel Worlds and Scenery | Inspect a castle scene across daylight, nighttime and aerial views. | Demo |
| [Fuji Garden](#case-7) | Voxel Worlds and Scenery | Explore a miniature Japanese garden, including a butterfly viewpoint. | Demo |
| [Voxel river and weather](#case-8) | Voxel Worlds and Scenery | Inspect a voxel river landscape with reflections and changing weather. | Demo |
| [Voxel pagoda](#case-9) | Voxel Worlds and Scenery | Inspect a detailed pagoda island through several lighting conditions. | Demo |
| [Five-story pagoda](#case-10) | Voxel Worlds and Scenery | Inspect a second pagoda output with animated lighting and close-up views. | Demo |
| [Voxel lighthouse island](#case-11) | Voxel Worlds and Scenery | Explore a lighthouse scene across daylight, nighttime and weather changes. | Demo |
| [Mechanical kraken diorama](#case-12) | Voxel Worlds and Scenery | Inspect a brass mechanical kraken and submarine voxel scene. | Demo |
| [Sky railway city](#case-13) | Voxel Worlds and Scenery | Explore a fantastical rail scene with a train, elevated tracks and towers. | Demo |
| [Cola bottle SVG](#case-14) | SVG and Interactive Graphics | Inspect a dimensional cola-bottle presentation described by its creator as SVG. | Demo |
| [Interactive PS5 controller](#case-15) | SVG and Interactive Graphics | Inspect a controller SVG with close-up and alternate display states. | Demo |
| [Xbox controller](#case-16) | SVG and Interactive Graphics | Inspect a detailed Xbox-style controller rendering. | Demo |
| [Sports-car SVG](#case-17) | SVG and Interactive Graphics | Inspect a white sports-car side view and its detailed wheels and bodywork. | Demo |
| [Coastal pelican cyclist](#case-18) | SVG and Interactive Graphics | Inspect a pelican cyclist animation against a sunset waterfront. | Demo |
| [Four-season pelican cyclist](#case-19) | SVG and Interactive Graphics | Explore four seasonal presentations of a pelican riding a bicycle. | Demo |
| [Pastel pelican cyclist](#case-20) | SVG and Interactive Graphics | Inspect wing movement in a pastel-colored pelican bicycle scene. | Demo |
| [Harbor pelican and UI limits](#case-21) | SVG and Interactive Graphics | Inspect a harbor pelican SVG while considering usability and response time. | Limit |
| [Super Mario-style platformer](#case-22) | Games and Animated Scenes | Inspect a platform game recording across outdoor and underground areas. | Demo |
| [Block-world sandbox](#case-23) | Games and Animated Scenes | Inspect a Minecraft-style first-person world with a block toolbar. | Demo |
| [Frog skateboard scene](#case-24) | Games and Animated Scenes | Inspect an animated frog on a skateboard moving through a stylized scene. | Demo |
| [Bicycle animation across three models](#case-25) | Model Comparison | Compare the source's grouped Carbon, Argon and GPT-6 Astra bicycle outputs. | Evaluation |
| [Robotic eye with an exploded view](#case-26) | Mechanical and 3D Objects | Inspect a robotic-eye demonstration that combines blinking, focusing and an exploded view. | Demo |
| [Café racer inspection across two models](#case-27) | Mechanical and 3D Objects | Compare the source’s Carbon and Opus 5.5 motorcycle inspection demonstrations. | Evaluation |
| [Rain scene with a music loop](#case-28) | SVG and Interactive Graphics | Explore the source’s JavaScript sleep-music loop with an SVG rain scene. | Demo |
| [Castle and dragon after follow-up prompts](#case-29) | Voxel Worlds and Scenery | Compare a castle-and-dragon scene before and after three follow-up prompts. | Evaluation |
| [Mechanical jaw across three models](#case-30) | Model Comparison | Compare mechanical-jaw and moving-tooth demonstrations across Carbon, Opus 5.5 and GPT-6 Astra. | Evaluation |
| [Nine-cylinder radial engine comparison](#case-31) | Model Comparison | Compare cutaway clarity and engineering detail across four engine animations. | Evaluation |
| [Mechanical shark: speed versus internal detail](#case-32) | Model Comparison | Compare assembly effects with the internal structure of a dismantlable shark. | Limit |
| [V8 engine inspection across two models](#case-33) | Mechanical and 3D Objects | Inspect X-ray, cutaway, exploded and part-by-part engine views. | Evaluation |
| [Cola bottle in a single shader](#case-34) | Mechanical and 3D Objects | Explore a Three.js bottle presented as mathematical shader geometry. | Demo |
| [Minecraft-style game in about thirty minutes](#case-35) | Games and Animated Scenes | Explore a Minecraft-style game recording and its stated development constraints. | Demo |
| [Zombie-hand animation: time and cost](#case-36) | Model Comparison | Compare scene design alongside the reported time and cost of one animation task. | Evaluation |
| [Three-dimensional racing game](#case-37) | Games and Animated Scenes | Inspect a car-racing demonstration attributed to a newer Carbon checkpoint. | Demo |
| [Two-stroke engine: unclear power stroke](#case-38) | Model Comparison | Check whether an engine animation clearly explains combustion and piston movement. | Limit |
| [Mechanical watch inspection across two models](#case-39) | Mechanical and 3D Objects | Inspect a watch through X-ray, cutaway and exploded views. | Evaluation |
| [Haunted-house website comparison](#case-40) | Model Comparison | Compare the visual mood of two websites built for the same brief. | Evaluation |
| [Mechanical eagle across two model labels](#case-41) | Mechanical and 3D Objects | Compare the source’s Carbon- and Argon-labelled mechanical eagles. | Evaluation |
| [Lantern River Night](#case-42) | Voxel Worlds and Scenery | Explore a lantern-filled river scene through several recorded viewpoints. | Demo |
| [Sailing ship across three lighting states](#case-43) | Voxel Worlds and Scenery | Inspect a sailing ship at daylight, sunset and night. | Demo |
| [Red-hulled sailing ship](#case-44) | Voxel Worlds and Scenery | Explore another sailing-ship scene with a red hull and tan sails. | Demo |
| [Pelican Quest campus game](#case-45) | Games and Animated Scenes | Inspect how a multi-agent workflow assembles an explorable campus game. | Demo |
| [Multimodal Knowledge Agent benchmark](#case-46) | Model Comparison | Compare weighted rubric scores for visually complex documents and deliverables. | Benchmark |
| [Eiffel Tower construction model](#case-47) | Mechanical and 3D Objects | Follow the transformation of engineering drawings into an animated 3D construction sequence. | Demo |
| [Platform 37 office visualization](#case-48) | Mechanical and 3D Objects | Trace an office design from planning drawings to a rendered exterior. | Demo |
| [Tensile knit study](#case-49) | Mechanical and 3D Objects | Inspect a three-dimensional representation of knitted fabric under tension. | Demo |
| [Gemini merchandise storefront](#case-50) | SVG and Interactive Graphics | See how brand guidelines become a working storefront with custom visuals. | Demo |

| Section | Purpose |
|---|---|
| [Related Repositories](#related-repositories) | Browse related model repositories. |
| [Quick Start](#quick-start) | Find and inspect a case. |
| [Acknowledge](#acknowledge) | See credits and corrections. |

## ⚙️ Mechanical and 3D Objects

<a id="case-1"></a>
### Case 1: [Mechanical flower](https://x.com/thtbee_/status/2112935205703147750) (by [@thtbee_](https://x.com/thtbee_))

**Inspect a three.js flower with changing materials, lighting and a small bee.**

The creator reports about 1 hour 43 minutes and says the bee was added after an open-ended request. The timing is self-reported.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112929911149371392-e21290e5e3a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112929911149371392-e771176b9f52.jpg" alt="Mechanical flower — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-2"></a>
### Case 2: [Mechanical bee](https://x.com/thtbee_/status/2112971691966267827) (by [@thtbee_](https://x.com/thtbee_))

**Inspect a mechanical bee animation and its figure-eight movement.**

The creator reports improved polish over Argon and points to an earlier Argon test. The comparison has no controlled timing or success-rate data.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112971150624276481-08802f1fd200.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112971150624276481-37af1edb658b.jpg" alt="Mechanical bee — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-3"></a>
### Case 3: [Mechanical creatures and a spiderweb](https://x.com/hakmgpt/status/2112999946777719116) (by [@hakmgpt](https://x.com/hakmgpt))

**Explore a video sequence of mechanical creatures, a spiderweb and a winged device.**

The three sampled frames show distinct scenes. The short source caption does not establish their prompts, workflow or whether they came from one generation.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112997765458309120-c7d3c185b9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112997765458309120-bc5f3191664e.jpg" alt="Mechanical creatures and a spiderweb — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-4"></a>
### Case 4: [Crystal citrus](https://x.com/pankajkumar_dev/status/2112946681977430469) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Inspect an interactive citrus model with layers, lighting and animated views.**

The author reports roughly 20 minutes and an Arena display name of gemini-4-argon. The identification as Carbon is the author's claim.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112945233822617600-6e32038ca6b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112945233822617600-ada2f593eab5.jpg" alt="Crystal citrus — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="pending-candidates"></a>
<a id="candidate-1"></a>
<a id="case-26"></a>
### Case 26: [Robotic eye with an exploded view](https://x.com/noclipepe/status/2115556254101692515) (by [@noclipepe](https://x.com/noclipepe))

**Inspect a robotic-eye demonstration that combines blinking, focusing and an exploded view.**

The creator reports one prompt and 29 minutes 49 seconds. The source recording is linked; runnable code, complete interaction and repeatability have not been independently verified.

[Watch source video](https://x.com/noclipepe/status/2115556254101692515/video/1)

Type: Demo | Date: 2026-10-28

---

<a id="candidate-2"></a>
<a id="case-27"></a>
### Case 27: [Café racer inspection across two models](https://x.com/dromexa/status/2115802517942497491) (by [@dromexa](https://x.com/dromexa))

**Compare the source’s Carbon and Opus 5.5 motorcycle inspection demonstrations.**

The publisher reports the same prompt and one attempt per model for X-ray, cutaway and exploded views. These are source-reported conditions; no shared execution logs or independent reproduction establish a general model ranking.

[Watch source video](https://x.com/dromexa/status/2115802517942497491/video/1)

Type: Evaluation | Date: 2026-10-29

---

<a id="case-33"></a>
### Case 33: [V8 engine inspection across two models](https://x.com/dromexa/status/2116927253980594275) (by [@dromexa](https://x.com/dromexa))

**Inspect X-ray, cutaway, exploded and part-by-part engine views.**

The creator reports a shared prompt and one attempt each for Carbon and Opus 5.5. The claimed three-round winning streak is a personal judgment; runnable code and mechanical accuracy were not independently checked.

[Watch source video](https://x.com/dromexa/status/2116927253980594275/video/1)

Type: Evaluation | Date: 2026-11-01

---

<a id="case-34"></a>
### Case 34: [Cola bottle in a single shader](https://x.com/dummerspast39/status/2116470583097438519) (by [@dummerspast39](https://x.com/dummerspast39))

**Explore a Three.js bottle presented as mathematical shader geometry.**

The creator reports no external models or assets and a 21-tooth cap. This is a shader demonstration, distinct from the earlier SVG bottle; the code, asset dependencies and tooth count were not independently checked.

[Watch source video](https://x.com/dummerspast39/status/2116470583097438519/video/1)

Type: Demo | Date: 2026-10-31

---

<a id="case-39"></a>
### Case 39: [Mechanical watch inspection across two models](https://x.com/dromexa/status/2116518366919667775) (by [@dromexa](https://x.com/dromexa))

**Inspect a watch through X-ray, cutaway and exploded views.**

The creator reports a shared prompt and one attempt each for Carbon and Opus 5.5, including a ticking balance wheel and correct gear speeds. Gear ratios and timekeeping accuracy were not independently checked.

[Watch source video](https://x.com/dromexa/status/2116518366919667775/video/1)

Type: Evaluation | Date: 2026-10-31

---

<a id="case-41"></a>
### Case 41: [Mechanical eagle across two model labels](https://x.com/srikanthvaluri/status/2116767284618486044) (by [@srikanthvaluri](https://x.com/srikanthvaluri))

**Compare the source’s Carbon- and Argon-labelled mechanical eagles.**

Sampled frames show different eagle designs with changing wing positions and camera angles. The author requests a Three.js mechanical eagle; model identity and mechanical behavior remain source-reported.

[Watch source video](https://x.com/srikanthvaluri/status/2116767284618486044/video/1)

Type: Evaluation | Date: 2026-11-01

---

<a id="case-47"></a>
### Case 47: [Eiffel Tower construction model](https://www.youtube.com/watch?v=rOVEmjfPmYk) (by [@Google](https://www.youtube.com/@Google))

**Follow the transformation of engineering drawings into an animated 3D construction sequence.**

Google shows how Antigravity agents use historical engineering drawings to model the Eiffel Tower and visualize stages of construction. The clip shows the drawings and the resulting sequence. It does not verify dimensional accuracy against the original plans.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/eiffel-219200fbc2cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/eiffel-poster-9785df340ffa.jpg" alt="Eiffel Tower construction model — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-11-10

---

<a id="case-48"></a>
### Case 48: [Platform 37 office visualization](https://www.youtube.com/watch?v=1G2j2eA8sew) (by [@Google](https://www.youtube.com/@Google))

**Trace an office design from planning drawings to a rendered exterior.**

Google shows agents reading planning drawings, building geometry, and producing an exterior view of the office with a planted roof. The published clip shows the transition from the drawings to the rendered building. It does not establish that the geometry is suitable for construction.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/platform37-fbbf8bf2f63d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/platform37-poster-c57f77af8cd2.jpg" alt="Platform 37 office visualization — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-11-10

---

<a id="case-49"></a>
### Case 49: [Tensile knit study](https://www.youtube.com/watch?v=VDIMa4u9skQ) (by [@Google](https://www.youtube.com/@Google))

**Inspect a three-dimensional representation of knitted fabric under tension.**

Google shows an interactive visualizer based on a 2026 study of knitted textile mechanics. It depicts 110 fibers under tension. The clip shows the simulation and its plots, without providing physical validation of the material.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/tensile-knit-66c22f5d9e56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/tensile-knit-poster-241308cc9364.jpg" alt="Tensile knit study — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-11-10

---

## 🏞️ Voxel Worlds and Scenery

<a id="case-5"></a>
### Case 5: [Hogwarts voxel build](https://x.com/dummerspast39/status/2112989454239416450) (by [@dummerspast39](https://x.com/dummerspast39))

**Explore a voxel castle through changing interior and exterior views.**

The source explicitly says best of 4. This is a selected result, not evidence of first-attempt success.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112989347301519360-99b7308b4b0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112989347301519360-42c02806db71.jpg" alt="Hogwarts voxel build — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-6"></a>
### Case 6: [Voxel castle landscape](https://x.com/Mr_Salio/status/2112856590386643413) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Inspect a castle scene across daylight, nighttime and aerial views.**

The media shows a distinct castle output. The poster's comparison with Opus is an opinion; no controlled benchmark or generation process is supplied.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112856348719210496-a57ed12eb899.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112856348719210496-b6b5dc0a31f6.jpg" alt="Voxel castle landscape — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-7"></a>
### Case 7: [Fuji Garden](https://x.com/doe_naps/status/2112975635337593132) (by [@doe_naps](https://x.com/doe_naps))

**Explore a miniature Japanese garden, including a butterfly viewpoint.**

The source describes reflections, moving people and a tiny living world. Sampled frames show the garden from several viewpoints; full interaction was not tested.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112972423893221376-421aa3046fa3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112972423893221376-a5bc633b97f3.jpg" alt="Fuji Garden — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-8"></a>
### Case 8: [Voxel river and weather](https://x.com/abhinavflac/status/2112910206644756745) (by [@abhinavflac](https://x.com/abhinavflac))

**Inspect a voxel river landscape with reflections and changing weather.**

The author reports taking 2–3 times longer than Argon. This is an individual comparison without a common timing protocol.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112909984925372417-c80bf67ccd5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112909984925372417-5998d70a68db.jpg" alt="Voxel river and weather — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-9"></a>
### Case 9: [Voxel pagoda](https://x.com/LuminaBench/status/2112822997161562600) (by [@LuminaBench](https://x.com/LuminaBench))

**Inspect a detailed pagoda island through several lighting conditions.**

The creator reports being 2–4 times slower than Argon depending on the task. This estimate is not a measured model-wide latency claim. The same creator also places this pagoda beside three other model outputs. The comparison media retains the original labels and is grouped here rather than counted as another Carbon generation.

([@LuminaBench](https://x.com/LuminaBench/status/2112829559158800732))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112821820793434112-52372e9a3a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112821820793434112-b673916ea1e4.jpg" alt="Voxel pagoda — 1" width="560"></a><br>Watch source video</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112827630357516288-060bdc9c31b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112827630357516288-76711181a8a7.jpg" alt="Voxel pagoda — 2" width="560"></a><br>Watch the original model comparison</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-10"></a>
### Case 10: [Five-story pagoda](https://x.com/Mr_Salio/status/2112890002619142465) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Inspect a second pagoda output with animated lighting and close-up views.**

The video contains a different pagoda presentation from the LuminaBench example. Similar subject matter does not establish the same generation.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112889945530445824-a889d183dcfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112889945530445824-be4088fa4d3a.jpg" alt="Five-story pagoda — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-11"></a>
### Case 11: [Voxel lighthouse island](https://x.com/LuminaBench/status/2112844170209399118) (by [@LuminaBench](https://x.com/LuminaBench))

**Explore a lighthouse scene across daylight, nighttime and weather changes.**

The source praises voxel detail; sampled frames identify the concrete lighthouse scene. The prompt and code are not provided.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112841088444628992-40ce06ef4e5f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112841088444628992-86073f2c1e6c.jpg" alt="Voxel lighthouse island — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-12"></a>
### Case 12: [Mechanical kraken diorama](https://x.com/HarshithLucky3/status/2112882176912158877) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Inspect a brass mechanical kraken and submarine voxel scene.**

The source specifies a steampunk kraken, Victorian submarine and hydrothermal vent. It calls the Arena checkpoint Carbon despite the Argon display name.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112881879125053440-ed7a36ad009c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112881879125053440-ef964b2745cf.jpg" alt="Mechanical kraken diorama — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-13"></a>
### Case 13: [Sky railway city](https://x.com/SPAC89/status/2112849450993336595) (by [@SPAC89](https://x.com/SPAC89))

**Explore a fantastical rail scene with a train, elevated tracks and towers.**

The task is identified from the video rather than the generic caption. The caption's release prediction and model ranking are not evidence about this scene.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112848304245481472-f855a4ec4d26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112848304245481472-1988e3f7ab74.jpg" alt="Sky railway city — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="candidate-4"></a>
<a id="case-29"></a>
### Case 29: [Castle and dragon after follow-up prompts](https://x.com/semichenkko/status/2116198626187706722) (by [@semichenkko](https://x.com/semichenkko))

**Compare a castle-and-dragon scene before and after three follow-up prompts.**

The creator presents the same island, castle and dragon on the first prompt and after three more prompts, highlighting the fire effect. The follow-up text and execution logs are not provided; this is one author’s comparison, not a controlled success-rate test.

[Watch source video](https://x.com/semichenkko/status/2116198626187706722/video/1)

Type: Evaluation | Date: 2026-10-30

---

<a id="case-42"></a>
### Case 42: [Lantern River Night](https://x.com/pankajkumar_dev/status/2116533017934241886) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Explore a lantern-filled river scene through several recorded viewpoints.**

The creator describes a night scene with glowing lanterns and water reflections. Sampled frames show those elements and an add-lantern control; the application’s complete interaction was not tested.

[Watch source video](https://x.com/pankajkumar_dev/status/2116533017934241886/video/1)

Type: Demo | Date: 2026-10-31

---

<a id="case-43"></a>
### Case 43: [Sailing ship across three lighting states](https://x.com/srikanthvaluri/status/2116931901332369894) (by [@srikanthvaluri](https://x.com/srikanthvaluri))

**Inspect a sailing ship at daylight, sunset and night.**

The source requests a historical ship on the open sea with changing lighting. Sampled frames show a dark hull and white sails across those states; wave physics and model identity were not independently tested.

[Watch source video](https://x.com/srikanthvaluri/status/2116931901332369894/video/1)

Type: Demo | Date: 2026-11-01

---

<a id="case-44"></a>
### Case 44: [Red-hulled sailing ship](https://x.com/doe_naps/status/2116768227275788429) (by [@doe_naps](https://x.com/doe_naps))

**Explore another sailing-ship scene with a red hull and tan sails.**

Sampled frames show close and distant views with foam and birds. Its hull, trim and sails differ from the three-lighting-state ship; the creator’s Carbon attribution and full implementation remain unverified.

[Watch source video](https://x.com/doe_naps/status/2116768227275788429/video/1)

Type: Demo | Date: 2026-11-01

---

## 🎨 SVG and Interactive Graphics

<a id="case-14"></a>
### Case 14: [Cola bottle SVG](https://x.com/dummerspast39/status/2112999200472596959) (by [@dummerspast39](https://x.com/dummerspast39))

**Inspect a dimensional cola-bottle presentation described by its creator as SVG.**

The creator reports around five minutes in Arena. The recording shows the result, but the SVG implementation and comparison with Opus were not independently reproduced.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112998739115651072-36c11d258cd7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112998739115651072-92e3c1a11f11.jpg" alt="Cola bottle SVG — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-15"></a>
### Case 15: [Interactive PS5 controller](https://x.com/marcthecreatorr/status/2112894985267761333) (by [@marcthecreatorr](https://x.com/marcthecreatorr))

**Inspect a controller SVG with close-up and alternate display states.**

The author reports a long wait and claims Carbon was displayed as gemini-4-argon. The recording does not independently verify backend model identity.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112894899636862976-d5e2bb02aca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112894899636862976-279e5a90cd0e.jpg" alt="Interactive PS5 controller — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-16"></a>
### Case 16: [Xbox controller](https://x.com/Mr_Salio/status/2112842066501816466) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Inspect a detailed Xbox-style controller rendering.**

The source labels the result Carbon and claims an Argon display name in Arena. A later news-style post shows the same controller design and is grouped with this case.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg" alt="Xbox controller — 1" width="560"></a><br>Open source image</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg" alt="Xbox controller — 2" width="560"></a><br>Open source image</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-17"></a>
### Case 17: [Sports-car SVG](https://x.com/auricxofficial/status/2112902209608597810) (by [@auricxofficial](https://x.com/auricxofficial))

**Inspect a white sports-car side view and its detailed wheels and bodywork.**

The image shows the vehicle; a related tester calls it an SVG test. The sparse source does not supply runnable code or prove interactive behavior.

([@HarshithLucky3](https://x.com/HarshithLucky3/status/2112904832600477960))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg" alt="Sports-car SVG — 1" width="560"></a><br>Open source image</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-18"></a>
### Case 18: [Coastal pelican cyclist](https://x.com/dummerspast39/status/2112941964819595479) (by [@dummerspast39](https://x.com/dummerspast39))

**Inspect a pelican cyclist animation against a sunset waterfront.**

The source calls the output SVG. Its scene differs from the separate LuminaBench harbor version; neither is treated as a reproducible code delivery.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112941947727785984-a35fd5a8a21a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112941947727785984-ebb464917b8f.jpg" alt="Coastal pelican cyclist — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-19"></a>
### Case 19: [Four-season pelican cyclist](https://x.com/hamoudi_yo/status/2112933636093919333) (by [@hamoudi_yo](https://x.com/hamoudi_yo))

**Explore four seasonal presentations of a pelican riding a bicycle.**

The source explicitly describes a four-season SVG and names an Arena checkpoint displayed as Argon. Backend identification remains source-reported.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112933037528772609-fd19e0c4ed54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112933037528772609-ed8b4e1fd852.jpg" alt="Four-season pelican cyclist — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-20"></a>
### Case 20: [Pastel pelican cyclist](https://x.com/abhinavflac/status/2112825133052428378) (by [@abhinavflac](https://x.com/abhinavflac))

**Inspect wing movement in a pastel-colored pelican bicycle scene.**

The author highlights flapping wings and claws. Shared subject matter with other pelican tests does not imply a shared output.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112824858526814208-cadb280b19f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112824858526814208-57282e71a7ce.jpg" alt="Pastel pelican cyclist — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-21"></a>
### Case 21: [Harbor pelican and UI limits](https://x.com/LuminaBench/status/2112830849771004187) (by [@LuminaBench](https://x.com/LuminaBench))

**Inspect a harbor pelican SVG while considering usability and response time.**

The tester explicitly calls the UI poor and the generation very slow. Preserve these drawbacks alongside the visible animation.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112830075997507584-093a4bc78c90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112830075997507584-5f9cde944578.jpg" alt="Harbor pelican and UI limits — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Limit | Date: 2026-10-21

---

<a id="candidate-3"></a>
<a id="case-28"></a>
### Case 28: [Rain scene with a music loop](https://x.com/chetaslua/status/2115935747798950069) (by [@chetaslua](https://x.com/chetaslua))

**Explore the source’s JavaScript sleep-music loop with an SVG rain scene.**

The creator attributes the music and rain scene to Carbon and reports roughly 4,000 lines in one attempt. Code length, music originality and complete playback behavior have not been independently verified.

[Watch source video](https://x.com/chetaslua/status/2115935747798950069/video/1)

Type: Demo | Date: 2026-10-29

---

<a id="case-50"></a>
### Case 50: [Gemini merchandise storefront](https://www.youtube.com/watch?v=Y8FA5LhXLdo) (by [@Google](https://www.youtube.com/@Google))

**See how brand guidelines become a working storefront with custom visuals.**

Google built the storefront in Antigravity using its frontend design skill. The team attributes the storefront work to Gemini and the generated imagery to Nano Banana. The demo can be opened in AI Studio. It shows a working front end but does not establish a live checkout or fulfillment integration.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/merch-store-8d0b2b41c24f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/merch-store-poster-ce02af10b44d.jpg" alt="Gemini merchandise storefront — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-11-10

---

## 🎮 Games and Animated Scenes

<a id="case-22"></a>
### Case 22: [Super Mario-style platformer](https://x.com/LuminaBench/status/2112848294581813473) (by [@LuminaBench](https://x.com/LuminaBench))

**Inspect a platform game recording across outdoor and underground areas.**

The creator reports about 30 minutes and a successful first attempt. The recording does not verify every collision, level rule or restart path.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112846477709967360-9bcb4df969c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112846477709967360-99c390222b65.jpg" alt="Super Mario-style platformer — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-23"></a>
### Case 23: [Block-world sandbox](https://x.com/Haleeeemahh/status/2112871860094538053) (by [@Haleeeemahh](https://x.com/Haleeeemahh))

**Inspect a Minecraft-style first-person world with a block toolbar.**

Sampled frames show navigation and block placement. The source calls this a Carbon checkpoint in Arena under the Argon name; complete game logic was not tested.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112871560407097344-e1b7609246df.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112871560407097344-37726fd4c849.jpg" alt="Block-world sandbox — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-24"></a>
### Case 24: [Frog skateboard scene](https://x.com/SPAC89/status/2112845784500629765) (by [@SPAC89](https://x.com/SPAC89))

**Inspect an animated frog on a skateboard moving through a stylized scene.**

The concrete task is visible in the media despite a broad caption. The author's favorable speed impression is not a timed measurement.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112845628640251904-f1909c90d438.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112845628640251904-700f770e3a57.jpg" alt="Frog skateboard scene — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-10-21

---

<a id="case-35"></a>
### Case 35: [Minecraft-style game in about thirty minutes](https://x.com/dummerspast39/status/2116502497158201520) (by [@dummerspast39](https://x.com/dummerspast39))

**Explore a Minecraft-style game recording and its stated development constraints.**

The author reports roughly 30 minutes and approximately one attempt under a poor harness. No runnable project is provided here; interaction, stability and the author’s model ranking were not independently tested.

[Watch source video](https://x.com/dummerspast39/status/2116502497158201520/video/1)

Type: Demo | Date: 2026-10-31

---

<a id="case-37"></a>
### Case 37: [Three-dimensional racing game](https://x.com/Mr_Salio/status/2116798612361375995) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Inspect a car-racing demonstration attributed to a newer Carbon checkpoint.**

The creator reports a playable game built from one prompt in around 20 minutes. Checkpoint identity, complete asset provenance and playability were not independently verified; a recording alone does not establish a reproducible game.

[Watch source video](https://x.com/Mr_Salio/status/2116798612361375995/video/1)

Type: Demo | Date: 2026-11-01

---

<a id="case-45"></a>
### Case 45: [Pelican Quest campus game](https://www.youtube.com/watch?v=dNbkThtNzS8) (by [@Google](https://www.youtube.com/@Google))

**Inspect how a multi-agent workflow assembles an explorable campus game.**

Google reports using Antigravity swarm agents to build a Three.js and WebGL game with Blender assets, where a pelican rides a GBike around the Mountain View campus. The published recording shows the scene and its controls. It does not establish that the workflow is reproducible.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/pelican-playable-35bc725f2793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/pelican-poster-257b69c207e0.jpg" alt="Pelican Quest campus game — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Demo | Date: 2026-11-10

---

## 🔬 Model Comparison

<a id="case-25"></a>
### Case 25: [Bicycle animation across three models](https://x.com/AI_Screening/status/2112916947923087364) (by [@AI_Screening](https://x.com/AI_Screening))

**Compare the source's grouped Carbon, Argon and GPT-6 Astra bicycle outputs.**

The recording keeps the model labels and outputs together. The poster prefers Carbon, but shared settings, retries and execution logs are not supplied.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112916798039642113-7f04c4d03491.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112916798039642113-c1474c749e67.jpg" alt="Bicycle animation across three models — 1" width="560"></a><br>Watch source video</td></tr></table>

Type: Evaluation | Date: 2026-10-21

---

<a id="candidate-5"></a>
<a id="case-30"></a>
### Case 30: [Mechanical jaw across three models](https://x.com/noclipepe/status/2116109757865930787) (by [@noclipepe](https://x.com/noclipepe))

**Compare mechanical-jaw and moving-tooth demonstrations across Carbon, Opus 5.5 and GPT-6 Astra.**

The creator reports a common prompt and individual tooth movement, with times of 29m 9s for Carbon, 35m 17s for Opus 5.5 and 26m 7s for GPT-6 Astra. Timing, model identity and complete interaction remain source-reported and have not been independently reproduced.

[Watch source video](https://x.com/noclipepe/status/2116109757865930787/video/1)

Type: Evaluation | Date: 2026-10-30

---

<a id="case-31"></a>
### Case 31: [Nine-cylinder radial engine comparison](https://x.com/olezhavich/status/2116606788241969445) (by [@olezhavich](https://x.com/olezhavich))

**Compare cutaway clarity and engineering detail across four engine animations.**

The author reports a shared prompt and one attempt per model, preferring Carbon’s readability and Opus 5.5’s engineering detail. Firing-order correctness is the author’s assessment, not an independent check.

[Watch source video](https://x.com/olezhavich/status/2116606788241969445/video/1)

Type: Evaluation | Date: 2026-10-31

---

<a id="case-32"></a>
### Case 32: [Mechanical shark: speed versus internal detail](https://x.com/0xPorterio/status/2116548548334321967) (by [@0xPorterio](https://x.com/0xPorterio))

**Compare assembly effects with the internal structure of a dismantlable shark.**

The author describes Carbon as faster and more visually dramatic, but less detailed internally than Opus 5.5. The reported 77–90 score is a personal rubric; part counts and mechanical correctness remain unverified.

[Watch source video](https://x.com/0xPorterio/status/2116548548334321967/video/1)

Type: Limit | Date: 2026-10-31

---

<a id="case-36"></a>
### Case 36: [Zombie-hand animation: time and cost](https://x.com/noclipepe/status/2116445289468850366) (by [@noclipepe](https://x.com/noclipepe))

**Compare scene design alongside the reported time and cost of one animation task.**

The author reports Carbon at 1h 23m/$10.2, Opus 5.5 at 1h 6m/$8.1 and GPT-6 Astra at 24m/$5.7, while preferring Carbon’s scene. These are reported task bills, not API unit prices or independently verified costs.

[Watch source video](https://x.com/noclipepe/status/2116445289468850366/video/1)

Type: Evaluation | Date: 2026-10-31

---

<a id="case-38"></a>
### Case 38: [Two-stroke engine: unclear power stroke](https://x.com/olezhavich/status/2116892619309461745) (by [@olezhavich](https://x.com/olezhavich))

**Check whether an engine animation clearly explains combustion and piston movement.**

In a reported shared-prompt, one-attempt comparison of four models, the author finds Carbon’s flame difficult to see and prefers other outputs for explanation or realism. The judgment is task-specific; physics and repeatability were not independently tested.

[Watch source video](https://x.com/olezhavich/status/2116892619309461745/video/1)

Type: Limit | Date: 2026-11-01

---

<a id="case-40"></a>
### Case 40: [Haunted-house website comparison](https://x.com/keydol123/status/2116556350130163783) (by [@keydol123](https://x.com/keydol123))

**Compare the visual mood of two websites built for the same brief.**

The creator attributes the paired haunted-house websites to Carbon and Opus 5.5 using the same prompt. The cute-versus-frightening distinction is subjective; source code, accessibility and complete website behavior were not independently tested.

[Watch source video](https://x.com/keydol123/status/2116556350130163783/video/1)

Type: Evaluation | Date: 2026-10-31

---

<a id="case-46"></a>
### Case 46: [Multimodal Knowledge Agent benchmark](https://artificialanalysis.ai/articles/google-deepmind-multimodal-knowledge-agent) (by [@ArtificialAnalysis](https://artificialanalysis.ai/))

**Compare weighted rubric scores for visually complex documents and deliverables.**

Artificial Analysis and Google DeepMind evaluated agents on 200 private tasks across ten industries. The report gives Gemini 4 Carbon High 54% on weighted Climb criteria, compared with 57% for Claude Fable 5.2 Max and 53% for Claude Opus 5.5 Max. These figures describe the Stirrup harness and the stated rubric, not the share of tasks completed.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/mka-chart-75ea0faed82d.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/mka-chart-75ea0faed82d.png" alt="Multimodal Knowledge Agent benchmark — 1" width="560"></a><br>Open source image</td></tr></table>

Type: Benchmark | Date: 2026-11-10

---

<a id="related-repositories"></a>
## Related Repositories

- [Gemini 3.6 Flash — Guide and Use Cases](https://github.com/Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases)
- [Gemini Omni 1.2 Flash — Guide and Prompts](https://github.com/Evolink-AI/awesome-gemini-omni-1.2-flash-API-guide-and-prompt)

<a id="acknowledge"></a>
## 🙏 Acknowledge

Thanks to the publishers whose demonstrations make this collection possible:

[@thtbee_](https://x.com/thtbee_), [@hakmgpt](https://x.com/hakmgpt), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@dummerspast39](https://x.com/dummerspast39), [@Mr_Salio](https://x.com/Mr_Salio), [@doe_naps](https://x.com/doe_naps), [@abhinavflac](https://x.com/abhinavflac), [@LuminaBench](https://x.com/LuminaBench), [@HarshithLucky3](https://x.com/HarshithLucky3), [@SPAC89](https://x.com/SPAC89), [@marcthecreatorr](https://x.com/marcthecreatorr), [@auricxofficial](https://x.com/auricxofficial), [@hamoudi_yo](https://x.com/hamoudi_yo), [@Haleeeemahh](https://x.com/Haleeeemahh), [@AI_Screening](https://x.com/AI_Screening), [@noclipepe](https://x.com/noclipepe), [@dromexa](https://x.com/dromexa), [@chetaslua](https://x.com/chetaslua), [@semichenkko](https://x.com/semichenkko), [@olezhavich](https://x.com/olezhavich), [@0xPorterio](https://x.com/0xPorterio), [@keydol123](https://x.com/keydol123), [@srikanthvaluri](https://x.com/srikanthvaluri), [@Google](https://www.youtube.com/@Google), [@ArtificialAnalysis](https://artificialanalysis.ai/)

Attribution follows the linked sources and may need correction. Please open an issue for missing credit, duplicate work, inaccurate claims or removal requests. Third-party media retains its original ownership.
