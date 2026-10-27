<div align="center">

# Sun'iy intellekt lingvistikasi
### O'quv qo'llanma uchun ochiq materiallar

**Katta til modellari tilni qanday qayta ishlaydi va bu til o'zbek tili bo'lsa nima bo'ladi?**

[English](README.md) · [Boblar](#boblar) · [Tez boshlash](#tez-boshlash) · [Terminlar lug'ati](glossary/)

</div>

---

## Nima uchun

NLP bo'yicha darsliklarning aksariyati ingliz tili misolida yozilgan. O'zbek tili esa
agglyutinativ, ikki yozuvli va kam resursli til sifatida zamonaviy til modellarida boshqacha
"o'zini tutadi":

- **Qimmatroq:** bir xil mazmun inglizchaga qaraganda ko'proq tokenga bo'linadi.
- **Kam vakillik:** o'qitish ma'lumotlarida o'zbek tilining ulushi juda kichik.
- **Ishonch bilan xato qilish:** kam resursli tillarda modelning ishonchliligi va kalibrlanishi pasayadi.

Bu repozitoriy ***Sun'iy intellekt lingvistikasi*** o'quv qo'llanmasiga hamroh bo'lib, har bir
bobni ishlaydigan Colab daftarchasi, ochiq ma'lumot to'plami yoki foydali vositaga aylantiradi.
U **sun'iy intellektni tushunmoqchi bo'lgan tilshunoslar** va **tilni tushunmoqchi bo'lgan muhandislar** uchun.

## Tarkibi

| Papka | Mazmuni |
|---|---|
| `notebooks/` | 14 ta Colab daftarchasi, har bir bob uchun bittadan |
| `src/uzling/` | Kichik Python kutubxonasi: apostrofni normallashtirish, kirill→lotin transliteratsiya, tokenizatsiya ko'rsatkichlari, kalibrlash metrikalari |
| `glossary/` | Inglizcha–o'zbekcha sun'iy intellekt terminlari lug'ati |
| `data/` | Kurs davomida yaratilgan ochiq test to'plamlari va ularning manbalari |
| `slides/` | O'qituvchilar uchun slaydlar |

## Boblar

1. Sun'iy intellekt lingvistikasi fan sifatida
2. Til belgilar tizimi sifatida va mashina uchun til
3. O'zbek tilining mashina uchun xususiyatlari
4. Tokenizatsiya va morfologiya
5. Leksika, semantika va embeddinglar
6. Sintaksis va til modellari
7. Katta til modellari
8. Korpus va ma'lumotlar
9. Pragmatika, diskurs va obrazli til
10. Ko'p tillilik va turkiy tillar
11. Ishonchlilik: gallyutsinatsiya, noaniqlik va kalibrlash
12. Baholash va benchmarklar
13. Etika va til siyosati
14. Kelajak yo'nalishlari va yakuniy loyiha

## Tez boshlash

Istalgan daftarchani oching va **Open in Colab** tugmasini bosing. Birinchi katak kerakli
kutubxonalarni o'zi o'rnatadi. Kompyuterda ishlatish uchun [README.md](README.md#quick-start) ga qarang.

## Model litsenziyalari

Barcha daftarchalar faqat **ochiq yuklab olinadigan** modellar va tokenizatorlar bilan ishlaydi:
Hugging Face hisobi, token yoki litsenziyani qabul qilish shart emas. Asosiy toʻplam — Qwen2.5, XLM-R va
mT5 (taqqoslash uchun GPT-2 va ByT5). Llama va Gemma litsenziyani qabul qilishni talab qiladi, shuning
uchun ular **ixtiyoriy**: `HF_TOKEN` oʻrnatilgan va litsenziya qabul qilingan boʻlsagina ishlatiladi,
aks holda daftarcha ularni xabar bilan oʻtkazib yuboradi. Kitobdagi barcha natija va rasmlar ochiq
modellar asosida olingan.

## Hissa qo'shish

Lug'atdagi tuzatishlar, yangi o'zbekcha misollar va sheva materiallari juda qadrlanadi.
Batafsil: [CONTRIBUTING.md](CONTRIBUTING.md).

## Muallif

**Dilrabo Khidirova** — IT Park University, mashinali o'qitish bo'yicha katta o'qituvchi.

## Litsenziya

Kod: MIT. Matn, lug'at va loyihada yaratilgan ma'lumotlar: CC BY 4.0.
