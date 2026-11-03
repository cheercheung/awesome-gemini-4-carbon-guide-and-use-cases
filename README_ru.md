<div align="center">

<a href="https://evolink.ai?utm_source=github&utm_medium=banner&utm_campaign=gemini-4-carbon-usecases&utm_content=readme-cover"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/banner/banner-owner-6aea570af8a4.png" alt="Gemini 4 Carbon — Примеры использования сообщества" width="760"></a>

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

## 🍌 Введение

Коллекция публичных демонстраций сообщества, которые авторы приписывают Gemini 4 Carbon в период раннего развёртывания.

**Изучайте конкретные задачи, видимые результаты и практические ограничения по первоисточникам.**

## 📊 Обзор

44 примеров в 5 категориях. Повторные публикации объединены с соответствующей работой, а сравнения существующего результата оставлены в том же примере.

> [!NOTE]
> Названия моделей, время генерации и оценки качества сообщены источниками. Имя в Arena не доказывает версию серверной модели. Запись не подтверждает исполняемый код, правильность всех взаимодействий или повторяемость успеха.

<a id="quick-start"></a>
## ⚡ Быстрый старт

1. Выберите задачу в содержании.
2. Откройте видео или изображение и перейдите к исходной публикации по заголовку.
3. Сопоставьте видимый результат с задачей и ограничениями.

## 📑 Содержание

| Пример | Категория | Тип |
|---|---|---|
| [1. Механический цветок](#case-1) | Механические и трёхмерные объекты | Demo |
| [2. Механическая пчела](#case-2) | Механические и трёхмерные объекты | Demo |
| [3. Механические существа и паутина](#case-3) | Механические и трёхмерные объекты | Demo |
| [4. Хрустальный цитрус](#case-4) | Механические и трёхмерные объекты | Demo |
| [5. Хогвартс из вокселей](#case-5) | Воксельные миры и пейзажи | Demo |
| [6. Воксельный замок и пейзаж](#case-6) | Воксельные миры и пейзажи | Demo |
| [7. Сад Фудзи](#case-7) | Воксельные миры и пейзажи | Demo |
| [8. Воксельная река и погода](#case-8) | Воксельные миры и пейзажи | Demo |
| [9. Воксельная пагода](#case-9) | Воксельные миры и пейзажи | Demo |
| [10. Пятиэтажная воксельная пагода](#case-10) | Воксельные миры и пейзажи | Demo |
| [11. Воксельный остров с маяком](#case-11) | Воксельные миры и пейзажи | Demo |
| [12. Диорама механического кракена](#case-12) | Воксельные миры и пейзажи | Demo |
| [13. Небесный железнодорожный город](#case-13) | Воксельные миры и пейзажи | Demo |
| [14. Бутылка колы в SVG](#case-14) | SVG и интерактивная графика | Demo |
| [15. Интерактивный контроллер PS5](#case-15) | SVG и интерактивная графика | Demo |
| [16. Контроллер в стиле Xbox](#case-16) | SVG и интерактивная графика | Demo |
| [17. Спортивная машина в SVG](#case-17) | SVG и интерактивная графика | Demo |
| [18. Пеликан-велосипедист на закате](#case-18) | SVG и интерактивная графика | Demo |
| [19. Пеликан-велосипедист в четырёх сезонах](#case-19) | SVG и интерактивная графика | Demo |
| [20. Пеликан-велосипедист в пастельных тонах](#case-20) | SVG и интерактивная графика | Demo |
| [21. Пеликан в порту и ограничения интерфейса](#case-21) | SVG и интерактивная графика | Limit |
| [22. Платформер в стиле Super Mario](#case-22) | Игры и анимированные сцены | Demo |
| [23. Песочница из блоков](#case-23) | Игры и анимированные сцены | Demo |
| [24. Лягушка на скейтборде](#case-24) | Игры и анимированные сцены | Demo |
| [25. Велосипедная анимация трёх моделей](#case-25) | Сравнение моделей | Evaluation |
| [26. Роботизированный глаз с разнесённым видом](#case-26) | Механические и трёхмерные объекты | Demo |
| [27. Осмотр кафе-рейсера двумя моделями](#case-27) | Механические и трёхмерные объекты | Evaluation |
| [28. Дождевая сцена с музыкальным циклом](#case-28) | SVG и интерактивная графика | Demo |
| [29. Замок и дракон после дополнительных запросов](#case-29) | Воксельные миры и пейзажи | Evaluation |
| [30. Механическая челюсть у трёх моделей](#case-30) | Сравнение моделей | Evaluation |
| [31. Сравнение девятицилиндрового звездообразного двигателя](#case-31) | Сравнение моделей | Evaluation |
| [32. Механическая акула: скорость и внутренние детали](#case-32) | Сравнение моделей | Limit |
| [33. Осмотр двигателя V8 в двух моделях](#case-33) | Механические и трёхмерные объекты | Evaluation |
| [34. Бутылка колы в одном шейдере](#case-34) | Механические и трёхмерные объекты | Demo |
| [35. Игра в стиле Minecraft примерно за полчаса](#case-35) | Игры и анимированные сцены | Demo |
| [36. Анимация руки зомби: время и стоимость](#case-36) | Сравнение моделей | Evaluation |
| [37. Трёхмерная гоночная игра](#case-37) | Игры и анимированные сцены | Demo |
| [38. Двухтактный двигатель: неясный рабочий ход](#case-38) | Сравнение моделей | Limit |
| [39. Осмотр механических часов в двух моделях](#case-39) | Механические и трёхмерные объекты | Evaluation |
| [40. Сравнение сайтов домов с привидениями](#case-40) | Сравнение моделей | Evaluation |
| [41. Механический орёл с двумя метками моделей](#case-41) | Механические и трёхмерные объекты | Evaluation |
| [42. Ночная река с фонарями](#case-42) | Воксельные миры и пейзажи | Demo |
| [43. Парусник при трёх вариантах освещения](#case-43) | Воксельные миры и пейзажи | Demo |
| [44. Парусник с красным корпусом](#case-44) | Воксельные миры и пейзажи | Demo |

## ⚙️ Механические и трёхмерные объекты

<a id="case-1"></a>
### Пример 1: [Механический цветок](https://x.com/thtbee_/status/2112935205703147750) (автор [@thtbee_](https://x.com/thtbee_))

**Изучите материалы, освещение и маленькую пчелу у цветка в three.js.**

Автор сообщает примерно о 1 часе 43 минутах и объясняет добавление пчелы открытым заданием. Время указано самим автором.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112929911149371392-e21290e5e3a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112929911149371392-e771176b9f52.jpg" alt="Механический цветок — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-2"></a>
### Пример 2: [Механическая пчела](https://x.com/thtbee_/status/2112971691966267827) (автор [@thtbee_](https://x.com/thtbee_))

**Изучите анимацию механической пчелы и движение восьмёркой.**

Автор отмечает лучшую проработку, чем у Argon, и ссылается на прежний тест. Общего хронометража и доли успешных попыток нет.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112971150624276481-08802f1fd200.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112971150624276481-37af1edb658b.jpg" alt="Механическая пчела — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-3"></a>
### Пример 3: [Механические существа и паутина](https://x.com/hakmgpt/status/2112999946777719116) (автор [@hakmgpt](https://x.com/hakmgpt))

**Изучите последовательность с механическими существами, паутиной и крылатым устройством.**

Три выбранных кадра показывают разные сцены. Короткая подпись не устанавливает задания, процесс или принадлежность к одной генерации.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112997765458309120-c7d3c185b9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112997765458309120-bc5f3191664e.jpg" alt="Механические существа и паутина — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-4"></a>
### Пример 4: [Хрустальный цитрус](https://x.com/pankajkumar_dev/status/2112946681977430469) (автор [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Изучите слои, освещение и анимированные ракурсы интерактивного цитруса.**

Автор сообщает о примерно 20 минутах и имени gemini-4-argon в Arena. Идентификация как Carbon является его утверждением.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112945233822617600-6e32038ca6b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112945233822617600-ada2f593eab5.jpg" alt="Хрустальный цитрус — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="pending-candidates"></a>
<a id="candidate-1"></a>
<a id="case-26"></a>
### Пример 26: [Роботизированный глаз с разнесённым видом](https://x.com/noclipepe/status/2115556254101692515) (автор [@noclipepe](https://x.com/noclipepe))

**Изучите демонстрацию роботизированного глаза с морганием, фокусировкой и разнесённым видом деталей.**

Автор сообщает об одном запросе и времени 29 минут 49 секунд. Дана ссылка на исходную запись; исполняемый код, полное взаимодействие и повторяемость независимо не проверены.

[Смотреть исходное видео](https://x.com/noclipepe/status/2115556254101692515/video/1)

Тип: Demo | Дата: 2026-10-28

---

<a id="candidate-2"></a>
<a id="case-27"></a>
### Пример 27: [Осмотр кафе-рейсера двумя моделями](https://x.com/dromexa/status/2115802517942497491) (автор [@dromexa](https://x.com/dromexa))

**Сравните демонстрации осмотра мотоцикла, которые источник приписывает Carbon и Opus 5.5.**

Публикатор сообщает об одинаковом запросе и одной попытке на модель для рентгеновского вида, разреза и разнесённого вида. Условия заявлены источником; общих журналов выполнения или независимого воспроизведения для общего рейтинга моделей нет.

[Смотреть исходное видео](https://x.com/dromexa/status/2115802517942497491/video/1)

Тип: Evaluation | Дата: 2026-10-29

---

<a id="case-33"></a>
### Пример 33: [Осмотр двигателя V8 в двух моделях](https://x.com/dromexa/status/2116927253980594275) (автор [@dromexa](https://x.com/dromexa))

**Изучите рентгеновские, разрезные, разнесённые и подетальные виды двигателя.**

Автор сообщает об одинаковом запросе и одной попытке для Carbon и Opus 5.5. Заявленные три победы подряд — личное суждение; исполняемый код и механическая точность независимо не проверялись.

[Смотреть исходное видео](https://x.com/dromexa/status/2116927253980594275/video/1)

Тип: Evaluation | Дата: 2026-11-01

---

<a id="case-34"></a>
### Пример 34: [Бутылка колы в одном шейдере](https://x.com/dummerspast39/status/2116470583097438519) (автор [@dummerspast39](https://x.com/dummerspast39))

**Изучите бутылку Three.js, представленную как математическая геометрия шейдера.**

Автор сообщает об отсутствии внешних моделей и ресурсов и о 21 зубце крышки. Эта демонстрация шейдера отличается от прежней SVG-бутылки; код, зависимости ресурсов и число зубцов независимо не проверялись.

[Смотреть исходное видео](https://x.com/dummerspast39/status/2116470583097438519/video/1)

Тип: Demo | Дата: 2026-10-31

---

<a id="case-39"></a>
### Пример 39: [Осмотр механических часов в двух моделях](https://x.com/dromexa/status/2116518366919667775) (автор [@dromexa](https://x.com/dromexa))

**Изучите рентгеновские, разрезные и разнесённые виды часов.**

Автор сообщает об одинаковом запросе и одной попытке для Carbon и Opus 5.5, колеблющемся балансе и правильной скорости шестерён. Передаточные отношения и точность хода независимо не проверялись.

[Смотреть исходное видео](https://x.com/dromexa/status/2116518366919667775/video/1)

Тип: Evaluation | Дата: 2026-10-31

---

<a id="case-41"></a>
### Пример 41: [Механический орёл с двумя метками моделей](https://x.com/srikanthvaluri/status/2116767284618486044) (автор [@srikanthvaluri](https://x.com/srikanthvaluri))

**Сравните механических орлов с метками Carbon и Argon в источнике.**

Кадры показывают разные конструкции, положения крыльев и ракурсы. Автор просит механического орла на Three.js; идентичность моделей и работа механики остаются заявлениями источника.

[Смотреть исходное видео](https://x.com/srikanthvaluri/status/2116767284618486044/video/1)

Тип: Evaluation | Дата: 2026-11-01

---

## 🏞️ Воксельные миры и пейзажи

<a id="case-5"></a>
### Пример 5: [Хогвартс из вокселей](https://x.com/dummerspast39/status/2112989454239416450) (автор [@dummerspast39](https://x.com/dummerspast39))

**Исследуйте внутренние и внешние виды воксельного замка.**

Источник явно указывает best of 4. Это выбранный результат, а не доказательство успеха с первой попытки.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112989347301519360-99b7308b4b0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112989347301519360-42c02806db71.jpg" alt="Хогвартс из вокселей — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-6"></a>
### Пример 6: [Воксельный замок и пейзаж](https://x.com/Mr_Salio/status/2112856590386643413) (автор [@Mr_Salio](https://x.com/Mr_Salio))

**Рассмотрите замок днём, ночью и с воздуха.**

Видео показывает другой результат с замком. Сравнение с Opus — мнение без контролируемого теста и описания генерации.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112856348719210496-a57ed12eb899.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112856348719210496-b6b5dc0a31f6.jpg" alt="Воксельный замок и пейзаж — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-7"></a>
### Пример 7: [Сад Фудзи](https://x.com/doe_naps/status/2112975635337593132) (автор [@doe_naps](https://x.com/doe_naps))

**Исследуйте миниатюрный японский сад, в том числе с точки зрения бабочки.**

Источник описывает отражения и движущихся людей. Кадры показывают несколько ракурсов; все взаимодействия не проверялись.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112972423893221376-421aa3046fa3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112972423893221376-a5bc633b97f3.jpg" alt="Сад Фудзи — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-8"></a>
### Пример 8: [Воксельная река и погода](https://x.com/abhinavflac/status/2112910206644756745) (автор [@abhinavflac](https://x.com/abhinavflac))

**Изучите отражения и смену погоды в воксельной долине.**

Автор сообщает о времени в 2–3 раза больше, чем у Argon. Это личное сравнение без общего протокола измерения.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112909984925372417-c80bf67ccd5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112909984925372417-5998d70a68db.jpg" alt="Воксельная река и погода — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-9"></a>
### Пример 9: [Воксельная пагода](https://x.com/LuminaBench/status/2112822997161562600) (автор [@LuminaBench](https://x.com/LuminaBench))

**Рассмотрите остров с пагодой при разном освещении.**

Автор сообщает о замедлении в 2–4 раза в зависимости от задачи, а не об общей измеренной задержке модели. Его сравнение с тремя другими моделями сохранено здесь с исходными подписями и не считается новой генерацией Carbon.

([@LuminaBench](https://x.com/LuminaBench/status/2112829559158800732))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112821820793434112-52372e9a3a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112821820793434112-b673916ea1e4.jpg" alt="Воксельная пагода — 1" width="560"></a><br>Смотреть исходное видео</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112827630357516288-060bdc9c31b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112827630357516288-76711181a8a7.jpg" alt="Воксельная пагода — 2" width="560"></a><br>Смотреть исходное сравнение моделей</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-10"></a>
### Пример 10: [Пятиэтажная воксельная пагода](https://x.com/Mr_Salio/status/2112890002619142465) (автор [@Mr_Salio](https://x.com/Mr_Salio))

**Изучите другую пагоду с анимированным светом и крупными планами.**

Показ отличается от примера LuminaBench. Одинаковая тема не доказывает одну генерацию.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112889945530445824-a889d183dcfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112889945530445824-be4088fa4d3a.jpg" alt="Пятиэтажная воксельная пагода — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-11"></a>
### Пример 11: [Воксельный остров с маяком](https://x.com/LuminaBench/status/2112844170209399118) (автор [@LuminaBench](https://x.com/LuminaBench))

**Изучите маяк при смене дня, ночи и погоды.**

Источник хвалит детализацию вокселей. Кадры позволяют узнать маяк, но код и полные входные инструкции не предоставлены.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112841088444628992-40ce06ef4e5f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112841088444628992-86073f2c1e6c.jpg" alt="Воксельный остров с маяком — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-12"></a>
### Пример 12: [Диорама механического кракена](https://x.com/HarshithLucky3/status/2112882176912158877) (автор [@HarshithLucky3](https://x.com/HarshithLucky3))

**Рассмотрите латунного кракена и подлодку в воксельной сцене.**

Источник задаёт стимпанк-кракена, викторианскую подлодку и гидротермальный источник. Чекпойнт Arena с именем Argon он называет Carbon.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112881879125053440-ed7a36ad009c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112881879125053440-ef964b2745cf.jpg" alt="Диорама механического кракена — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-13"></a>
### Пример 13: [Небесный железнодорожный город](https://x.com/SPAC89/status/2112849450993336595) (автор [@SPAC89](https://x.com/SPAC89))

**Исследуйте фантастическую сцену с поездом, высокими путями и башнями.**

Задача определена по видео, а не общей подписи. Прогнозы выхода и места моделей не доказывают качество этой сцены.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112848304245481472-f855a4ec4d26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112848304245481472-1988e3f7ab74.jpg" alt="Небесный железнодорожный город — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="candidate-4"></a>
<a id="case-29"></a>
### Пример 29: [Замок и дракон после дополнительных запросов](https://x.com/semichenkko/status/2116198626187706722) (автор [@semichenkko](https://x.com/semichenkko))

**Сравните сцену с замком и драконом до и после трёх дополнительных запросов.**

Автор показывает тот же остров, замок и дракона после первого запроса и ещё трёх, выделяя эффект огня. Текст дополнительных запросов и журналы выполнения не предоставлены; это сравнение одного автора, а не контролируемый тест доли успешных попыток.

[Смотреть исходное видео](https://x.com/semichenkko/status/2116198626187706722/video/1)

Тип: Evaluation | Дата: 2026-10-30

---

<a id="case-42"></a>
### Пример 42: [Ночная река с фонарями](https://x.com/pankajkumar_dev/status/2116533017934241886) (автор [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Изучите реку, полную фонарей, с нескольких записанных ракурсов.**

Автор описывает ночную сцену со светящимися фонарями и отражениями. Кадры показывают эти элементы и кнопку добавления фонаря; полное взаимодействие с приложением не тестировалось.

[Смотреть исходное видео](https://x.com/pankajkumar_dev/status/2116533017934241886/video/1)

Тип: Demo | Дата: 2026-10-31

---

<a id="case-43"></a>
### Пример 43: [Парусник при трёх вариантах освещения](https://x.com/srikanthvaluri/status/2116931901332369894) (автор [@srikanthvaluri](https://x.com/srikanthvaluri))

**Изучите парусник днём, на закате и ночью.**

Источник просит исторический корабль в открытом море с меняющимся освещением. Кадры показывают тёмный корпус и белые паруса в этих состояниях; физика волн и идентичность модели независимо не тестировались.

[Смотреть исходное видео](https://x.com/srikanthvaluri/status/2116931901332369894/video/1)

Тип: Demo | Дата: 2026-11-01

---

<a id="case-44"></a>
### Пример 44: [Парусник с красным корпусом](https://x.com/doe_naps/status/2116768227275788429) (автор [@doe_naps](https://x.com/doe_naps))

**Изучите другую сцену парусника с красным корпусом и бежевыми парусами.**

Кадры показывают близкие и дальние виды с пеной и птицами. Корпус, отделка и паруса отличаются от корабля с тремя освещениями; атрибуция Carbon и полная реализация независимо не подтверждены.

[Смотреть исходное видео](https://x.com/doe_naps/status/2116768227275788429/video/1)

Тип: Demo | Дата: 2026-11-01

---

## 🎨 SVG и интерактивная графика

<a id="case-14"></a>
### Пример 14: [Бутылка колы в SVG](https://x.com/dummerspast39/status/2112999200472596959) (автор [@dummerspast39](https://x.com/dummerspast39))

**Рассмотрите объёмную бутылку, которую автор описывает как SVG.**

Автор сообщает о примерно пяти минутах в Arena. Запись показывает результат, но реализация SVG и сравнение с Opus независимо не воспроизводились.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112998739115651072-36c11d258cd7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112998739115651072-92e3c1a11f11.jpg" alt="Бутылка колы в SVG — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-15"></a>
### Пример 15: [Интерактивный контроллер PS5](https://x.com/marcthecreatorr/status/2112894985267761333) (автор [@marcthecreatorr](https://x.com/marcthecreatorr))

**Изучите крупные планы и разные состояния SVG-контроллера.**

Автор сообщает о долгом ожидании и Carbon под именем gemini-4-argon. Запись не подтверждает серверную модель независимо.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112894899636862976-d5e2bb02aca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112894899636862976-279e5a90cd0e.jpg" alt="Интерактивный контроллер PS5 — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-16"></a>
### Пример 16: [Контроллер в стиле Xbox](https://x.com/Mr_Salio/status/2112842066501816466) (автор [@Mr_Salio](https://x.com/Mr_Salio))

**Рассмотрите детальный контроллер в стиле Xbox.**

Источник называет результат Carbon и утверждает, что Arena показывала Argon. Более поздняя новостная публикация с тем же дизайном объединена с этим примером.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112842052165595136-ac213e72a7f7.jpg" alt="Контроллер в стиле Xbox — 1" width="560"></a><br>Открыть исходное изображение</td><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112852360112537600-4826d3455e74.jpg" alt="Контроллер в стиле Xbox — 2" width="560"></a><br>Открыть исходное изображение</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-17"></a>
### Пример 17: [Спортивная машина в SVG](https://x.com/auricxofficial/status/2112902209608597810) (автор [@auricxofficial](https://x.com/auricxofficial))

**Рассмотрите колёса и кузов белой спортивной машины сбоку.**

На изображении видна машина, а связанный тестировщик называет работу SVG-тестом. Исполняемого кода и доказательства интерактивности нет.

([@HarshithLucky3](https://x.com/HarshithLucky3/status/2112904832600477960))

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/images/2112901971741192192-d811b3b3b505.jpg" alt="Спортивная машина в SVG — 1" width="560"></a><br>Открыть исходное изображение</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-18"></a>
### Пример 18: [Пеликан-велосипедист на закате](https://x.com/dummerspast39/status/2112941964819595479) (автор [@dummerspast39](https://x.com/dummerspast39))

**Посмотрите анимацию пеликана у берега на закате.**

Источник называет результат SVG. Сцена отличается от портовой версии LuminaBench; ни одна не считается воспроизводимой поставкой кода.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112941947727785984-a35fd5a8a21a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112941947727785984-ebb464917b8f.jpg" alt="Пеликан-велосипедист на закате — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-19"></a>
### Пример 19: [Пеликан-велосипедист в четырёх сезонах](https://x.com/hamoudi_yo/status/2112933636093919333) (автор [@hamoudi_yo](https://x.com/hamoudi_yo))

**Изучите четыре сезонных варианта пеликана на велосипеде.**

Источник явно указывает SVG четырёх сезонов и имя Argon в Arena. Серверная идентичность остаётся утверждением источника.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112933037528772609-fd19e0c4ed54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112933037528772609-ed8b4e1fd852.jpg" alt="Пеликан-велосипедист в четырёх сезонах — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-20"></a>
### Пример 20: [Пеликан-велосипедист в пастельных тонах](https://x.com/abhinavflac/status/2112825133052428378) (автор [@abhinavflac](https://x.com/abhinavflac))

**Изучите движение крыльев в пастельной велосипедной сцене.**

Автор выделяет взмахи крыльев и когти. Общая тема с другими тестами не означает тот же результат.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112824858526814208-cadb280b19f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112824858526814208-57282e71a7ce.jpg" alt="Пеликан-велосипедист в пастельных тонах — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-21"></a>
### Пример 21: [Пеликан в порту и ограничения интерфейса](https://x.com/LuminaBench/status/2112830849771004187) (автор [@LuminaBench](https://x.com/LuminaBench))

**Рассмотрите портовый SVG с учётом удобства и времени ответа.**

Тестировщик прямо критикует интерфейс и очень медленную генерацию. Недостатки сохранены рядом с видимой анимацией.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112830075997507584-093a4bc78c90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112830075997507584-5f9cde944578.jpg" alt="Пеликан в порту и ограничения интерфейса — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Limit | Дата: 2026-10-21

---

<a id="candidate-3"></a>
<a id="case-28"></a>
### Пример 28: [Дождевая сцена с музыкальным циклом](https://x.com/chetaslua/status/2115935747798950069) (автор [@chetaslua](https://x.com/chetaslua))

**Изучите представленный источником цикл музыки для сна на JavaScript со сценой дождя в SVG.**

Автор приписывает музыку и сцену Carbon и сообщает примерно о 4 000 строках за одну попытку. Объём кода, оригинальность музыки и полная работа воспроизведения независимо не проверены.

[Смотреть исходное видео](https://x.com/chetaslua/status/2115935747798950069/video/1)

Тип: Demo | Дата: 2026-10-29

---

## 🎮 Игры и анимированные сцены

<a id="case-22"></a>
### Пример 22: [Платформер в стиле Super Mario](https://x.com/LuminaBench/status/2112848294581813473) (автор [@LuminaBench](https://x.com/LuminaBench))

**Изучите запись игры с наземными и подземными участками.**

Автор сообщает примерно о 30 минутах и успехе с первой попытки. Запись не проверяет все столкновения, правила и пути перезапуска.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112846477709967360-9bcb4df969c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112846477709967360-99c390222b65.jpg" alt="Платформер в стиле Super Mario — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-23"></a>
### Пример 23: [Песочница из блоков](https://x.com/Haleeeemahh/status/2112871860094538053) (автор [@Haleeeemahh](https://x.com/Haleeeemahh))

**Рассмотрите мир от первого лица в стиле Minecraft с панелью блоков.**

Кадры показывают перемещение и установку блоков. Источник называет модель Carbon под именем Argon; вся игровая логика не тестировалась.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112871560407097344-e1b7609246df.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112871560407097344-37726fd4c849.jpg" alt="Песочница из блоков — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-24"></a>
### Пример 24: [Лягушка на скейтборде](https://x.com/SPAC89/status/2112845784500629765) (автор [@SPAC89](https://x.com/SPAC89))

**Посмотрите анимацию лягушки на скейтборде в стилизованной сцене.**

Несмотря на общую подпись, задача видна в видео. Положительное впечатление от скорости не является измерением.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112845628640251904-f1909c90d438.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112845628640251904-700f770e3a57.jpg" alt="Лягушка на скейтборде — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Demo | Дата: 2026-10-21

---

<a id="case-35"></a>
### Пример 35: [Игра в стиле Minecraft примерно за полчаса](https://x.com/dummerspast39/status/2116502497158201520) (автор [@dummerspast39](https://x.com/dummerspast39))

**Изучите запись игры в стиле Minecraft и заявленные условия разработки.**

Автор сообщает примерно о 30 минутах и приблизительно одной попытке в неудачной среде запуска агента. Исполняемый проект здесь не предоставлен; взаимодействие, стабильность и рейтинг моделей автора независимо не тестировались.

[Смотреть исходное видео](https://x.com/dummerspast39/status/2116502497158201520/video/1)

Тип: Demo | Дата: 2026-10-31

---

<a id="case-37"></a>
### Пример 37: [Трёхмерная гоночная игра](https://x.com/Mr_Salio/status/2116798612361375995) (автор [@Mr_Salio](https://x.com/Mr_Salio))

**Изучите демонстрацию гонок, приписанную более новому чекпойнту Carbon.**

Автор сообщает о создании игры одним запросом примерно за 20 минут. Идентичность чекпойнта, полное происхождение ресурсов и играбельность независимо не проверялись; запись сама по себе не доказывает воспроизводимость игры.

[Смотреть исходное видео](https://x.com/Mr_Salio/status/2116798612361375995/video/1)

Тип: Demo | Дата: 2026-11-01

---

## 🔬 Сравнение моделей

<a id="case-25"></a>
### Пример 25: [Велосипедная анимация трёх моделей](https://x.com/AI_Screening/status/2112916947923087364) (автор [@AI_Screening](https://x.com/AI_Screening))

**Сравните совместно показанные результаты Carbon, Argon и GPT-6 Astra.**

Видео сохраняет исходные подписи вместе с результатами. Автор предпочитает Carbon, но не предоставляет общих настроек, числа повторов и журналов выполнения.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112916798039642113-7f04c4d03491.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112916798039642113-c1474c749e67.jpg" alt="Велосипедная анимация трёх моделей — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Evaluation | Дата: 2026-10-21

---

<a id="candidate-5"></a>
<a id="case-30"></a>
### Пример 30: [Механическая челюсть у трёх моделей](https://x.com/noclipepe/status/2116109757865930787) (автор [@noclipepe](https://x.com/noclipepe))

**Сравните демонстрации механической челюсти и подвижных зубов у Carbon, Opus 5.5 и GPT-6 Astra.**

Автор сообщает об общем запросе и независимом движении зубов, указывая время 29m 9s для Carbon, 35m 17s для Opus 5.5 и 26m 7s для GPT-6 Astra. Время, идентичность моделей и полное взаимодействие остаются заявлениями источника без независимого воспроизведения.

[Смотреть исходное видео](https://x.com/noclipepe/status/2116109757865930787/video/1)

Тип: Evaluation | Дата: 2026-10-30

---

<a id="case-31"></a>
### Пример 31: [Сравнение девятицилиндрового звездообразного двигателя](https://x.com/olezhavich/status/2116606788241969445) (автор [@olezhavich](https://x.com/olezhavich))

**Сравните наглядность разрезов и инженерные детали четырёх анимаций двигателей.**

Автор сообщает об одинаковом запросе и одной попытке на модель, предпочитая наглядность Carbon и инженерные детали Opus 5.5. Правильный порядок зажигания — оценка автора, без независимой проверки.

[Смотреть исходное видео](https://x.com/olezhavich/status/2116606788241969445/video/1)

Тип: Evaluation | Дата: 2026-10-31

---

<a id="case-32"></a>
### Пример 32: [Механическая акула: скорость и внутренние детали](https://x.com/0xPorterio/status/2116548548334321967) (автор [@0xPorterio](https://x.com/0xPorterio))

**Сравните эффекты сборки с внутренним устройством разборной акулы.**

По словам автора, Carbon быстрее и эффектнее, но уступает Opus 5.5 в детализации внутренних механизмов. Счёт 77–90 основан на личной шкале; число деталей и механическая корректность не проверены.

[Смотреть исходное видео](https://x.com/0xPorterio/status/2116548548334321967/video/1)

Тип: Limit | Дата: 2026-10-31

---

<a id="case-36"></a>
### Пример 36: [Анимация руки зомби: время и стоимость](https://x.com/noclipepe/status/2116445289468850366) (автор [@noclipepe](https://x.com/noclipepe))

**Сопоставьте оформление сцены с заявленными временем и затратами одной задачи анимации.**

Автор сообщает: Carbon — 1h 23m/$10.2, Opus 5.5 — 1h 6m/$8.1, GPT-6 Astra — 24m/$5.7, предпочитая сцену Carbon. Это заявленные расходы на задачу, а не тарифы API или независимо подтверждённые затраты.

[Смотреть исходное видео](https://x.com/noclipepe/status/2116445289468850366/video/1)

Тип: Evaluation | Дата: 2026-10-31

---

<a id="case-38"></a>
### Пример 38: [Двухтактный двигатель: неясный рабочий ход](https://x.com/olezhavich/status/2116892619309461745) (автор [@olezhavich](https://x.com/olezhavich))

**Проверьте, насколько ясно анимация объясняет сгорание и движение поршня.**

В заявленном сравнении четырёх моделей с одинаковым запросом и одной попыткой автор считает пламя Carbon плохо заметным и предпочитает другие результаты по наглядности или реализму. Оценка относится к этой задаче; физика и повторяемость независимо не тестировались.

[Смотреть исходное видео](https://x.com/olezhavich/status/2116892619309461745/video/1)

Тип: Limit | Дата: 2026-11-01

---

<a id="case-40"></a>
### Пример 40: [Сравнение сайтов домов с привидениями](https://x.com/keydol123/status/2116556350130163783) (автор [@keydol123](https://x.com/keydol123))

**Сравните визуальную атмосферу двух сайтов, созданных по одному заданию.**

Автор приписывает два сайта Carbon и Opus 5.5 с одинаковым запросом. Различие между милым и страшным субъективно; исходный код, доступность и полное поведение сайтов независимо не тестировались.

[Смотреть исходное видео](https://x.com/keydol123/status/2116556350130163783/video/1)

Тип: Evaluation | Дата: 2026-10-31

---

<a id="related-repositories"></a>
## Связанные репозитории

- [Gemini 3.6 Flash — Руководство и примеры использования](https://github.com/Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases)
- [Gemini Omni — Руководство и запросы](https://github.com/Evolink-AI/awesome-gemini-omni-guide-api-and-prompt)

<a id="acknowledge"></a>
## 🙏 Благодарности

Спасибо авторам, опубликовавшим эти демонстрации:

[@thtbee_](https://x.com/thtbee_), [@hakmgpt](https://x.com/hakmgpt), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@dummerspast39](https://x.com/dummerspast39), [@Mr_Salio](https://x.com/Mr_Salio), [@doe_naps](https://x.com/doe_naps), [@abhinavflac](https://x.com/abhinavflac), [@LuminaBench](https://x.com/LuminaBench), [@HarshithLucky3](https://x.com/HarshithLucky3), [@SPAC89](https://x.com/SPAC89), [@marcthecreatorr](https://x.com/marcthecreatorr), [@auricxofficial](https://x.com/auricxofficial), [@hamoudi_yo](https://x.com/hamoudi_yo), [@Haleeeemahh](https://x.com/Haleeeemahh), [@AI_Screening](https://x.com/AI_Screening), [@noclipepe](https://x.com/noclipepe), [@dromexa](https://x.com/dromexa), [@chetaslua](https://x.com/chetaslua), [@semichenkko](https://x.com/semichenkko), [@olezhavich](https://x.com/olezhavich), [@0xPorterio](https://x.com/0xPorterio), [@keydol123](https://x.com/keydol123), [@srikanthvaluri](https://x.com/srikanthvaluri)

Атрибуция следует связанным источникам и может нуждаться в исправлении. Сообщайте через issue о пропущенных авторах, дубликатах, неверных утверждениях или просьбах об удалении. Права на сторонние материалы остаются у их владельцев.
