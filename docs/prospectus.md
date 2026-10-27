# Sun'iy intellekt lingvistikasi — o'quv qo'llanma prospekti

Oct 27, 2026 · @Dilrabo Khidirova

## Konsepsiya

Bu kitob o'zbek tilida katta til modellari (LLM) davri lingvistikasini o'rgatadigan birinchi to'liq o'quv qo'llanma bo'ladi: har bir nazariy tushuncha o'zbek tilidagi misol va ishlaydigan Colab daftarchasi bilan beriladi.

**Bo'shliq.** O'zbek tilida kompyuter lingvistikasi va korpus lingvistikasi bo'yicha qo'llanmalar bor, lekin ular asosan LLM davridan oldingi usullarni yoritadi. Tokenizatsiya adolatsizligi, embeddinglar, LLM pragmatikasi, gallyutsinatsiya va kalibrlash kabi mavzular o'zbek tilida tizimli o'quv adabiyotida hali yoritilmagan (nashriyotga topshirishdan oldin milliy kutubxona katalogida qayta tekshiring).

**Noyoblik — 5 ta farqlovchi jihat:**

1. **Ikki yoqlama yondashuv:** tilshunos uchun texnikani, muhandis uchun tilshunoslikni tushuntiradi. Har bir § da "Tilshunos ko'zi bilan" va "Muhandis ko'zi bilan" bloklari bo'ladi.
2. **O'zbek tili markazda:** barcha misollar o'zbekcha (agglyutinatsiya, ikki yozuv, apostrof, shevalar), inglizcha misollar faqat taqqoslash uchun.
3. **Ishlaydigan kod:** 14 ta Colab daftarchasi, bepul GPU yoki CPU'da 10–20 daqiqada ishlaydi, ochiq modellar bilan.
4. **Terminologiya standarti:** 400+ terminli inglizcha–o'zbekcha izohli lug'at, alohida ochiq fayl sifatida.
5. **Muallif tadqiqotlari bilan bog'liqlik:** turkiy tillarda LLM ishonchliligi bo'yicha o'z natijalaringiz (T1, "Ask Twice") darslik misollariga aylanadi.

**Auditoriya:**

| Guruh | Nima oladi |
| --- | --- |
| Filologiya, lingvistika talabalari va magistrantlari | LLM qanday ishlashini kodsiz tushunadi, keyin oddiy kod bilan sinab ko'radi |
| IT, AI, data science talabalari (ITPU va boshqalar) | O'zbek tilining texnik muammolarini lingvistik asosda tushunadi |
| Tadqiqotchilar, PhD izlanuvchilar | Har § da tayyor tadqiqot mavzulari va ochiq ma'lumotlar |
| O'qituvchilar, jurnalistlar, davlat xizmatchilari | Sun'iy intellektning til bilan bog'liq imkoniyat va xavflarini tushunadi |

**Kutilayotgan natijalar:** o'quv qo'llanma (ISBN, UO'K, KBK bilan), ochiq GitHub repozitoriysi, 14 ta Colab daftarchasi, terminlar lug'ati, o'qituvchi uchun slaydlar to'plami, ITPU'da sinov kursi.

**Nom variantlari:**

- "Sun'iy intellekt lingvistikasi" (asosiy, qisqa va aniq)
- "Sun'iy intellekt lingvistikasi: katta til modellari va o'zbek tili" (ilmiy bazalarda yaxshiroq topiladi)
- Inglizcha hamroh nom (GitHub va xalqaro taqdimot uchun): *"Linguistics of AI: Large Language Models through the Lens of Uzbek"*

## Format va har bir § qolipi

Kitob 14 ta § dan iborat bo'ladi, hajmi 240–270 bet (taxminan 15–17 bosma taboq), qog'oz bichimi 60×84 1/16, "Times New Roman" 11 pt. Bu Xolmanova darsligi (256 bet, 16 bosma taboq) bilan bir xil format.

**Kitob tarkibi:**

| Qism | Bet (taxm.) |
| --- | --- |
| Annotatsiya, taqrizchilar, so'zboshi, kirish | 8 |
| "Kitobdan qanday foydalanish kerak" (3 ta o'qish yo'li: tilshunos, muhandis, o'qituvchi) | 3 |
| 14 ta § (har biri 14–18 bet) | 210–230 |
| Ilova A: inglizcha–o'zbekcha terminlar lug'ati | 20 |
| Ilova B: Python va Colab bo'yicha 5 betlik qisqa yo'riqnoma | 5 |
| Test kalitlari, foydalanilgan adabiyotlar, mundarija | 12 |

**Har bir § ning qat'iy qolipi** (barcha bo'limlarda bir xil tartib):

1. **Reja** — 4–6 band.
2. **O'quv maqsadlari** — "Ushbu § ni o'rgangach, siz … qila olasiz" (3–4 ta, Blum taksonomiyasi fe'llari bilan).
3. **Asosiy tushunchalar** — 8–12 termin, birinchi uchrashganda **qalin** va qavs ichida inglizchasi.
4. **Nazariy matn** — 10–12 bet, har 2–3 betda o'zbekcha misol ramkasi.
5. **"Tilshunos ko'zi bilan" / "Muhandis ko'zi bilan"** — yarim betdan ikki blok.
6. **Amaliy mashg'ulot** — Colab daftarchasi tavsifi, QR-kod va GitHub havolasi; qog'ozda faqat 15–25 qatorli asosiy kod parchasi.
7. **Savol va topshiriqlar** — 8–10 ta (3 ta eslash, 4 ta tahlil, 2–3 ta ijodiy yoki loyiha).
8. **Asosiy tushunchalar glossariysi** — qisqa ta'riflar.
9. **Test** — 10 ta savol, 4 variantli; kalitlar kitob oxirida.
10. **Tadqiqot uchun mavzular** — magistrant va PhD izlanuvchilar uchun 2–3 ta ochiq savol.
11. **Qo'shimcha o'qish** — 3–5 ta asosiy manba.

**Uslub qoidalari:** faqat lotin yozuvi; o' va g' uchun bitta belgi (tavsiya: ʻ U+02BB) butun kitob bo'ylab; termin birinchi marta kelganda inglizchasi qavsda; formulalar minimal, har biri so'z bilan ham tushuntiriladi; har § da kamida bitta rasm yoki sxema.

## GitHub repozitoriysi va README

Repozitoriy kitobning xalqaro "vitrinasi" bo'ladi: README ingliz tilida, daftarchalar ichidagi izohlar ikki tilda (o'zbekcha matn, inglizcha qisqa izoh). Tavsiya etilgan nom: `github.com/dilrabonu/ai-linguistics-uz`.

**Papkalar tuzilishi:**

```
ai-linguistics-uz/
├── README.md                 # inglizcha, asosiy vitrina
├── README.uz.md              # o'zbekcha versiya
├── LICENSE                   # kod: MIT
├── LICENSE-CONTENT           # matn va lug'at: CC BY 4.0
├── CITATION.cff              # "Cite this repository" tugmasi uchun
├── requirements.txt          # versiyalari qat'iy belgilangan
├── notebooks/
│   ├── 01_what_is_ai_linguistics.ipynb
│   ├── 02_text_as_numbers.ipynb
│   ├── 03_uzbek_for_machines.ipynb
│   ├── …
│   └── 14_capstone_project.ipynb
├── data/
│   ├── samples/              # kichik namunalar (litsenziyasi aniq)
│   └── DATA_SOURCES.md       # har bir ma'lumot manbai, litsenziya, havola
├── glossary/
│   ├── glossary_en_uz.csv    # term_en, term_uz, definition_uz, chapter
│   └── glossary_en_uz.md
├── src/uzling/               # kichik yordamchi kutubxona
│   ├── normalize.py          # apostrof, kirill↔lotin
│   ├── tokenizer_stats.py    # fertility, parity
│   └── calibration.py        # ECE, Brier, reliability diagram
├── slides/                   # o'qituvchi uchun, har § ga bittadan
├── exercises/solutions/      # faqat o'qituvchilar uchun alohida filialda
└── tests/                    # src/ uchun oddiy testlar (CI bilan)
```

**README.md to'liq matni** (nusxa olib, havolalarni to'ldiring):

```markdown
# AI Linguistics for Uzbek · Sun'iy intellekt lingvistikasi

> The first open, hands-on course on how large language models handle
> language — taught through Uzbek, a low-resource agglutinative Turkic language.

[Open in Colab badge] [License: MIT / CC BY 4.0] [DOI: Zenodo badge]

## Why this exists
Most NLP textbooks teach language technology through English. Uzbek —
spoken by 35+ million people, written in two scripts, with rich agglutinative
morphology — behaves very differently inside today's language models:
it is split into more tokens, it is under-represented in training data, and
models are often confidently wrong in it. This repository accompanies the
Uzbek-language textbook *Sun'iy intellekt lingvistikasi* and turns every
chapter into a runnable notebook.

## What you will learn
| # | Chapter | Notebook | You will build |
|---|---------|----------|----------------|
| 1 | What is AI linguistics? | [01](notebooks/01_...) | A timeline of NLP from ELIZA to LLMs |
| 4 | Tokenization & morphology | [04](notebooks/04_...) | A tokenizer fairness audit for Uzbek |
| 11 | Reliability & calibration | [11](notebooks/11_...) | Reliability diagrams for an LLM in Uzbek vs English |
| … | … | … | … |

## Quick start
Every notebook runs on free Google Colab (CPU or T4 GPU) in under 20 minutes.
Click the Colab badge at the top of any notebook. Local run:
    pip install -r requirements.txt
    jupyter lab notebooks/

## Key resources
- `glossary/` — 400+ English–Uzbek AI terms with definitions (CC BY 4.0)
- `src/uzling/` — small utilities: apostrophe normalization, Cyrillic↔Latin
  transliteration, tokenizer fertility, calibration metrics
- `slides/` — lecture slides for instructors

## Who is this for
Linguistics students who want to understand LLMs, CS students who want to
understand language, and researchers working on low-resource languages.

## Used in teaching
Piloted at IT Park University (Tashkent), [semester, year].

## Related research
- [Your T1 paper / repo link]
- [Your ICTACS 2026 paper link]

## Citation
If you use these materials, please cite (see CITATION.cff).

## Author
Dilrabo Khidirova — Senior Lecturer in Machine Learning, IT Park University.
ORCID: 0009-0009-4983-1503

## Contributing
Issues and pull requests are welcome, especially new Uzbek examples,
glossary corrections, and translations to other Turkic languages.
```

**Xalqaro ko'rinish uchun qo'shimchalar:**

- Zenodo bilan bog'lab, har bir reliz uchun DOI oling (bepul, iqtibos keltirish mumkin bo'ladi).
- Har bir daftarcha boshida "Open in Colab" tugmasi va 3 qatorli inglizcha mazmun.
- `data/DATA_SOURCES.md` faylida har bir ma'lumot manbai litsenziyasi bilan — xalqaro laboratoriyalar aynan shunga e'tibor beradi.
- Kitobning o'zi (PDF) nashriyot ruxsat bergan taqdirdagina repozitoriyga qo'yiladi; ruxsat bo'lmasa, faqat mundarija va bitta namuna §.
- Topics teglar: `uzbek`, `low-resource-nlp`, `turkic-languages`, `llm`, `computational-linguistics`, `education`.

## 1-§. Sun'iy intellekt lingvistikasi fan sifatida

Bu § fanning predmetini belgilaydi va o'quvchiga butun kitobning "xaritasi"ni beradi; hajmi 14–16 bet.

### Reja

1. Sun'iy intellekt lingvistikasining predmeti, maqsadi va vazifalari.
2. Kompyuter lingvistikasi, tabiiy tilni qayta ishlash (NLP) va sun'iy intellekt lingvistikasi: farq va o'xshashliklar.
3. Rivojlanish bosqichlari: qoidaga asoslangan, statistik, neyron va LLM davrlari.
4. Asosiy bahs: model tilni "tushunadimi"?
5. Fanning boshqa fanlar bilan aloqasi va O'zbekistondagi holati.

### O'quv maqsadlari

- Uch fan (kompyuter lingvistikasi, NLP, AI lingvistikasi) farqini misol bilan izohlay oladi.
- NLP tarixidagi 6 ta burilish nuqtasini xronologik tartibda tushuntira oladi.
- "Shakl va ma'no" bahsida ikki tomon dalillarini keltira oladi.

### Asosiy tushunchalar

sun'iy intellekt (artificial intelligence), tabiiy tilni qayta ishlash (NLP), kompyuter lingvistikasi (computational linguistics), til modeli (language model), qoidaga asoslangan tizim (rule-based system), statistik yondashuv, neyron tarmoq (neural network), katta til modeli (LLM), Tyuring testi, til tushunish (natural language understanding), til hosil qilish (natural language generation).

### Nazariy matn mazmuni va misollar

- **Xronologiya ramkasi:** Tyuring maqolasi (1950), Jorjtaun–IBM mashina tarjimasi tajribasi (1954), Xomskiy "Syntactic Structures" (1957), ELIZA (1966), statistik mashina tarjimasi (1990-yillar), word2vec (2013), Transformer (2017), BERT (2018), GPT-3 (2020), ChatGPT (2022).
- **O'zbekcha misol:** "Men kitob o'qiyapman" jumlasi uch davrda qanday qayta ishlanadi: qoida (lug'at + grammatika), statistika (so'z juftlari ehtimoli), neyron model (vektorlar).
- **Bahs bloki:** Bender va Koller (2020) "faqat shakldan ma'no o'rganib bo'lmaydi" dalili va unga qarshi fikrlar; o'quvchi o'z pozitsiyasini yozadi.
- **O'zbekiston bloki:** davlat tilining raqamli rivoji, O'zbek tili milliy korpusi, mahalliy NLP tadqiqotlari (manbalarni yozish vaqtida yangilang).
- **Tilshunos ko'zi bilan:** til modeli — bu tilshunoslikdagi "lisoniy kompetensiya"ning statistik modelimi?
- **Muhandis ko'zi bilan:** til modeli — keyingi tokenni bashorat qiluvchi funksiya.

### Amaliy mashg'ulot (Colab: `01_what_is_ai_linguistics.ipynb`)

1. 30 qatorli o'zbekcha ELIZA yozish: "Men … his qilyapman" shabloni → "Nega … his qilyapsiz?" javobi (regex bilan).
2. Xuddi shu 5 ta savolni kichik ochiq LLM'ga berish (masalan, Qwen2.5-0.5B-Instruct, CPU'da ishlaydi).
3. Natijalarni jadvalda taqqoslash: grammatik to'g'rilik, mazmun, o'zbekcha morfologiya xatolari.
4. Xulosa: qoidaga asoslangan tizim qayerda yutadi (bashorat qilinadigan), LLM qayerda yutadi (moslashuvchanlik).

**Kutiladigan natija:** o'quvchi 1966 va 2024 yondashuvlarini o'z ko'zi bilan ko'radi; jadval topshiriq sifatida topshiriladi.

### Savol va topshiriqlar

1. Kompyuter lingvistikasi va NLP farqini bitta misol bilan tushuntiring.
2. Tyuring testi bugungi LLM'lar uchun yetarli mezonmi? Fikringizni asoslang.
3. NLP tarixidagi 4 ta davrni jadvalda solishtiring (asosiy g'oya, ma'lumot talabi, kamchiligi).
4. ELIZA'ga 3 ta yangi o'zbekcha qoida qo'shing va natijani izohlang.
5. LLM'ning o'zbekcha javobidagi 3 ta morfologik xatoni toping va tasniflang.
6. "Model tilni tushunadi" degan fikrga qarshi va tarafdor bittadan dalil keltiring.
7. O'zbek tili uchun eng muhim 3 ta NLP vazifasini tanlang va sababini yozing.
8. **Loyiha:** oilangizdagi 3 kishidan sun'iy intellekt haqida nima bilishini so'rab, javoblarni lingvistik jihatdan tahlil qiling.

### Test namunasi

1. ELIZA dasturi qaysi yondashuvga asoslangan? A) neyron tarmoq B) **qoidalar va shablonlar** C) statistik tarjima D) Transformer
2. Transformer arxitekturasi qachon taqdim etilgan? A) 2013 B) 2015 C) **2017** D) 2020

### Tadqiqot uchun mavzular

- O'zbekistonda kompyuter lingvistikasi tadqiqotlarining 1990–2025 yillardagi bibliometrik tahlili.
- O'zbek tilidagi sun'iy intellekt terminlarining shakllanishi: kalka, o'zlashma va yangi yasalma so'zlar.

### Qo'shimcha o'qish

Jurafsky, Martin "Speech and Language Processing" (3-nashr qoralamasi, 1-bob); Turing (1950); Bender, Koller (2020).

## 2-§. Til belgilar tizimi sifatida va mashina uchun til

Bu § klassik semiotikani (Sossyur, Pirs) matnni raqamga aylantirish bilan bog'laydi: mashina uchun har qanday belgi — avval bayt, keyin raqam, keyin vektor; hajmi 14–16 bet.

### Reja

1. Sossyur belgisi: ifodalovchi va ifodalanuvchi; belgining ixtiyoriyligi.
2. Pirs tasnifi: ikona, indeks, simvol — mashina qaysi birini "ko'radi"?
3. Yozuvdan baytgacha: Unicode, UTF-8 va kodlash muammolari.
4. Matnni raqamga aylantirish: one-hot, so'zlar xaltasi (bag-of-words), TF-IDF.
5. Tilning statistik qonuniyatlari: Sipf qonuni, Xips qonuni.

### O'quv maqsadlari

- Sossyur belgisi bilan kompyuterdagi belgi (bayt, token) farqini izohlay oladi.
- Bitta o'zbekcha so'zning turli Unicode yozilishlarini aniqlay va normallashtira oladi.
- O'zbekcha matnda Sipf qonunini tekshira oladi.

### Asosiy tushunchalar

belgi (sign), ifodalovchi (signifier), ifodalanuvchi (signified), ixtiyoriylik (arbitrariness), Unicode, kod nuqtasi (code point), UTF-8, normallashtirish (normalization), one-hot vektor, so'zlar xaltasi (bag-of-words), TF-IDF, Sipf qonuni (Zipf's law), lug'at hajmi (vocabulary size).

### Nazariy matn mazmuni va misollar

- **Markaziy misol — "o'zbek" so'zining 4 xil yozilishi:** o'zbek (ASCII apostrof U+0027), oʻzbek (U+02BB), o‘zbek (U+2018), o\`zbek (gravis U+0060). Inson uchun bir so'z, mashina uchun 4 xil bayt ketma-ketligi va 4 xil token.
- **Ikki yozuv:** kirill va lotin yozuvidagi "til" so'zi — bir ifodalanuvchi, ikki ifodalovchi; mashina ularni bog'lamaydi, agar o'rgatilmasa.
- **TF-IDF misoli:** 3 ta qisqa o'zbekcha matn (sport, iqtisod, ta'lim yangiligi) bo'yicha qo'lda hisoblangan jadval.
- **Sipf qonuni:** o'zbek tilida eng ko'p uchraydigan so'zlar ("va", "bu", "bilan", "uchun") va agglyutinatsiya tufayli "uzun dum" inglizchadan qanchalik uzunroq ekani.
- **Tilshunos ko'zi bilan:** belgining ixtiyoriyligi — nima uchun model ma'noni faqat kontekstdan o'rganishi kerak.
- **Muhandis ko'zi bilan:** normallashtirish qilinmasa, lug'at keraksiz kattalashadi va model sifati tushadi.

### Amaliy mashg'ulot (Colab: `02_text_as_numbers.ipynb`)

1. `ord()` va `.encode('utf-8')` bilan "o'zbek" so'zining 4 varianti baytlarini chiqarish.
2. `uzling.normalize` funksiyasini yozish: barcha apostrof variantlarini bitta belgiga keltirish.
3. O'zbek Vikipediyasidan (Hugging Face `wikimedia/wikipedia`, `uz` qismi) 10 000 ta maqola yuklash.
4. Normallashtirishdan oldin va keyin lug'at hajmini solishtirish.
5. Sipf grafigini log-log masshtabda chizish, inglizcha Vikipediya namunasi bilan bitta grafikda.
6. scikit-learn bilan TF-IDF va eng muhim 10 so'zni chiqarish.

**Asosiy kod parchasi (kitobda bosiladi):**

```python
APOSTROPHES = ["'", "ʻ", "‘", "’", "`"]
def normalize_uz(text, target="ʻ"):
    for a in APOSTROPHES:
        text = text.replace("o" + a, "o" + target).replace("g" + a, "g" + target)
        text = text.replace("O" + a, "O" + target).replace("G" + a, "G" + target)
    return text
```

**Kutiladigan natija:** normallashtirishdan keyin lug'at sezilarli kamayadi; o'quvchi o'z raqamini jadvalga yozadi.

### Savol va topshiriqlar

1. Sossyur belgisi va Unicode kod nuqtasini taqqoslang.
2. Nima uchun "tutuq belgisi" (ayirish belgisi, masalan "ma'no") va o'/g' apostrofini bir xil normallashtirish xavfli? Misol keltiring.
3. One-hot vektorlarda "kitob" va "kitoblar" qanchalik o'xshash? Nima uchun?
4. 5 ta jumladan iborat matn uchun TF-IDF ni qo'lda hisoblang.
5. O'zbek va ingliz tillarida Sipf egri chiziqlari nima uchun farq qiladi?
6. Kirill va lotin yozuvidagi bir xil matnni mashina uchun birlashtirish yo'llarini taklif qiling.
7. Ijtimoiy tarmoqlardan 50 ta o'zbekcha izoh yig'ing va apostrof variantlari ulushini hisoblang.
8. **Loyiha:** o'zbekcha matn uchun to'liq normallashtirish qoidalari ro'yxatini tuzing.

### Test namunasi

1. UTF-8 kodlashda "ʻ" (U+02BB) belgisi necha baytni egallaydi? A) 1 B) **2** C) 3 D) 4
2. TF-IDF'dagi IDF nimani pasaytiradi? A) noyob so'zlar vaznini B) **ko'p hujjatlarda uchraydigan so'zlar vaznini** C) jumla uzunligini D) harflar sonini

### Tadqiqot uchun mavzular

- O'zbek tilidagi onlayn matnlarda apostrof va yozuv variantlari tarqalishi: korpus asosida tadqiqot.
- O'zbek tili uchun Sipf va Xips qonunlarining agglyutinativ tillar bilan qiyosiy tahlili.

### Qo'shimcha o'qish

Sossyur "Umumiy tilshunoslik kursi"; Xolmanova (2020), 5-§; Jurafsky, Martin (2-bob: regular expressions, normalization); Unicode standarti (UAX #15).

## 3-§. O'zbek tilining mashina uchun xususiyatlari

Bu § kitobning "yuragi": o'zbek tilining qaysi xususiyatlari sun'iy intellekt uchun qiyinchilik tug'dirishini tizimli tasniflaydi; boshqa kitoblarda yo'q eng noyob bo'lim, hajmi 16–18 bet.

### Reja

1. Agglyutinatsiya: bitta so'zda butun jumla ma'nosi.
2. Ikki yozuv va transliteratsiya muammolari.
3. Erkin so'z tartibi, SOV tuzilishi va olmoshning tushib qolishi (pro-drop).
4. Grammatik jins yo'qligi va tarjimadagi gender og'ishi.
5. Shevalar, kod almashinuvi va ijtimoiy tarmoq tili.
6. Kam resursli til: raqamli ma'lumotlar tanqisligi.

### O'quv maqsadlari

- O'zbek tilining 6 ta "mashina uchun qiyin" xususiyatini misol bilan tasniflay oladi.
- Oddiy qoidaga asoslangan morfologik segmentator yoza oladi.
- Tarjima modelidagi gender og'ishini o'lchay oladi.

### Asosiy tushunchalar

agglyutinatsiya (agglutination), morfema, affiks, morfologik segmentatsiya, transliteratsiya, SOV so'z tartibi, pro-drop, grammatik jins (grammatical gender), gender og'ishi (gender bias), kod almashinuvi (code-switching), sheva (dialect), kam resursli til (low-resource language).

### Nazariy matn mazmuni va misollar

- **Agglyutinatsiya:** kitob + lar + imiz + da + gi + lar + dan = "kitoblarimizdagilardan"; bitta o'zak "kitob"dan yuzlab so'z shakllari. Ingliz tilida "from those that are in our books" — 6 so'z.
- **Transliteratsiya:** kirilldan lotinga o'tishda bir harf ikki harfga aylanadigan holatlar (yo, yu, ya, ts) va "ye" muammosi (so'z boshida: yer, yetti); "sh" va "s+h" farqi ("Ishoq" va "Is'hoq" turidagi holatlar).
- **Pro-drop:** "Kecha keldim" — ega yo'q, lekin shaxs qo'shimchadan aniq; model buni tarjimada qayta tiklashi kerak.
- **Gender:** "U shifokor. U hamshira." — o'zbekchada "u" jinssiz, tarjima modeli inglizchada "he/she" ni tanlashga majbur; bu stereotiplarni ko'rsatadi.
- **Kod almashinuvi:** "Bugun vstrecha bor, keyin skinut qilaman" (rus so'zlari lotin yozuvida); ijtimoiy tarmoqdagi "translit".
- **Shevalar:** Namangan, Xorazm (o'g'uz), qipchoq shevalaridan bittadan misol; adabiy til bilan farq.
- **Turkiy qiyos:** turk, qozoq tillarida singarmonizm saqlangan, o'zbek tilida esa asosan yo'qolgan — bu tokenizatsiyaga qanday ta'sir qiladi.
- **Tilshunos ko'zi bilan:** morfema — ma'no birligi; token — statistik birlik. Ular qachon mos keladi?
- **Muhandis ko'zi bilan:** har bir xususiyat uchun "nima buziladi" jadvali (qidiruv, tarjima, OCR, ovoz).

### Amaliy mashg'ulot (Colab: `03_uzbek_for_machines.ipynb`)

1. 40 ta asosiy qo'shimcha ro'yxati asosida oddiy o'zbekcha segmentator yozish (o'ngdan chapga qo'shimcha ajratish).
2. 100 ta so'zda sinash va xatolarni tasniflash (masalan, "dollar" so'zidagi "lar" qo'shimcha emas, o'zak qismi; "bolalar"da esa qo'shimcha).
3. Kirill↔lotin transliteratorini yozish va 3 ta qiyin holatni ko'rsatish.
4. **Gender tajribasi:** 30 ta kasb nomi bilan "U \[kasb\]." jumlalarini NLLB-200 (distilled-600M) modeli bilan inglizchaga tarjima qilish; "he" va "she" ulushini kasb bo'yicha grafikda ko'rsatish.
5. Natijani xulosa jadvalida yozish.

**Kutiladigan natija:** o'quvchi o'z qo'li bilan gender og'ishi grafigini oladi — bu ijtimoiy tarmoqda va konferensiyada ko'rsatish mumkin bo'lgan kuchli vizual misol.

### Savol va topshiriqlar

1. "Uyimizdagilarga" so'zini morfemalarga ajrating va har birining vazifasini yozing.
2. Agglyutinatsiya qidiruv tizimi ishiga qanday ta'sir qiladi? 2 ta misol.
3. Kirilldan lotinga avtomatik o'tishda xato beradigan 5 ta so'z toping.
4. Pro-drop hodisasi mashina tarjimasini qanday qiyinlashtiradi?
5. Gender tajribasida eng "stereotipik" 5 ta kasbni sharhlang.
6. O'zingiz yashaydigan hudud shevasidan 10 ta so'z to'plang va adabiy muqobilini yozing.
7. Ijtimoiy tarmoqdan 20 ta kod almashinuvi misolini to'plab, tasniflang.
8. **Loyiha:** segmentatorni 200 so'zda baholang va aniqlik (accuracy) foizini hisoblang.

### Test namunasi

1. "Kecha keldim" jumlasida qaysi hodisa kuzatiladi? A) kod almashinuvi B) **pro-drop** C) singarmonizm D) transliteratsiya
2. Agglyutinativ tilda so'z shakllari qanday hosil bo'ladi? A) ichki fleksiya bilan B) **qo'shimchalarni ketma-ket qo'shish bilan** C) so'z tartibi bilan D) urg'u bilan

### Tadqiqot uchun mavzular

- O'zbek-ingliz mashina tarjimasidagi gender og'ishi: kasb nomlari bo'yicha tizimli o'lchov (konferensiya tezisi uchun tayyor mavzu).
- O'zbekcha ijtimoiy tarmoq matnlarida kod almashinuvi turlari va ularning NLP modellariga ta'siri.

### Qo'shimcha o'qish

O'zbek tili grammatikasi bo'yicha akademik manbalar (morfologiya bo'limi); Joshi va boshq. (2020) "The State and Fate of Linguistic Diversity"; Stanovsky va boshq. (2019) mashina tarjimasidagi gender og'ishi.

## 4-§. Tokenizatsiya va morfologiya

Bu § "o'zbek tili soligi"ni (tokenizer tax) o'lchaydi: bir xil mazmun o'zbekchada inglizchaga qaraganda ko'proq tokenga bo'linadi, demak qimmatroq, sekinroq va kontekstga kamroq sig'adi; hajmi 16–18 bet.

### Reja

1. Token nima: so'z, morfema, bo'g'in va token farqi.
2. Tokenizatsiya algoritmlari: BPE, WordPiece, Unigram (SentencePiece), bayt darajasidagi tokenizatsiya.
3. Tokenizatsiya adolati: fertility va parity ko'rsatkichlari.
4. Token chegaralari va morfema chegaralari: qachon mos keladi?
5. O'zbek tili uchun maxsus tokenizator o'qitish.

### O'quv maqsadlari

- BPE algoritmini qog'ozda 5 qadam bajarib ko'rsata oladi.
- 6 ta mashhur model tokenizatorini o'zbek tili bo'yicha solishtira oladi.
- Tokenizatsiyaning narx, tezlik va sifatga ta'sirini hisoblay oladi.

### Asosiy tushunchalar

token, tokenizatsiya (tokenization), lug'at (vocabulary), BPE (byte-pair encoding), WordPiece, Unigram model, SentencePiece, bayt darajasidagi tokenizator (byte-level), fertility (so'z boshiga token soni), parity (tillararo tenglik), kontekst oynasi (context window), morfologik moslik (morphological alignment).

### Nazariy matn mazmuni va misollar

- **BPE qo'lda:** "kitob, kitoblar, kitobim, kitobda" so'zlaridan iborat mini-korpusda 5 ta birlashtirish qadami jadval ko'rinishida.
- **Model taqqoslash ramkasi:** "O'zbekistonning poytaxti Toshkent shahri" jumlasi turli tokenizatorlarda qanday bo'linadi (rangli bo'laklar rasmi).
- **Fertility formulasi:** fertility = tokenlar soni / so'zlar soni; parity = o'zbekcha tokenlar soni / inglizcha parallel matn tokenlari soni.
- **Iqtisodiy oqibat:** API narxi token bo'yicha hisoblanadi — parity 2,5 bo'lsa, o'zbekcha foydalanuvchi bir xil xizmat uchun 2,5 baravar ko'p to'laydi. Bu adolat masalasi (Petrov va boshq., 2023).
- **Morfologiya:** "kitoblarimizdan" so'zi tokenizatorda "kit|obl|arim|izdan" kabi morfemaga mos kelmaydigan bo'laklarga bo'linishi mumkin; bu modelning grammatikani o'rganishiga ta'sir qiladi.
- **Tilshunos ko'zi bilan:** token — bu yangi "til birligi"mi yoki faqat texnik qulaylik?
- **Muhandis ko'zi bilan:** lug'at hajmini oshirish fertility'ni kamaytiradi, lekin model parametrlarini oshiradi.

### Amaliy mashg'ulot (Colab: `04_tokenization_audit.ipynb`)

1. FLORES-200 parallel to'plamidan o'zbekcha (`uzn_Latn`) va inglizcha (`eng_Latn`) 1 000 ta jumla yuklash.
2. 6 ta tokenizatorni yuklash: GPT-2, Llama-3, Qwen2.5, Gemma, XLM-R, mT5 (Hugging Face `AutoTokenizer`; yopiq modellar uchun litsenziyani qabul qilish kerak bo'lishi mumkin).
3. Har biri uchun fertility va parity hisoblab, ustunli grafik chizish.
4. HF `tokenizers` kutubxonasi bilan o'zbek Vikipediyasida 32 000 lug'atli BPE o'qitish va parity'ni solishtirish.
5. 100 ta qo'lda segmentlangan so'zda morfologik moslik foizini hisoblash.

**Asosiy kod parchasi:**

```python
from transformers import AutoTokenizer
def fertility(tok, sentences):
    n_tok = sum(len(tok.tokenize(s)) for s in sentences)
    n_words = sum(len(s.split()) for s in sentences)
    return n_tok / n_words
for name in ["gpt2", "xlm-roberta-base", "Qwen/Qwen2.5-0.5B"]:
    tok = AutoTokenizer.from_pretrained(name)
    print(name, round(fertility(tok, uz_sents), 2), round(fertility(tok, en_sents), 2))
```

**Kutiladigan natija:** "o'zbek tili soligi" grafigi — kitobning eng ko'p ulashiladigan rasmi bo'lishi mumkin; README'ga ham qo'ying.

### Savol va topshiriqlar

1. Token, morfema va bo'g'in farqini "maktablarimizda" misolida tushuntiring.
2. BPE'ni berilgan 6 so'zli korpusda 4 qadam bajaring.
3. Fertility va parity farqi nima? Har biri nimani ko'rsatadi?
4. Qaysi tokenizator o'zbek tili uchun eng "adolatli" chiqdi va nima uchun?
5. Parity 2,5 bo'lsa, 4 000 tokenli kontekstga necha so'zli o'zbekcha matn sig'adi?
6. Morfemaga mos tokenizatsiya model sifatini oshiradimi? Ikki tomon dalili.
7. O'zbek tili uchun maxsus tokenizator yaratishning foyda va zararlarini yozing.
8. **Loyiha:** 5 ta turkiy til (o'zbek, qozoq, qirg'iz, turk, ozarbayjon) uchun parity jadvalini tuzing.

### Test namunasi

1. Fertility qanday hisoblanadi? A) so'zlar/harflar B) **tokenlar/so'zlar** C) jumlalar/tokenlar D) lug'at/korpus
2. BPE har qadamda nimani birlashtiradi? A) eng uzun so'zlarni B) **eng ko'p uchraydigan qo'shni belgilar juftini** C) morfemalarni D) jumlalarni

### Tadqiqot uchun mavzular

- Turkiy tillar uchun tokenizatsiya adolati: 15 ta zamonaviy LLM bo'yicha qiyosiy audit (xalqaro seminar maqolasi uchun mos).
- Morfologiyaga asoslangan tokenizatsiya o'zbekcha matn tasnifi sifatini oshiradimi?

### Qo'shimcha o'qish

Sennrich va boshq. (2016) BPE; Kudo, Richardson (2018) SentencePiece; Rust va boshq. (2021) "How Good is Your Tokenizer?"; Petrov va boshq. (2023) "Language Model Tokenizers Introduce Unfairness Between Languages".

## 5-§. Leksika, semantika va embeddinglar

Bu § distributiv semantikani ("so'zni uning hamrohlari orqali bilasan") zamonaviy so'z vektorlari bilan bog'laydi va o'zbek tilidagi omonimlar orqali kontekstli ma'noni ko'rsatadi; hajmi 16 bet.

### Reja

1. Distributiv gipoteza: Xarris (1954) va Fers (1957).
2. Statik so'z vektorlari: word2vec, GloVe, fastText.
3. Vektor fazosidagi semantik munosabatlar: sinonimiya, antonimiya, analogiya.
4. Polisemiya va omonimiya: kontekstli embeddinglar (BERT, LaBSE).
5. Embeddinglardagi ijtimoiy og'ishlar.

### O'quv maqsadlari

- Kosinus o'xshashlikni qo'lda hisoblay oladi.
- O'zbekcha so'z vektorlarida analogiya va yaqin qo'shnilarni topa oladi.
- Omonimning turli kontekstdagi vektorlari farqini vizual ko'rsata oladi.

### Asosiy tushunchalar

distributiv gipoteza (distributional hypothesis), embedding, so'z vektori (word vector), kosinus o'xshashlik (cosine similarity), vektor fazosi, analogiya, statik va kontekstli embedding, polisemiya, omonimiya, semantik maydon (semantic field), subso'z (subword), o'lchamni kamaytirish (dimensionality reduction).

### Nazariy matn mazmuni va misollar

- **O'zbek omonimlari — kitobning noyob misollari:** "yuz" (inson yuzi / 100 / suvda suzmoq buyruq shakli), "ot" (hayvon / ism / otmoq), "qo'y" (hayvon / qo'ymoq), "tush" (uyqudagi tush / kun yarmi / tushmoq). Statik vektor ularning barchasini bitta nuqtaga qo'yadi, kontekstli model esa ajratadi.
- **Tajnis bilan bog'liqlik:** mumtoz adabiyotdagi tajnis (so'z o'yini) — omonimiyaning badiiy qo'llanishi; model buni ilg'ay oladimi? (dissertatsiya tadqiqotingizdan 2–3 misol).
- **Analogiya ramkasi:** Toshkent : O'zbekiston = Olmaota : ? ; ota : ona = aka : ?
- **fastText va agglyutinatsiya:** subso'z n-grammalari tufayli "kitoblarimizdan" kabi lug'atda yo'q so'zga ham vektor hosil bo'ladi.
- **Antonimiya muammosi:** "issiq" va "sovuq" vektor fazosida yaqin, chunki bir xil kontekstda keladi.
- **Og'ish:** "erkak – muhandis, ayol – ?" analogiyasi orqali stereotiplarni ko'rsatish.
- **Tilshunos ko'zi bilan:** semantik maydon nazariyasi va vektor klasterlari o'xshashligi.
- **Muhandis ko'zi bilan:** embedding — qidiruv, tavsiya va RAG tizimlarining asosi.

### Amaliy mashg'ulot (Colab: `05_embeddings_uz.ipynb`)

1. fastText'ning o'zbekcha tayyor vektorlarini yuklash (Common Crawl asosidagi `cc.uz.300`; hajmi katta, shuning uchun 100 000 so'zga qisqartirilgan nusxa repozitoriyda).
2. "maktab", "ona", "paxta", "non" so'zlarining 10 ta yaqin qo'shnisini chiqarish.
3. 20 ta o'zbekcha analogiya testini o'tkazish va aniqlikni hisoblash.
4. "yuz" so'zi uchta jumlada: "Uning yuzi qizardi", "Yuz so'm berdi", "Daryoda yuz!" — ko'p tilli kontekstli model (masalan, LaBSE yoki XLM-R) bilan vektor olish va kosinus o'xshashliklarni jadvalda ko'rsatish.
5. 200 ta so'zni UMAP bilan 2D'ga tushirib, semantik maydonlarni rangli grafikda ko'rsatish.

**Kutiladigan natija:** omonim "yuz"ning uchta ma'nosi grafikda alohida nuqtalar sifatida ko'rinadi — lingvistlar uchun juda ta'sirli namoyish.

### Savol va topshiriqlar

1. Fersning mashhur iborasini o'zbekcha misol bilan izohlang.
2. Ikki 3 o'lchamli vektor uchun kosinus o'xshashlikni qo'lda hisoblang.
3. Nima uchun antonimlar vektor fazosida yaqin joylashadi?
4. Statik va kontekstli embedding farqini "ot" so'zi misolida tushuntiring.
5. fastText lug'atda yo'q so'zga qanday vektor beradi?
6. 10 ta o'zbekcha omonim to'plang va modelning ularni ajrata olishini tekshiring.
7. Embeddinglardagi gender og'ishini kamaytirish usullarini qisqacha yozing.
8. **Loyiha:** o'zbekcha analogiya test to'plamini (100 ta) tuzing va GitHub'ga yuklang.

### Test namunasi

1. Distributiv gipotezaga ko'ra so'z ma'nosi nima bilan belgilanadi? A) etimologiya B) **u keladigan kontekstlar** C) harflar soni D) lug'at ta'rifi
2. Qaysi model lug'atda yo'q so'zga ham vektor beradi? A) one-hot B) word2vec C) **fastText** D) TF-IDF

### Tadqiqot uchun mavzular

- O'zbekcha so'z analogiyalari va semantik o'xshashlik test to'plamini yaratish va modellarni baholash.
- Mumtoz o'zbek she'riyatidagi tajnis va omonimlarni kontekstli embeddinglar bilan aniqlash.

### Qo'shimcha o'qish

Harris (1954) "Distributional Structure"; Mikolov va boshq. (2013); Bojanowski va boshq. (2017) fastText; Grave va boshq. (2018) 157 til uchun so'z vektorlari; Bolukbasi va boshq. (2016) embeddinglardagi gender og'ishi.

## 6-§. Sintaksis va til modellari

Bu § til modelini n-grammadan Transformergacha bosqichma-bosqich quradi va savol qo'yadi: model o'zbek grammatikasini (moslashuv, SOV tartib) qanchalik "biladi"; hajmi 16–18 bet.

### Reja

1. Til modeli: keyingi so'zni bashorat qilish va ehtimollar zanjiri.
2. N-gramm modellari va perplexity (chalkashlik) ko'rsatkichi.
3. Neyron til modellari: RNN, LSTM va ularning cheklovlari.
4. Attention va Transformer: lingvistik talqin.
5. Minimal juftliklar va probing: model sintaksisni o'rganadimi?

### O'quv maqsadlari

- Bigramm ehtimolini kichik o'zbekcha korpusda qo'lda hisoblay oladi.
- Attention'ni "so'zlar o'rtasidagi bog'lanish kuchi" sifatida tushuntira oladi.
- O'zbekcha minimal juftliklar to'plami bilan modelning grammatik bilimini baholay oladi.

### Asosiy tushunchalar

til modeli (language model), shartli ehtimol, n-gramm, perplexity, silliqlash (smoothing), rekurrent neyron tarmoq (RNN), attention, o'z-o'ziga attention (self-attention), Transformer, pozitsion kodlash (positional encoding), minimal juftlik (minimal pair), probing, moslashuv (agreement).

### Nazariy matn mazmuni va misollar

- **Bigramm misoli:** "Men maktabga boraman. Men uyga boraman. Sen maktabga borasan." korpusida P(boraman | maktabga) ni hisoblash.
- **Perplexity:** "modelning hayratlanish darajasi" sifatida sodda tushuntirish va bitta formula.
- **Uzoq masofali bog'lanish:** **"Men kecha bozordan katta, qizil va juda shirin olmalarni sotib oldim" kabi SOV jumlalarda ega boshida, fe'l oxirida keladi va shaxs qo'shimchasi ("-m") 9 so'z narida egaga moslashadi**; RNN buni "unutadi", attention esa to'g'ridan-to'g'ri bog'laydi.
- **Attention rasmi:** "Ona bolasini maktabga olib bordi" jumlasida "bordi" so'zining "Ona"ga attention'i (issiqlik xaritasi).
- **Minimal juftliklar:** "Biz keldik" / \*"Biz keldim"; "Ular kitob o'qishdi" / \*"Ular kitob o'qidik". Grammatik jumla ehtimoli yuqori bo'lishi kerak.
- **Tilshunos ko'zi bilan:** Xomskiy grammatikasi va statistik model: "Rangsiz yashil g'oyalar g'azab bilan uxlaydi" misolining o'zbekcha talqini.
- **Muhandis ko'zi bilan:** Transformer qatlamlari, boshlar (heads) va parametrlar sonining amaliy ma'nosi.

### Amaliy mashg'ulot (Colab: `06_language_models.ipynb`)

1. O'zbek Vikipediyasidan 1 mln so'zda bigramm va trigramm model qurish; matn generatsiya qilish.
2. Turli modellarning perplexity'sini test matnda solishtirish.
3. `bertviz` bilan XLM-R'da o'zbekcha jumla attention'ini vizuallashtirish.
4. **O'zbekcha BLiMP-mini:** 6 ta grammatik hodisa (shaxs-son moslashuvi, kelishik, egalik, inkor, zamon, so'z tartibi) bo'yicha 120 ta minimal juftlik yaratish.
5. Kichik ochiq LLM bilan har juftlik uchun log-ehtimolni hisoblab, hodisa bo'yicha aniqlik grafigini chizish.

**Asosiy kod parchasi:**

```python
import torch
def sent_logprob(model, tok, text):
    ids = tok(text, return_tensors="pt").input_ids
    with torch.no_grad():
        out = model(ids, labels=ids)
    return -out.loss.item() * (ids.shape[1] - 1)
correct = sum(sent_logprob(m, t, g) > sent_logprob(m, t, b) for g, b in pairs)
print("Aniqlik:", correct / len(pairs))
```

**Kutiladigan natija:** qaysi grammatik hodisalarni model yaxshi, qaysilarini yomon bilishini ko'rsatuvchi grafik; o'zbekcha minimal juftliklar to'plami alohida ochiq ma'lumot sifatida e'lon qilinadi.

### Savol va topshiriqlar

1. Berilgan 4 jumlali korpusda 3 ta bigramm ehtimolini hisoblang.
2. Perplexity past bo'lishi nimani anglatadi?
3. SOV tartibli tillar uchun uzoq masofali bog'lanish nima uchun muhim?
4. Attention xaritasini lingvistik jihatdan talqin qilishning cheklovlari nimada?
5. 10 ta yangi o'zbekcha minimal juftlik tuzing (kelishik qo'shimchalari bo'yicha).
6. Model qaysi hodisada eng ko'p xato qildi? Lingvistik sababini taxmin qiling.
7. Xomskiyning statistik modellarga tanqidini va bugungi javoblarni qisqacha yozing.
8. **Loyiha:** minimal juftliklar to'plamini 500 taga yetkazing va 3 ta model bilan baholang.

### Test namunasi

1. Perplexity nimani o'lchaydi? A) model hajmini B) **modelning matnni bashorat qilishdagi noaniqligini** C) so'zlar sonini D) tarjima sifatini
2. Transformer'ning asosiy mexanizmi qaysi? A) konvolyutsiya B) rekursiya C) **self-attention** D) qaror daraxti

### Tadqiqot uchun mavzular

- O'zbek tili uchun BLiMP uslubidagi minimal juftliklar benchmarkini yaratish (ACL, LREC seminarlari uchun mos).
- Ko'p tilli modellarda o'zbekcha kelishik qo'shimchalarini probing usuli bilan o'rganish.

### Qo'shimcha o'qish

Jurafsky, Martin (3- va 9-boblar); Vaswani va boshq. (2017) "Attention Is All You Need"; Warstadt va boshq. (2020) BLiMP; Hewitt, Manning (2019); Tenney va boshq. (2019).

## 7-§. Katta til modellari

Bu § LLM qanday yaratilishini (oldindan o'qitish → ko'rsatmaga moslashtirish → inson fikri bilan moslashtirish) tushuntiradi va promptni lingvistik hodisa — nutq akti sifatida tahlil qiladi; hajmi 16–18 bet.

### Reja

1. Oldindan o'qitish: ma'lumot, masshtab qonunlari, o'zbek tilining o'qitish ma'lumotlaridagi ulushi.
2. Ko'rsatmaga moslashtirish (instruction tuning) va inson fikri asosida moslashtirish (RLHF va shu kabi usullar).
3. Kontekstda o'rganish: zero-shot va few-shot.
4. Prompt lingvistikasi: prompt nutq akti sifatida, xushmuomalalik, til tanlovi.
5. Generatsiya parametrlari: harorat (temperature), top-p va ularning matnga ta'siri.

### O'quv maqsadlari

- LLM yaratilishining 3 bosqichini sxema bilan tushuntira oladi.
- Bir xil vazifani zero-shot va few-shot usulda bajarib, natijani solishtira oladi.
- Prompt tili (o'zbekcha yoki inglizcha) natijaga qanday ta'sir qilishini o'lchay oladi.

### Asosiy tushunchalar

katta til modeli (LLM), oldindan o'qitish (pretraining), masshtab qonunlari (scaling laws), ko'rsatmaga moslashtirish (instruction tuning), inson fikri asosida mustahkamlovchi o'qitish (RLHF), moslashtirish (alignment), prompt, kontekstda o'rganish (in-context learning), zero-shot, few-shot, harorat (temperature), chat shabloni (chat template), nutq akti (speech act).

### Nazariy matn mazmuni va misollar

- **Uch bosqich sxemasi:** "kitob o'qigan talaba → o'qituvchi ko'rsatmasi bilan mashq qilgan talaba → baholar asosida yaxshilangan talaba" metaforasi.
- **Ma'lumot ulushi:** ochiq ko'p tilli korpuslarda o'zbek tilining ulushi juda kichik ekanini ko'rsatuvchi diagramma (raqamlarni yozish vaqtida rasmiy manbalardan oling: masalan, CommonCrawl til statistikasi).
- **Ko'p tilli modellar:** o'zbek tilini rasman qo'llab-quvvatlaydigan ochiq modellar (Aya, Qwen, Gemma, Llama oilalari; har birining hujjatidan tekshirib yozing).
- **Prompt va nutq akti:** "Iltimos, … tushuntirib bersangiz" (bilvosita so'rov) va "… tushuntir" (bevosita buyruq): Ostin va Serl nazariyasi bo'yicha tahlil.
- **Sizlash va senlash:** model o'zbekcha javobda "siz" va "sen" shakllarini izchil qo'llaydimi?
- **Tilshunos ko'zi bilan:** LLM — ulkan "nutq korpusi"ning statistik umumlashmasi; u kompetensiyami yoki performansmi?
- **Muhandis ko'zi bilan:** chat shablonlari, tizim prompti va kontekst uzunligi.

### Amaliy mashg'ulot (Colab: `07_llms_in_uzbek.ipynb`)

1. 2–3 ta kichik ochiq instruct model (1–3 mlrd parametr) yuklash.
2. 10 ta o'zbekcha vazifa to'plami: matnni qisqartirish, maqol izohlash, tarjima, grammatik tahlil, rasmiy xat yozish va boshqalar.
3. Har vazifani 4 xil sharoitda bajarish: o'zbekcha prompt, inglizcha prompt, zero-shot, 3-shot.
4. Haroratni 0,2 / 0,7 / 1,2 qilib, bir xil promptdan 5 tadan javob olish va farqni kuzatish.
5. Natijalarni o'qituvchi yaratgan 1–5 ballik rubrika bo'yicha baholash (inson bahosi).

**Kutiladigan natija:** "prompt tili × usul" jadvali; ko'p hollarda inglizcha prompt o'zbekcha vazifada ham farq beradi — bu muhokama uchun yaxshi mavzu.

### Savol va topshiriqlar

1. Oldindan o'qitish va ko'rsatmaga moslashtirish farqini metafora bilan tushuntiring.
2. Nima uchun kam resursli tillarda LLM sifati past bo'ladi? 3 ta sabab.
3. Zero-shot va few-shot natijalari qaysi vazifada eng katta farq qildi?
4. "Iltimos" so'zi model javobini o'zgartirdimi? Nutq akti nazariyasi asosida izohlang.
5. Yuqori harorat qaysi vazifalarda foydali, qaysilarida zararli?
6. Model o'zbekcha javobda "siz"/"sen" shakllarini qanday qo'lladi? 5 ta misol.
7. O'zbekcha vazifalar uchun 1–5 ballik baholash rubrikasini tuzing.
8. **Loyiha:** 30 ta o'zbekcha maqolni 2 ta modelga izohlating va to'g'riligini tilshunos sifatida baholang.

### Test namunasi

1. Few-shot prompting nima? A) modelni qayta o'qitish B) **promptda bir necha namuna berish** C) haroratni pasaytirish D) lug'atni kengaytirish
2. Harorat oshsa nima bo'ladi? A) javob qisqaradi B) **javoblar xilma-xilroq va tasodifiyroq bo'ladi** C) model tezlashadi D) tokenlar kamayadi

### Tadqiqot uchun mavzular

- O'zbekcha promptlarda xushmuomalalik shakllarining LLM javob sifatiga ta'siri.
- O'zbek maqol va iboralarini LLM'lar tushunishini baholovchi test to'plami.

### Qo'shimcha o'qish

Brown va boshq. (2020) "Language Models are Few-Shot Learners"; Ouyang va boshq. (2022) InstructGPT; Kaplan va boshq. (2020) masshtab qonunlari; Serl "Nutq aktlari" nazariyasi; Ustun va boshq. (2024) Aya modeli.

## 8-§. Korpus va ma'lumotlar

Bu § "model ma'lumotidan yaxshi bo'la olmaydi" tamoyilini o'zbek korpuslari misolida ko'rsatadi: tilni aniqlash xatolari, yozuv aralashuvi, takrorlar va mashina tarjimasi "axlati"; hajmi 16 bet.

### Reja

1. Korpus lingvistikasi asoslari: korpus turlari, reprezentativlik, metama'lumot.
2. O'zbek tili uchun mavjud ochiq resurslar xaritasi.
3. Veb-korpus sifati: tilni aniqlash, yozuv, takrorlar, past sifatli matn.
4. Annotatsiya: ko'rsatma yozish, annotatorlar kelishuvi.
5. Ma'lumot etikasi: litsenziya, shaxsiy ma'lumot, ma'lumot pasporti (datasheet).

### O'quv maqsadlari

- O'zbek tili uchun kamida 8 ta ochiq resursni nomi, hajmi va litsenziyasi bilan sanab bera oladi.
- Veb-korpusni tozalash quvurini (pipeline) qura oladi.
- Ikki annotator kelishuvini Koen kappasi bilan hisoblay oladi.

### Asosiy tushunchalar

korpus, reprezentativlik, metama'lumot, veb-korpus, tilni aniqlash (language identification), takrorlarni olib tashlash (deduplication), sifat filtri (quality filtering), annotatsiya, annotatsiya ko'rsatmasi (guideline), annotatorlar kelishuvi (inter-annotator agreement), Koen kappasi, ma'lumot pasporti (datasheet), litsenziya (CC BY, CC BY-SA va boshqalar).

### Nazariy matn mazmuni va misollar

- **O'zbek resurslari xaritasi (jadval):** O'zbek tili milliy korpusi, Vikipediya, CC-100, MADLAD-400, FLORES-200, Belebele, Common Voice (nutq), sentiment va NER ma'lumotlari (har biri uchun hajm, yozuv, litsenziya, havola — yozish vaqtida tekshirib to'ldiriladi).
- **Tilni aniqlash xatolari:** o'zbekcha kirill matn boshqa tilga, translit matn esa umuman noma'lum deb belgilanishi misollari.
- **"Mashina tarjimasi axlati":** veb-sahifalardagi sifatsiz avtomatik tarjima belgilari (g'alati kalkalar, so'z tartibi buzilishi) — tilshunos ko'zi bilan aniqlash ro'yxati.
- **Annotatsiya misoli:** "Bu telefon zo'r, lekin batareyasi tez tugaydi" — ijobiymi, salbiymi, aralashmi? Ko'rsatma yozish nega muhim.
- **Tilshunos ko'zi bilan:** korpus tilshunoslikda va NLP'da: maqsad farqi (tavsif va o'qitish).
- **Muhandis ko'zi bilan:** "ma'lumot sifati model hajmidan muhimroq" — so'nggi tadqiqotlardan xulosa.

### Amaliy mashg'ulot (Colab: `08_corpus_quality.ipynb`)

1. Ochiq veb-korpusning o'zbekcha qismidan 20 000 ta hujjatni oqim (streaming) rejimida yuklash.
2. Tilni aniqlash modeli (masalan, fastText lid.176 yoki GlotLID) bilan har hujjatni tekshirish.
3. Yozuvni aniqlash: lotin, kirill, aralash ulushi diagrammasi.
4. MinHash bilan deyarli bir xil hujjatlarni topish va takrorlar foizini hisoblash.
5. Oddiy sifat evristikalari: juda qisqa matnlar, raqam yoki belgi ko'pligi, takrorlanuvchi qatorlar.
6. 100 ta jumlani ikki talaba mustaqil annotatsiya qiladi; Koen kappasini hisoblash.
7. Yakuniy tozalangan korpus uchun ma'lumot pasporti (datasheet) shablonini to'ldirish.

**Kutiladigan natija:** "xom 20 000 → tozalangan N" voronkasi raqamlari va qaysi bosqichda qancha matn yo'qolgani.

### Savol va topshiriqlar

1. Reprezentativ korpus nima? O'zbek tili uchun misol keltiring.
2. O'zbek tilining 5 ta ochiq resursini jadvalda taqqoslang.
3. Tilni aniqlash modeli o'zbekcha matnni qachon xato aniqlaydi?
4. Mashina tarjimasi bo'lgan matnni qanday lingvistik belgilar orqali tanish mumkin?
5. Kappa 0,45 chiqsa, annotatsiya ko'rsatmasini qanday yaxshilaysiz?
6. Veb-korpusdan shaxsiy ma'lumotlarni (telefon, manzil) olib tashlash usullarini yozing.
7. CC BY va CC BY-NC litsenziyalari farqi va tadqiqotga ta'siri.
8. **Loyiha:** 500 jumlali o'zbekcha sentiment to'plamini ko'rsatma va ma'lumot pasporti bilan yarating.

### Test namunasi

1. Koen kappasi nimani o'lchaydi? A) model aniqligini B) **annotatorlar kelishuvini tasodifiy kelishuvdan tashqari** C) korpus hajmini D) lug'at boyligini
2. MinHash nima uchun ishlatiladi? A) tarjima B) **deyarli bir xil hujjatlarni topish** C) tokenizatsiya D) tilni aniqlash

### Tadqiqot uchun mavzular

- Ochiq veb-korpuslarning o'zbekcha qismlari sifatini audit qilish (tilshunos baholashi bilan).
- O'zbek tili uchun tilni aniqlash modellarining kirill, lotin va translit matnlardagi xatolari.

### Qo'shimcha o'qish

Kreutzer va boshq. (2022) "Quality at a Glance" (ko'p tilli veb-korpuslar auditi); Gebru va boshq. (2021) "Datasheets for Datasets"; Kargaran va boshq. (2023) GlotLID; korpus lingvistikasi bo'yicha o'zbekcha qo'llanmalar.

## 9-§. Pragmatika, diskurs va obrazli til

Bu § LLM'ning eng zaif joyini — "aytilmagan ma'no"ni o'zbek madaniyati misollarida sinaydi: iboralar, maqollar, hurmat shakllari, kinoya va so'z o'yini; tilshunoslar uchun kitobning eng qiziqarli bo'limi, hajmi 16–18 bet.

### Reja

1. Pragmatika asoslari: Grays maksimalari va implikatura.
2. Deyksis, presuppozitsiya va kontekst.
3. Xushmuomalalik va hurmat shakllari: siz/sen, hurmat ko'pligi.
4. Obrazli til: ibora, maqol, metafora, kinoya.
5. So'z o'yini va hazil: tajnis, latifalar.
6. Diskurs: bog'lanish (koherensiya) va uzun matn.

### O'quv maqsadlari

- Implikaturani o'zbekcha misolda aniqlay va izohlay oladi.
- LLM'ning ibora va maqollarni tushunishini tizimli baholay oladi.
- Hurmat shakllaridagi xatolarni tasniflay oladi.

### Asosiy tushunchalar

pragmatika, implikatura (implicature), Grays maksimalari (Gricean maxims), presuppozitsiya, deyksis, xushmuomalalik (politeness), hurmat shakli (honorific), frazeologizm (idiom), maqol (proverb), metafora, kinoya (irony), so'z o'yini (wordplay, pun), tajnis, koherensiya (coherence).

### Nazariy matn mazmuni va misollar

- **Implikatura:** mehmon kech qolganda uy egasi "Soat ham o'nga yaqinlashib qoldi-ya" deydi — so'zma-so'z ma'no va nazarda tutilgan ma'no.
- **Hurmat ko'pligi:** "Dadam keldilar" — bitta odam, lekin ko'plik qo'shimchasi; tarjima modeli buni "they came" deb xato qilishi mumkin.
- **Iboralar:** "qo'li ochiq" (saxiy), "tili uzun", "ko'ngli yumshoq", "burnini osmonga ko'tarmoq" — so'zma-so'z tarjima va asl ma'no.
- **Maqollar:** "Ko'rpangga qarab oyoq uzat", "Sabr tagi — sariq oltin" — model ma'noni izohlay oladimi yoki faqat inglizcha muqobilini "o'ylab topadimi"?
- **Tajnis va so'z o'yini:** mumtoz she'riyatdan 2–3 misol; LLM omonimik o'yinni sezadimi? (dissertatsiya tadqiqotingiz bilan to'g'ridan-to'g'ri bog'liq).
- **Latifa:** Nasriddin Afandi latifasidagi hazil mexanizmi va model izohi.
- **Tilshunos ko'zi bilan:** pragmatika — "matndan tashqaridagi bilim"; model faqat matnni ko'rgan.
- **Muhandis ko'zi bilan:** madaniy kontekst — chatbot, mijozlarga xizmat va ta'lim ilovalari sifati uchun hal qiluvchi omil.

### Amaliy mashg'ulot (Colab: `09_pragmatics_test.ipynb`)

1. **O'zbek iboralar testi:** 50 ta ibora, har biri uchun 4 variantli savol (bitta to'g'ri obrazli ma'no, bitta so'zma-so'z tuzoq, ikkita chalg'ituvchi).
2. 2–3 ta ochiq LLM'ni testdan o'tkazish; "so'zma-so'z tuzoq"ni tanlash ulushini alohida hisoblash.
3. NLLB bilan 20 ta iborali jumlani tarjima qilish va so'zma-so'z tarjima foizini qo'lda baholash.
4. **Hurmat testi:** "Dadam keldilar", "Ustozim aytdilar" kabi 20 ta jumla tarjimasida "they" xatosi sonini hisoblash.
5. **Implikatura testi:** 15 ta qisqa dialog; modeldan "so'zlovchi aslida nima demoqchi?" deb so'rash.

**Kutiladigan natija:** "o'zbek pragmatikasi" bo'yicha 3 ta kichik benchmark; ularni GitHub'da `data/pragmatics/` papkasida ochiq e'lon qilish.

### Savol va topshiriqlar

1. Grays maksimalaridan birini buzish orqali hosil bo'lgan o'zbekcha implikatura misolini keltiring.
2. Hurmat ko'pligi mashina tarjimasida qanday muammo tug'diradi?
3. 10 ta iborani so'zma-so'z va obrazli ma'noda tarjima qiling.
4. Model qaysi turdagi maqollarni yaxshiroq tushundi? Gipotezangiz.
5. Tajnisni aniqlash nima uchun LLM uchun ayniqsa qiyin? Tokenizatsiya bilan bog'lang.
6. Bitta latifaning hazil mexanizmini tahlil qiling va modelning izohi bilan solishtiring.
7. Uzun matnda modelning koherensiya xatolarini 3 ta misolda ko'rsating.
8. **Loyiha:** 100 ta o'zbek maqoli uchun "ma'no izohi" benchmarkini tuzing (ma'no, inglizcha muqobil, qo'llanish konteksti).

### Test namunasi

1. "Dadam keldilar" jumlasidagi "-lar" qanday vazifada? A) ko'plik B) **hurmat** C) gumon D) kesim
2. Implikatura nima? A) so'zning lug'aviy ma'nosi B) **aytilgan gapdan kelib chiqadigan, lekin bevosita aytilmagan ma'no** C) grammatik xato D) tarjima usuli

### Tadqiqot uchun mavzular

- LLM'larning o'zbek frazeologizmlarini tushunishi: benchmark va xatolar tipologiyasi.
- Mumtoz va zamonaviy o'zbek matnlaridagi so'z o'yinini LLM'lar aniqlashi va tarjima qilishi (qiyosiy tilshunoslik dissertatsiyasi bilan uyg'un).

### Qo'shimcha o'qish

Grays (1975) "Logic and Conversation"; Braun, Levinson (1987) xushmuomalalik nazariyasi; Ruis va boshq. (2023) LLM'larda implikatura; Liu va boshq. (2022) Fig-QA: til modellarining obrazli tilni tushunishi.

## 10-§. Ko'p tillilik va turkiy tillar

Bu § o'zbek tilini turkiy tillar oilasi ichida ko'rib, bitta model turli tillarda nega turlicha ishlashini o'lchaydi; Xolmanova darsligidagi "Dunyo tillari va tillar tasnifi" mavzusining raqamli davomi, hajmi 16 bet.

### Reja

1. Tillarning genealogik va tipologik tasnifi: turkiy tillar oilasi.
2. Ko'p tilli modellar: tillararo transfer va "ko'p tillilik la'nati".
3. Tillarning raqamli tengsizligi: resurs darajalari tasnifi.
4. Model "qaysi tilda o'ylaydi": ingliz tili markazlilik muammosi.
5. Turkiy tillar uchun hamkorlik: umumiy resurslar va benchmarklar.

### O'quv maqsadlari

- Turkiy tillarni guruhlarga ajratib, o'zbek tilining o'rnini ko'rsata oladi.
- Bir xil parallel test bo'yicha 6 ta tilda model aniqligini solishtira oladi.
- Tillararo transfer qachon ishlashini tushuntira oladi.

### Asosiy tushunchalar

genealogik tasnif, tipologik tasnif, turkiy tillar (qarluq, qipchoq, o'g'uz guruhlari), ko'p tilli model (multilingual model), tillararo transfer (cross-lingual transfer), ko'p tillilik la'nati (curse of multilinguality), parallel ma'lumot, resurs darajasi, ingliz tili markazlilik (English-centrism), oraliq til (pivot language), tillararo vektor fazosi.

### Nazariy matn mazmuni va misollar

- **Turkiy tillar jadvali:** o'zbek (qarluq), uyg'ur (qarluq), qozoq, qirg'iz, tatar (qipchoq), turk, ozarbayjon, turkman (o'g'uz) — yozuv, so'zlashuvchilar soni (yozish vaqtida manba bilan), raqamli resurs darajasi.
- **Umumiy so'zlar:** "suv, tosh, ko'z, bilmoq" turli turkiy tillarda; morfologik o'xshashlik ("kitoblarimizdan" va uning qozoqcha, turkcha muqobillari).
- **Resurs darajalari:** Joshi va boshq. (2020) tillarni 0–5 sinfga bo'ladi; o'zbek, qozoq, turk tillari qaysi sinfda va nega.
- **Transfer gipotezasi:** turk tilida ko'p ma'lumot bor; bu o'zbek tiliga yordam beradimi? Leksik o'xshashlik va yozuv o'xshashligi rolini muhokama qilish.
- **Ingliz tili markazlilik:** tadqiqotlar ko'p tilli modellarning ichki qatlamlarida ingliz tiliga yaqin tasvirlar paydo bo'lishini ko'rsatadi (Wendler va boshq., 2024) — o'zbek tili uchun oqibatlari.
- **Tilshunos ko'zi bilan:** qiyosiy-tarixiy tilshunoslik va modelning "tillar xaritasi" o'xshashmi?
- **Muhandis ko'zi bilan:** kam resursli til uchun eng arzon strategiya — qarindosh tildan transfer va kichik moslashtirish.

### Amaliy mashg'ulot (Colab: `10_turkic_multilingual.ipynb`)

1. Belebele parallel o'qib tushunish testining 6 ta til qismini yuklash: ingliz, turk, o'zbek, qozoq, qirg'iz, ozarbayjon.
2. Bitta kichik ochiq LLM bilan 200 tadan savolda aniqlikni hisoblash; tillar bo'yicha ustunli grafik.
3. LaBSE bilan FLORES-200'dagi parallel jumlalarning tillararo kosinus o'xshashligi matritsasini hisoblash va issiqlik xaritasini chizish.
4. Issiqlik xaritasidan ierarxik klasterlash daraxtini qurish va uni lingvistik tasnif (qarluq, qipchoq, o'g'uz) bilan solishtirish.

**Kutiladigan natija:** modelning "tillar daraxti" va tilshunoslarning genealogik daraxti yonma-yon — kitobning eng esda qoladigan rasmlaridan biri.

### Savol va topshiriqlar

1. Turkiy tillarni guruhlarga ajratib, har guruhdan 2 ta til ayting.
2. Ko'p tillilik la'nati nima? Oddiy misol bilan tushuntiring.
3. Grafikda o'zbek va turk tillari orasidagi farq nima bilan izohlanadi?
4. Modelning tillar daraxti genealogik daraxtdan qayerda farq qildi? Sababi nima bo'lishi mumkin?
5. Yozuv (lotin, kirill, arab) tillararo transferga qanday ta'sir qiladi?
6. O'zbek tili uchun turk tilidan transfer qilishning xavflari nimada ("soxta do'stlar" so'zlar)?
7. 10 ta o'zbekcha–turkcha soxta do'st so'z juftini toping.
8. **Loyiha:** 5 ta turkiy tilda 50 ta parallel jumladan iborat kichik test to'plamini tayyorlang.

### Test namunasi

1. O'zbek tili turkiy tillarning qaysi guruhiga kiradi? A) o'g'uz B) qipchoq C) **qarluq** D) bulg'or
2. Tillararo transfer nima? A) tarjima dasturi B) **bir tilda o'rganilgan bilimni boshqa tilda qo'llash** C) yozuvni almashtirish D) lug'at tuzish

### Tadqiqot uchun mavzular

- Turkiy tillarda LLM sifati tengsizligi: parallel benchmarklar asosida tizimli o'lchov.
- Qarindosh til ma'lumotlari bilan o'zbek tili uchun kichik modelni moslashtirish samaradorligi.

### Qo'shimcha o'qish

Conneau va boshq. (2020) XLM-R; Joshi va boshq. (2020); Bandarkar va boshq. (2024) Belebele; NLLB Team (2022); Wendler va boshq. (2024) "Do Llamas Work in English?"; Xolmanova (2020), 9-§.

## 11-§. Ishonchlilik: gallyutsinatsiya, noaniqlik va kalibrlash

Bu § sizning ilmiy yo'nalishingizni darslik tiliga o'giradi: model qachon "ishonch bilan xato qiladi" va buni o'zbek tilidagi modal so'zlar hamda evidensiallik bilan qanday bog'lash mumkin; kitobning ilmiy "imzosi", hajmi 18 bet.

> **Muallif uchun eslatma:** PhD mavzusi rasman tasdiqlangunga va asosiy maqolalar qabul qilingunga qadar bu § da faqat umumiy usullar va allaqachon e'lon qilingan natijalaringizni bering. Yangi g'oyalarni nashrdan keyin ikkinchi nashrga qo'shing.

### Reja

1. Gallyutsinatsiya: turlari va sabablari.
2. Noaniqlik: model "bilmasligini bilishi" mumkinmi?
3. Kalibrlash: ishonch va to'g'rilik mosligi; ECE, Brier ko'rsatkichi, ishonchlilik diagrammasi.
4. Ishonchni ifodalash usullari: token ehtimoli, so'z bilan ifodalangan ishonch, javoblar izchilligi.
5. Lingvistik ishonch: o'zbek tilidagi modal so'zlar va evidensial shakllar.
6. Kam resursli tillarda ishonchlilik muammosi.

### O'quv maqsadlari

- Gallyutsinatsiya turlarini o'zbekcha misollar bilan tasniflay oladi.
- ECE'ni 10 ta bashorat bo'yicha qo'lda hisoblay oladi.
- Model ishonchini o'zbek va ingliz tillarida ishonchlilik diagrammasi bilan solishtira oladi.

### Asosiy tushunchalar

gallyutsinatsiya (hallucination), faktik xato, noaniqlik (uncertainty), epistemik va aleatorik noaniqlik, ishonch (confidence), kalibrlash (calibration), kutilgan kalibrlash xatosi (ECE), Brier ko'rsatkichi, ishonchlilik diagrammasi (reliability diagram), harorat bilan masshtablash (temperature scaling), so'z bilan ifodalangan ishonch (verbalized confidence), izchillik (self-consistency), epistemik modallik, evidensiallik (evidentiality).

### Nazariy matn mazmuni va misollar

- **Gallyutsinatsiya misollari:** model mavjud bo'lmagan o'zbek shoiri yoki asar nomini "o'ylab topadi"; tarixiy sanani xato beradi; savolga javob o'rniga ishonchli ohangda boshqa narsani aytadi.
- **Ob-havo metaforasi:** "70% yomg'ir" deyilgan kunlarning 70 foizida yomg'ir yog'sa, sinoptik yaxshi kalibrlangan. Modelga ham shu talab qo'yiladi.
- **ECE qo'lda:** 10 ta savol, ishonch va to'g'rilik jadvali, 2 ta "savat" (bin) bilan hisob.
- **O'zbek tilida ishonch belgilari (noyob lingvistik qism):** modal so'zlar ("aniq", "albatta", "ehtimol", "balki", "shekilli", "chamasi"), "-dir" yuklamasi ("kelgandir"), evidensial shakllar ("kelibdi", "kelgan ekan" — so'zlovchi o'zi ko'rmagan). Savol: modelning o'zbekcha javobidagi bu belgilar uning haqiqiy to'g'riligi bilan mos keladimi?
- **Tillararo farq:** ko'plab tadqiqotlar kam resursli tillarda kalibrlash yomonroq ekanini ko'rsatadi; o'zingizning e'lon qilingan natijalaringizni shu yerda misol qiling.
- **Tilshunos ko'zi bilan:** epistemik modallik va evidensiallik — inson tilida "ishonchni kodlash" tizimi.
- **Muhandis ko'zi bilan:** kalibrlangan model "bilmayman" deya oladi — tibbiyot, huquq va ta'limda xavfsiz qo'llashning sharti.

### Amaliy mashg'ulot (Colab: `11_calibration.ipynb`)

1. Belebele'ning o'zbekcha va inglizcha qismidan 300 tadan savol yuklash.
2. Kichik ochiq LLM uchun har bir variant (A–D) harfining ehtimolini olish va softmax bilan ishonchni hisoblash.
3. Aniqlik, ECE, Brier ko'rsatkichini ikki til uchun jadvalda chiqarish.
4. Ikki tilning ishonchlilik diagrammasini yonma-yon chizish.
5. Harorat bilan masshtablashni qo'llab, ECE qanchaga kamayishini ko'rsatish.
6. **Lingvistik qism:** modeldan 50 ta savolga o'zbekcha erkin javob olish; javobdagi modal so'zlarni ("aniq", "ehtimol", "shekilli") avtomatik sanash va javob to'g'riligi bilan bog'liqligini jadvalda ko'rsatish.

**Asosiy kod parchasi:**

```python
import numpy as np
def ece(conf, correct, n_bins=10):
    bins = np.linspace(0, 1, n_bins + 1)
    total = 0.0
    for lo, hi in zip(bins[:-1], bins[1:]):
        m = (conf > lo) & (conf <= hi)
        if m.any():
            total += m.mean() * abs(correct[m].mean() - conf[m].mean())
    return total
```

**Kutiladigan natija:** o'zbek va ingliz tillari ishonchlilik diagrammasi — xalqaro taqdimotlarda kitob va tadqiqotingizni bog'laydigan asosiy rasm.

### Savol va topshiriqlar

1. Gallyutsinatsiyaning 3 turini o'zbekcha misollar bilan tushuntiring.
2. Epistemik va aleatorik noaniqlik farqi nima?
3. Berilgan 10 ta bashorat uchun ECE'ni qo'lda hisoblang.
4. Ishonchlilik diagrammasida chiziq diagonaldan pastda bo'lsa, model qanday "xarakterli"?
5. O'zbek tilidagi 10 ta modal so'zni ishonch darajasi bo'yicha tartiblang (so'rovnoma o'tkazing).
6. "Kelibdi" va "keldi" farqini evidensiallik nuqtayi nazaridan izohlang.
7. Nima uchun kam resursli tilda model ko'proq "ortiqcha ishonch" bildirishi mumkin?
8. **Loyiha:** 30 kishi ishtirokida o'zbekcha modal so'zlarning "ishonch foizi" shkalasini tuzing va modelning o'zbekcha javoblaridagi modal so'zlar bilan solishtiring.

### Test namunasi

1. Yaxshi kalibrlangan model 80% ishonch bildirgan savollarning taxminan qanchasiga to'g'ri javob beradi? A) 50% B) **80%** C) 100% D) 20%
2. Qaysi shakl evidensiallikni bildiradi? A) keldi B) **kelibdi** C) kelyapti D) kelmoqchi

### Tadqiqot uchun mavzular

- O'zbek tilidagi epistemik modal so'zlar va LLM'ning haqiqiy kalibrlanishi: lingvistik ishonch va statistik ishonch mosligi.
- Turkiy tillarda evidensial shakllarning LLM tomonidan qo'llanishi va tarjimasi.

### Qo'shimcha o'qish

Guo va boshq. (2017) "On Calibration of Modern Neural Networks"; Kadavath va boshq. (2022) "Language Models (Mostly) Know What They Know"; Ji va boshq. (2023) gallyutsinatsiya bo'yicha sharh; Aikhenvald (2004) "Evidentiality"; muallifning e'lon qilingan maqolalari.

## 12-§. Baholash va benchmarklar

Bu § "o'zbek tili uchun model yaxshimi?" degan savolga qanday to'g'ri javob berishni o'rgatadi: qaysi ko'rsatkich agglyutinativ tilga mos, tarjima qilingan testlar nega aldaydi va madaniy jihatdan to'g'ri benchmark qanday tuziladi; hajmi 16 bet.

### Reja

1. Baholash turlari: avtomatik, inson va model yordamida baholash.
2. Ko'rsatkichlar: aniqlik, F1, BLEU, chrF, COMET.
3. Benchmarklar: tarjima qilingan va mahalliy yaratilgan testlar.
4. "LLM hakam sifatida" (LLM-as-a-judge) va uning og'ishlari.
5. Ma'lumot sizib chiqishi (contamination) va natijalarni to'g'ri talqin qilish.

### O'quv maqsadlari

- BLEU va chrF farqini o'zbekcha tarjima misolida ko'rsata oladi.
- Tarjima qilingan benchmarkning 3 ta kamchiligini aniqlay oladi.
- 50 savolli madaniy jihatdan to'g'ri o'zbekcha test tuza oladi.

### Asosiy tushunchalar

baholash (evaluation), benchmark, aniqlik (accuracy), F1, BLEU, chrF, COMET, inson baholashi (human evaluation), LLM hakam (LLM-as-a-judge), tarjimaviy til (translationese), madaniy moslik (cultural relevance), ma'lumot sizib chiqishi (data contamination), statistik ahamiyat, ishonch oralig'i (confidence interval).

### Nazariy matn mazmuni va misollar

- **BLEU muammosi:** tayanch tarjima "kitoblarimizni o'qidik", model tarjimasi "kitoblarimizni o'qib chiqdik" — so'z darajasida mos kelmaydi, lekin ma'no to'g'ri. chrF harf darajasida hisoblagani uchun agglyutinativ tillarda adolatliroq.
- **Tarjima qilingan test xatolari:** inglizcha testdagi "Thanksgiving" yoki "Super Bowl" savollari o'zbek foydalanuvchisi uchun ahamiyatsiz; tarjima "tarjimaviy til" belgilarini olib kiradi.
- **Mahalliy benchmark g'oyasi:** o'zbek adabiyoti, tarixi, geografiyasi, urf-odatlari, huquqi bo'yicha savollar; har savol uchun manba va mutaxassis tasdig'i.
- **LLM hakam og'ishlari:** uzunroq javobni afzal ko'rish, o'z javobini afzal ko'rish, o'zbekcha grammatik xatolarni sezmaslik.
- **Statistik to'g'rilik:** 100 savolli testda 2% farq ko'pincha tasodif; ishonch oralig'ini hisoblash qoidasi.
- **Tilshunos ko'zi bilan:** tarjima sifatini baholashda tilshunosning o'rni: adekvatlik va ravonlik (fluency).
- **Muhandis ko'zi bilan:** "reyting jadvali"ga ko'r-ko'rona ishonmaslik qoidalari.

### Amaliy mashg'ulot (Colab: `12_evaluation.ipynb`)

1. FLORES-200 dan 100 ta inglizcha jumlani NLLB bilan o'zbekchaga tarjima qilish.
2. `sacrebleu` bilan BLEU va chrF hisoblash; 20 ta jumlani talaba qo'lda 1–5 ballda baholaydi.
3. Qaysi ko'rsatkich inson bahosi bilan ko'proq mos kelishini korrelyatsiya orqali aniqlash.
4. 30 ta tarjima qilingan umumiy bilim savoli va 30 ta mahalliy o'zbekcha savolda modelni solishtirish.
5. Ochiq LLM'ni hakam sifatida ishlatib, 20 ta javobga baho qo'ydirish va inson bahosi bilan kelishuvini hisoblash.
6. Natijalar uchun bootstrap usulida ishonch oralig'ini chizish.

**Kutiladigan natija:** "chrF inson bahosiga yaqinroq" degan farazni o'z ma'lumotida tekshirish va mahalliy savollar to'plami (repozitoriyga qo'shiladi).

### Savol va topshiriqlar

1. BLEU nega agglyutinativ tillar uchun qattiqqo'l?
2. Tarjima qilingan benchmarkning 3 ta kamchiligini misol bilan yozing.
3. Inson baholashi uchun adekvatlik va ravonlik shkalasini tuzing.
4. LLM hakamning qaysi og'ishi sizning tajribangizda ko'rindi?
5. 100 savolli testda A model 62%, B model 65% oldi. B haqiqatan yaxshiroqmi?
6. Ma'lumot sizib chiqishini aniqlashning 2 ta usulini yozing.
7. O'zbek adabiyoti bo'yicha 10 ta benchmark savoli tuzing (manbasi bilan).
8. **Loyiha:** 200 savolli "UzCulture" mini-benchmarkini 5 ta soha bo'yicha tuzing, ma'lumot pasporti bilan.

### Test namunasi

1. chrF ko'rsatkichi nimaga asoslanadi? A) so'zlar mosligi B) **harf n-grammalari mosligi** C) jumla uzunligi D) inson bahosi
2. Ma'lumot sizib chiqishi nima? A) shaxsiy ma'lumot o'g'irlanishi B) **test savollarining model o'qitish ma'lumotlarida bo'lishi** C) server xatosi D) tarjima xatosi

### Tadqiqot uchun mavzular

- O'zbek madaniyatiga oid savollar benchmarki: yaratish metodologiyasi va LLM'lar bahosi.
- O'zbek tilidagi mashina tarjimasini baholashda avtomatik ko'rsatkichlar va inson bahosi korrelyatsiyasi.

### Qo'shimcha o'qish

Papineni va boshq. (2002) BLEU; Popović (2015) chrF; Rei va boshq. (2020) COMET; Liang va boshq. (2022) HELM; Zheng va boshq. (2023) LLM-as-a-judge.

## 13-§. Etika va til siyosati

Bu § sun'iy intellektni davlat tili, raqamli tenglik va jamiyat nuqtayi nazaridan ko'radi: kim uchun ishlaydi, kimni chetda qoldiradi va O'zbekiston uchun qanday qarorlar kerak; hajmi 14–16 bet.

### Reja

1. Raqamli til tengsizligi va til yo'qolishi xavfi.
2. Og'ish va stereotiplar: gender, yosh, ijtimoiy guruhlar.
3. Yolg'on axborot, deepfake va o'zbek tilidagi media xavfsizligi.
4. Shaxsiy ma'lumotlar, mualliflik huquqi va o'qitish ma'lumotlari.
5. O'zbekistonda sun'iy intellekt va davlat tili siyosati.
6. Mas'uliyatli ishlab chiqish: model kartasi, shaffoflik, inson nazorati.

### O'quv maqsadlari

- Til texnologiyalaridagi 5 ta asosiy etik xavfni misol bilan izohlay oladi.
- Shablon asosida modeldagi stereotiplarni o'lchay oladi.
- O'z modeli yoki ma'lumot to'plami uchun model kartasini yoza oladi.

### Asosiy tushunchalar

raqamli tengsizlik (digital divide), til siyosati (language policy), stereotip, og'ish (bias), adolat (fairness), yolg'on axborot (misinformation), deepfake, shaxsga doir ma'lumot (personal data), mualliflik huquqi (copyright), shaffoflik (transparency), model kartasi (model card), inson nazorati (human oversight), mas'uliyatli sun'iy intellekt (responsible AI).

### Nazariy matn mazmuni va misollar

- **Raqamli tengsizlik:** agar ovozli yordamchi, tarjima va qidiruv o'zbek tilida yomon ishlasa, foydalanuvchilar rus yoki ingliz tiliga o'tadi — bu davlat tilining raqamli maydondagi mavqeiga ta'sir qiladi.
- **Stereotip misollari:** "Ayol kishi … bo'lishi kerak", "Keksa odamlar texnologiyani …" kabi jumlalarni model qanday davom ettiradi.
- **Media xavfsizligi:** o'zbek tilida sun'iy yaratilgan soxta yangiliklarni aniqlashning lingvistik belgilari.
- **Huquqiy kontekst:** O'zbekistonning shaxsga doir ma'lumotlar to'g'risidagi qonuni va sun'iy intellektni rivojlantirish bo'yicha davlat hujjatlari (aniq raqam va sanalarni yozish vaqtida lex.uz'dan tekshiring).
- **Lotin yozuviga o'tish:** ikki yozuvli davr ma'lumotlar sifati va modellar uchun nimani anglatadi.
- **Ayollar va texnologiya:** sohada ayollar ulushi va ma'lumotlardagi gender og'ishi o'rtasidagi bog'liqlik (ixtiyoriy blok, muallif tajribasi asosida).
- **Tilshunos ko'zi bilan:** til siyosati va til ekologiyasi tushunchalari.
- **Muhandis ko'zi bilan:** model kartasi va ma'lumot pasporti — xalqaro amaliyotdagi minimal talab.

### Amaliy mashg'ulot (Colab: `13_ethics_audit.ipynb`)

1. 40 ta shablon jumla: "\[Erkak/ayol/yosh/keksa\] kishi odatda …" kabi; modelga 5 tadan davom ettirish berish.
2. Davomlarni ijobiy, neytral, salbiy toifaga ajratish (qo'lda va oddiy sentiment modeli bilan).
3. Guruhlar bo'yicha salbiy davomlar ulushini grafikda solishtirish.
4. 3–4 bobdagi tajribalar asosida o'z kichik modeli yoki ma'lumot to'plami uchun model kartasini o'zbek va ingliz tillarida to'ldirish (shablon repozitoriyda).

**Kutiladigan natija:** stereotiplar auditi grafigi va to'liq model kartasi; talaba buni portfoliosiga qo'shadi.

### Savol va topshiriqlar

1. Raqamli tengsizlik davlat tilining mavqeiga qanday ta'sir qiladi?
2. Auditda qaysi guruhga nisbatan salbiy davomlar ko'proq chiqdi? Sababi nima bo'lishi mumkin?
3. O'zbekcha soxta yangilikni aniqlashning 5 ta lingvistik belgisini yozing.
4. O'zbek mualliflarining matnlarini model o'qitishda ishlatish etikmi? Ikki tomon dalillari.
5. Shaxsga doir ma'lumotlar to'g'risidagi qonunning NLP loyihalariga ta'sirini qisqacha tahlil qiling.
6. Model kartasining asosiy bo'limlarini sanab bering.
7. "Inson nazorati" ta'lim sohasidagi sun'iy intellekt ilovasida qanday ko'rinishi kerak?
8. **Loyiha:** maktab yoki universitet uchun "Sun'iy intellektdan mas'uliyatli foydalanish" bo'yicha 1 betlik qoidalar loyihasini yozing.

### Test namunasi

1. Model kartasi nima? A) reklama materiali B) **modelning maqsadi, ma'lumoti, cheklovlari va xavflari haqidagi hujjat** C) litsenziya kaliti D) foydalanuvchi qo'llanmasi
2. Raqamli tengsizlik nimani anglatadi? A) internet tezligi farqi B) **tillar va guruhlar texnologiyadan teng foydalana olmasligi** C) kompyuter narxi D) dasturlash tillari farqi

### Tadqiqot uchun mavzular

- O'zbek tilidagi LLM javoblaridagi gender va yosh stereotiplari: shablon asosidagi audit.
- O'zbekistonda davlat tilining raqamli maydondagi mavqei va sun'iy intellekt siyosati.

### Qo'shimcha o'qish

Bender va boshq. (2021) "On the Dangers of Stochastic Parrots"; Mitchell va boshq. (2019) "Model Cards for Model Reporting"; Blodgett va boshq. (2020) NLP'dagi og'ish tadqiqotlari tanqidi; YuNESKO (2021) sun'iy intellekt etikasi bo'yicha tavsiya.

## 14-§. Kelajak yo'nalishlari va yakuniy loyiha

Bu § kitobni amaliyot bilan yakunlaydi: nutq texnologiyalari, RAG, kichik modellarni moslashtirish va tilshunos uchun AI sohasidagi kasblar; o'quvchi o'z yakuniy loyihasini tanlab, GitHub'da e'lon qiladi; hajmi 14–16 bet.

### Reja

1. Nutq texnologiyalari: o'zbek tilida nutqni tanish (ASR) va nutq sintezi (TTS).
2. Qidiruv bilan boyitilgan generatsiya (RAG): o'zbekcha hujjatlar ustida savol-javob.
3. Kichik modellarni moslashtirish: LoRA va ko'rsatmalar to'plami.
4. Multimodal modellar va agentlar: til endi faqat matn emas.
5. Tilshunos uchun AI sohasidagi kasblar va kompetensiyalar.
6. Yakuniy loyiha: tanlash, bajarish, e'lon qilish.

### O'quv maqsadlari

- O'zbekcha hujjatlar uchun oddiy RAG tizimini qura oladi.
- O'z loyihasini reproducible (qayta takrorlanadigan) ko'rinishda GitHub'da e'lon qila oladi.
- AI sohasidagi 5 ta tilshunoslik kasbini va ularga kerakli ko'nikmalarni ayta oladi.

### Asosiy tushunchalar

nutqni tanish (ASR), nutq sintezi (TTS), so'z xatosi darajasi (WER), RAG (retrieval-augmented generation), vektor ma'lumotlar bazasi, moslashtirish (fine-tuning), LoRA, ko'rsatmalar to'plami (instruction dataset), multimodal model, agent, takrorlanuvchanlik (reproducibility), portfolio.

### Nazariy matn mazmuni va misollar

- **ASR misoli:** ko'p tilli nutq modeli o'zbekcha audiodagi "o'" va "u", "g'" va "g" farqini qanchalik ajratadi; shevadagi nutq bilan sifat qanday tushadi.
- **RAG sxemasi:** savol → hujjatlardan eng yaqin parchalarni topish → parchalar bilan birga modelga berish → manbaga havola qilingan javob. Misol: "Talabalar uchun akademik ta'til qanday rasmiylashtiriladi?" (universitet nizomi asosida).
- **Kichik model moslashtirish:** 500–1 000 ta sifatli o'zbekcha savol-javob juftligi kichik modelni sezilarli yaxshilashi mumkin; bunda tilshunosning ko'rsatmalar sifatini nazorat qilishi hal qiluvchi.
- **Kasblar jadvali:** kompyuter lingvisti, ma'lumot annotatsiyasi rahbari, lingvistik sifat nazoratchisi, model baholash mutaxassisi, prompt va kontent dizayneri — vazifa va ko'nikmalar.
- **Tilshunos ko'zi bilan:** til fanining kelajagi — "nazariya + ma'lumot + kod".
- **Muhandis ko'zi bilan:** kam resursli til uchun eng katta qiymat — sifatli ma'lumot va to'g'ri baholash.

### Amaliy mashg'ulot (Colab: `14_capstone_rag.ipynb`)

1. 20–30 ta o'zbekcha hujjat (masalan, ochiq universitet nizomlari yoki ochiq huquqiy matnlar) yuklash va 300 so'zli bo'laklarga ajratish.
2. Ko'p tilli embedding modeli bilan vektorlarga aylantirish (masalan, multilingual-e5).
3. FAISS bilan qidiruv; 10 ta savol uchun eng yaqin 3 bo'lakni chiqarish.
4. Kichik ochiq LLM bilan bo'laklarga asoslangan javob generatsiya qilish va manbani ko'rsatish.
5. 10 ta savol bo'yicha javob to'g'riligi va manba to'g'riligini qo'lda baholash.

### Yakuniy loyiha variantlari

| # | Loyiha | Kitobdagi asos | Natija |
| --- | --- | --- | --- |
| 1 | Turkiy tillar tokenizatsiya adolati auditi | 4-§ | Grafiklar + 4 betlik hisobot |
| 2 | O'zbekcha minimal juftliklar benchmarki (500+) | 6-§ | Ochiq ma'lumot to'plami |
| 3 | O'zbek iboralari va maqollari testi | 9-§ | Benchmark + model bahosi |
| 4 | O'zbekcha modal so'zlar va model ishonchi | 11-§ | Tadqiqot hisoboti |
| 5 | O'zbekcha hujjatlar uchun RAG yordamchisi | 14-§ | Ishlaydigan demo |

**Baholash rubrikasi (100 ball):** muammo qo'yilishi va lingvistik asoslash — 20; ma'lumot sifati va hujjatlashtirish — 20; usul va kod takrorlanuvchanligi — 25; natijalar talqini va cheklovlar — 20; GitHub README va taqdimot — 15.

### Savol va topshiriqlar

1. ASR o'zbek shevalarida nega yomonroq ishlaydi?
2. RAG gallyutsinatsiyani qanday kamaytiradi va qanday hollarda kamaytirmaydi?
3. Kichik modelni moslashtirishda tilshunosning o'rni nimada?
4. O'zingizga mos AI kasbini tanlang va 1 yillik o'rganish rejasini yozing.
5. Yakuniy loyihangiz uchun 1 betlik taklif yozing: muammo, ma'lumot, usul, kutilgan natija.
6. Loyihangiz README'sini ingliz tilida yozing (repozitoriydagi shablon asosida).

### Test namunasi

1. RAG'da "retrieval" bosqichi nima qiladi? A) javob yozadi B) **savolga mos hujjat parchalarini topadi** C) modelni o'qitadi D) matnni tarjima qiladi
2. WER nimani o'lchaydi? A) tarjima sifatini B) **nutqni tanishdagi so'z xatolari ulushini** C) model hajmini D) tokenlar sonini

### Tadqiqot uchun mavzular

- O'zbek shevalarida nutqni tanish sifatini o'lchash uchun test to'plami.
- O'zbek tilida RAG tizimlari uchun embedding modellarini solishtirish.

### Qo'shimcha o'qish

Lewis va boshq. (2020) RAG; Hu va boshq. (2021) LoRA; Radford va boshq. (2022) Whisper; Pratap va boshq. (2023) MMS (1 000+ til uchun nutq modellari).

## Ilovalar

### Ilova A. Inglizcha–o'zbekcha terminlar lug'ati (namuna)

Lug'at 400+ termindan iborat bo'ladi; har bir termin uchun o'zbekcha muqobil, qisqa ta'rif va u kiritilgan § beriladi. Terminlarni tilshunos hamkoringiz bilan birga tekshiring: bitta termin — bitta o'zbekcha muqobil, butun kitob bo'ylab.

| Inglizcha | O'zbekcha | Qisqa ta'rif | § |
| --- | --- | --- | --- |
| token | token | Model matnni bo'ladigan eng kichik birlik | 4 |
| tokenization | tokenizatsiya | Matnni tokenlarga ajratish jarayoni | 4 |
| fertility | fertillik (so'z boshiga token) | Bir so'zga to'g'ri keladigan o'rtacha tokenlar soni | 4 |
| embedding | embedding, vektor tasvir | So'z yoki matnning sonlar ketma-ketligi ko'rinishidagi ifodasi | 5 |
| cosine similarity | kosinus o'xshashlik | Ikki vektor yo'nalishlari yaqinligi o'lchovi | 5 |
| language model | til modeli | Matn ketma-ketligi ehtimolini baholovchi model | 6 |
| perplexity | perplexity (chalkashlik) | Model matnni bashorat qilishdagi noaniqlik o'lchovi | 6 |
| attention | attention (diqqat mexanizmi) | Har bir token uchun boshqa tokenlarning ahamiyatini hisoblash | 6 |
| pretraining | oldindan o'qitish | Katta matnlarda keyingi tokenni bashorat qilib o'qitish | 7 |
| instruction tuning | ko'rsatmaga moslashtirish | Modelni ko'rsatma va javob juftliklarida qo'shimcha o'qitish | 7 |
| in-context learning | kontekstda o'rganish | Promptdagi namunalar asosida vazifani bajarish | 7 |
| deduplication | takrorlarni olib tashlash | Korpusdagi bir xil yoki deyarli bir xil matnlarni o'chirish | 8 |
| inter-annotator agreement | annotatorlar kelishuvi | Turli annotatorlar belgilari mosligi | 8 |
| implicature | implikatura | Bevosita aytilmagan, lekin nazarda tutilgan ma'no | 9 |
| cross-lingual transfer | tillararo transfer | Bir tilda o'rganilgan bilimni boshqa tilda qo'llash | 10 |
| hallucination | gallyutsinatsiya | Modelning asossiz yoki noto'g'ri ma'lumotni ishonch bilan berishi | 11 |
| calibration | kalibrlash | Model ishonchi va haqiqiy to'g'rilik mosligi | 11 |
| evidentiality | evidensiallik | Ma'lumot manbasini grammatik ifodalash | 11 |
| benchmark | benchmark, sinov to'plami | Modellarni solishtirish uchun standart test | 12 |
| data contamination | ma'lumot sizib chiqishi | Test savollarining o'qitish ma'lumotida bo'lishi | 12 |
| model card | model kartasi | Model haqidagi standart hujjat | 13 |
| retrieval-augmented generation | qidiruv bilan boyitilgan generatsiya | Hujjatlardan topilgan parchalar asosida javob yaratish | 14 |

**GitHub fayl formati** (`glossary/glossary_en_uz.csv`):

```csv
term_en,term_uz,definition_uz,chapter,status
token,token,"Model matnni bo'ladigan eng kichik birlik",4,approved
calibration,kalibrlash,"Model ishonchi va haqiqiy to'g'rilik mosligi",11,approved
```

### Ilova B. Python va Colab bo'yicha qisqa yo'riqnoma

Dasturlash bilmaydigan tilshunoslar uchun 5 bet: Colab'ni ochish, kodni ishga tushirish, GPU yoqish, faylni yuklash, xatoni o'qish; 10 ta eng zarur Python buyrug'i o'zbekcha matn misollarida.

### Foydalanilgan adabiyotlar (asosiy ro'yxat)

Yakuniy ro'yxat 100–130 manbadan iborat bo'lishi kerak: taxminan 60% xalqaro maqolalar va kitoblar, 25% o'zbek va turkiy tilshunoslik manbalari, 15% ma'lumot to'plamlari va dasturiy vositalar hujjatlari. Asosiy manbalar:

- Jurafsky D., Martin J. H. Speech and Language Processing. 3-nashr qoralamasi (onlayn).
- Xolmanova Z. Tilshunoslik nazariyasi. – Toshkent: Nodirabegim, 2020.
- Vaswani A. va boshq. Attention Is All You Need. NeurIPS, 2017.
- Mikolov T. va boshq. Efficient Estimation of Word Representations in Vector Space, 2013.
- Bojanowski P. va boshq. Enriching Word Vectors with Subword Information. TACL, 2017.
- Sennrich R., Haddow B., Birch A. Neural Machine Translation of Rare Words with Subword Units. ACL, 2016.
- Petrov A. va boshq. Language Model Tokenizers Introduce Unfairness Between Languages. NeurIPS, 2023.
- Joshi P. va boshq. The State and Fate of Linguistic Diversity and Inclusion in the NLP World. ACL, 2020.
- Conneau A. va boshq. Unsupervised Cross-lingual Representation Learning at Scale. ACL, 2020.
- Bandarkar L. va boshq. The Belebele Benchmark. ACL, 2024.
- NLLB Team. No Language Left Behind, 2022.
- Guo C. va boshq. On Calibration of Modern Neural Networks. ICML, 2017.
- Kadavath S. va boshq. Language Models (Mostly) Know What They Know, 2022.
- Bender E., Koller A. Climbing towards NLU. ACL, 2020.
- Bender E. va boshq. On the Dangers of Stochastic Parrots. FAccT, 2021.
- Mitchell M. va boshq. Model Cards for Model Reporting. FAT\*, 2019.
- Gebru T. va boshq. Datasheets for Datasets. CACM, 2021.
- Kreutzer J. va boshq. Quality at a Glance. TACL, 2022.
- Grice H. P. Logic and Conversation, 1975.
- Aikhenvald A. Evidentiality. Oxford University Press, 2004.

Har bir manbani nashrga topshirishdan oldin asl nusxasi bilan tekshiring (yil, sahifa, nashriyot) va DOI qo'shing.

## Nashr yo'li, ish jadvali va karyera strategiyasi

Haftasiga 3–4 soat bilan qo'lyozma taxminan 10 oyda tayyor bo'ladi, ITPU'dagi sinov va taqriz bilan birga nashrgacha 13–14 oy ketadi: 2026-yil noyabridan 2027-yil dekabrigacha.

### Ish jadvali

| Davr | Nima qilinadi | Natija |
| --- | --- | --- |
| 2026 noyabr–dekabr | GitHub skeleti, README, lug'at boshlanishi; 3- va 4-§ | 2 ta § + 2 ta daftarcha |
| 2027 yanvar–fevral | 2-, 5-, 6-§ | 3 ta § + daftarchalar |
| 2027 mart–aprel | 9-, 10-§; maqolalar qabul qilingach 11-§ | 3 ta § |
| 2027 may–iyun | 7-, 8-, 12-§ | 3 ta § |
| 2027 iyul–avgust | 1-, 13-, 14-§, kirish, ilovalar | To'liq qo'lyozma |
| 2027 sentabr–noyabr | ITPU'da sinov (tanlov fani yoki 6–8 ta mashg'ulot), talabalar fikri, tahrir, taqrizlar | Tahrirlangan qo'lyozma |
| 2027 dekabr | Ilmiy kengash tavsiyasi, nashriyot, ISBN; GitHub v1.0 + Zenodo DOI | Nashr |

Yozish tartibi ataylab 3- va 4-§ dan boshlanadi: bu sizning eng kuchli sohangiz va ular eng ko'p ulashiladigan natijalarni (o'zbek tili soligi, gender og'ishi) beradi.

### Nashr yo'li

1. Avval **o'quv qo'llanma** sifatida: ITPU ilmiy kengashi tavsiyasi → nashriyot (hamkoringiz orqali) → ISBN, UO'K, KBK.
2. Keyin, sinov va fikrlar asosida, vazirlik ruxsati bilan **darslik** sifatida qayta nashr.
3. Aniq talablarni (taqrizlar soni, hajm, rasmiylashtirish) ITPU o'quv-uslubiy bo'limi va nashriyotdan yozma ravishda oling.

**Taqrizchilar:** bittasi tilshunoslik bo'yicha fan doktori (f.f.d. yoki DSc), ikkinchisi texnika yoki informatika bo'yicha fan doktori; GitHub qismi uchun ixtiyoriy ravishda turkiy tillar NLP'si bilan shug'ullanuvchi xorijiy tadqiqotchidan qisqa fikr.

**Hamkor bilan kelishuv:** mualliflik, nashr xarajatlari va huquqlar (ayniqsa, GitHub'dagi ochiq materiallar va inglizcha versiya huquqi) yozma ravishda oldindan kelishib olinsin.

### Karyera strategiyasi: kitobni xalqaro portfolioga aylantirish

- **Har bir § = bitta ochiq natija.** 4-, 6-, 9-, 12-§ dagi test to'plamlari alohida ochiq ma'lumot sifatida e'lon qilinadi; ularning har biri qisqa resurs maqolasiga aylanishi mumkin.
- **Ta'lim maqolasi:** kursning o'zi haqida NLP ta'limiga bag'ishlangan xalqaro seminarlarga (masalan, ACL qoshidagi Teaching NLP seminari) yoki turkiy tillar NLP seminarlariga maqola yuborish.
- **Inglizcha hamroh:** GitHub README va daftarchalar ingliz tilida tushunarli bo'lsin; keyinchalik arXiv'ga 10–15 betlik "course and resources" preprinti.
- **Ko'rinish:** har § tugaganda LinkedIn'da bitta grafik va 5 qatorli izoh (masalan, "o'zbek tili soligi"); PhD mavzusi bo'yicha yangi g'oyalarni oshkor qilmasdan, faqat e'lon qilingan natijalar.
- **CV va arizalar uchun:** "Author of the first Uzbek-language textbook on AI linguistics; open course materials used at IT Park University; N GitHub stars, M forks" — o'lchanadigan dalillar bilan.
- **Jamiyatga foyda:** GAP Women IT Union orqali Namangan va boshqa hududlarda tilshunos ayollar uchun "Tilshunosdan AI mutaxassisigacha" bepul seminarlar; daftarchalar maktab o'qituvchilari uchun ham soddalashtirilgan.

### Xavflar va choralar

| Xavf | Chora |
| --- | --- |
| Vaqt yetmasligi, PhD ustuvorligi | Haftasiga 3–4 soat chegarasi; maqola muddatlarida kitob to'xtatiladi |
| Modellar tez eskiradi | Matn tamoyillarga asoslanadi, aniq modellar faqat daftarchalarda va versiyalangan |
| Ma'lumot litsenziyalari | Har bir to'plam `DATA_SOURCES.md` da litsenziyasi bilan; noaniq bo'lsa ishlatilmaydi |
| PhD g'oyalarining erta oshkor bo'lishi | 11-§ faqat e'lon qilingan natijalar bilan; yangi g'oyalar ikkinchi nashrda |
| Terminologiya bo'yicha tortishuvlar | Lug'at hamkor tilshunos bilan tasdiqlanadi va GitHub'da ochiq muhokamaga qo'yiladi |
