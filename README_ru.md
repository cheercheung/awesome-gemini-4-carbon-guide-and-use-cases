<div align="center">

<a href="https://evolink.ai?utm_source=github&utm_medium=banner&utm_campaign=gemini-4-carbon-usecases&utm_content=readme-cover"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/banner/banner-b55a8eaa373d.svg" alt="Gemini 4 Carbon — Примеры использования сообщества" width="760"></a>

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

25 примеров в 5 категориях. Повторные публикации объединены с соответствующей работой, а сравнения существующего результата оставлены в том же примере.

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

## 🔬 Сравнение моделей

<a id="case-25"></a>
### Пример 25: [Велосипедная анимация трёх моделей](https://x.com/AI_Screening/status/2112916947923087364) (автор [@AI_Screening](https://x.com/AI_Screening))

**Сравните совместно показанные результаты Carbon, Argon и GPT-6 Astra.**

Видео сохраняет исходные подписи вместе с результатами. Автор предпочитает Carbon, но не предоставляет общих настроек, числа повторов и журналов выполнения.

<table><tr><td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/videos/2112916798039642113-7f04c4d03491.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases/posters/2112916798039642113-c1474c749e67.jpg" alt="Велосипедная анимация трёх моделей — 1" width="560"></a><br>Смотреть исходное видео</td></tr></table>

Тип: Evaluation | Дата: 2026-10-21

---

<a id="related-repositories"></a>
## Связанные репозитории

- [Gemini 3.6 Flash — Руководство и примеры использования](https://github.com/Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases)
- [Gemini Omni — Руководство и запросы](https://github.com/Evolink-AI/awesome-gemini-omni-guide-api-and-prompt)

<a id="acknowledge"></a>
## 🙏 Благодарности

Спасибо авторам, опубликовавшим эти демонстрации:

[@thtbee_](https://x.com/thtbee_), [@hakmgpt](https://x.com/hakmgpt), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@dummerspast39](https://x.com/dummerspast39), [@Mr_Salio](https://x.com/Mr_Salio), [@doe_naps](https://x.com/doe_naps), [@abhinavflac](https://x.com/abhinavflac), [@LuminaBench](https://x.com/LuminaBench), [@HarshithLucky3](https://x.com/HarshithLucky3), [@SPAC89](https://x.com/SPAC89), [@marcthecreatorr](https://x.com/marcthecreatorr), [@auricxofficial](https://x.com/auricxofficial), [@hamoudi_yo](https://x.com/hamoudi_yo), [@Haleeeemahh](https://x.com/Haleeeemahh), [@AI_Screening](https://x.com/AI_Screening)

Атрибуция следует связанным источникам и может нуждаться в исправлении. Сообщайте через issue о пропущенных авторах, дубликатах, неверных утверждениях или просьбах об удалении. Права на сторонние материалы остаются у их владельцев.
