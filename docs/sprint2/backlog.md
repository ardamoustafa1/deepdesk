# Sprint 2 — Backlog Dağıtma Mantığı

**Sprint Süresi:** 6 Temmuz 2026 – 19 Temmuz 2026
**Sprint Hedefi:** Sprint 1'in CLI-only MVP'sini, Sprint 1 retrospektifinde
belirlenen üç bekleyen user story ile genişletmek: basit bir web arayüzü,
kullanıcı geri bildirim döngüsü ve çoklu dil (TR/EN) desteği.

## Sprint 1'den Devralınan Ders
Sprint 1 retrospektifinde "story point tahminlerini daha gerçekçi yap"
aksiyonu alınmıştı (bkz. [Sprint 1 retrospective](../sprint1/sprint_retrospective.md)).
Bu nedenle Sprint 2 kapsamı, Sprint 1'de zaten planlanmış olan US-10,
US-11 ve US-12 ile sınırlı tutuldu; ek kapsam eklenmedi.

## Sprint 2 User Story'leri

| ID | User Story | Story Point | Durum |
|---|---|---|---|
| US-10 | Streamlit tabanlı basit web arayüzü | 5 | ✅ Tamamlandı |
| US-11 | Rapor kalitesi için kullanıcı geri bildirim döngüsü | 3 | ✅ Tamamlandı |
| US-12 | Çoklu dil desteği (EN/TR) | 3 | ✅ Tamamlandı |

**Toplam tamamlanan:** 11 / 11 puan (kapasiteyle birebir eşleşti — Sprint 1
retrospektifindeki "gerçekçi kapasite" aksiyonu bu sprintte uygulandı).

## Kabul Kriterleri (Definition of Done)

**US-10 — Streamlit web arayüzü**
- `streamlit run web_app.py` ile tarayıcıda çalışan bir arayüz açılmalı.
- Konu girişi, alt sorular, rapor ve rapor indirme (.md) desteklenmeli.
- Boş konu (empty), API anahtarı eksikliği (error), yükleniyor (loading)
  ve başarılı sonuç (success) durumlarının hepsi ele alınmalı.

**US-11 — Geri bildirim döngüsü**
- Kullanıcı, ürettiği her rapor için 1-5 arası puan ve opsiyonel yorum
  bırakabilmeli (hem CLI hem web arayüzünden).
- Geri bildirimler kalıcı olarak saklanmalı (`reports/feedback.json`).
- Benzer bir konu tekrar araştırıldığında, geçmiş yorumlar Writer Agent'a
  bağlam olarak verilmeli.

**US-12 — Çoklu dil desteği**
- Planner, Research ve Writer agent'ları hem Türkçe hem İngilizce sistem
  promptlarını desteklemeli.
- CLI'da `--lang tr|en` bayrağı, web arayüzünde dil seçici bulunmalı.
- `DEEPDESK_DEFAULT_LANGUAGE` ortam değişkeni ile varsayılan dil
  ayarlanabilmeli.

## Sprint 2'den Sprint 3'e Aktarılan (Backlog'da Bekleyen)

| ID | User Story | Tahmini Puan |
|---|---|---|
| US-13 | PDF export (rapor çıktısını PDF olarak da kaydetme) | 3 |
| US-14 | Gelişmiş kaynak doğrulama ve rapor skorlama | 5 |
