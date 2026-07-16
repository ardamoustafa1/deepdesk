# Sprint 2 — Sprint Retrospective

**Tarih:** 16 Temmuz 2026
**Format:** Başla / Durdur / Devam Et (Start / Stop / Continue)

## 🟢 İyi Gidenler (Devam Et)
- Sprint 1 retrospektifinde alınan "story point tahminlerini gerçekçi
  yap" kararına uyulması: Sprint 2 kapsamı (11 puan) kapasiteyle
  neredeyse birebir örtüştü, Sprint 1'deki gibi aşırı yüklenme olmadı.
- Her user story için önce dil/geri bildirim mantığını agent
  seviyesinde bağımsız test etmek (mock Groq client ile), sonra
  orchestrator'a entegre etmek hataları erken yakalamayı sağladı.
- Yeni özellikleri (dil desteği, geri bildirim) mevcut fonksiyon
  imzalarına varsayılan parametre olarak eklemek (`language="tr"`,
  `feedback_notes=None`), Sprint 1 kodunun ve testlerinin hiçbirini
  bozmadan geriye dönük uyumluluğu korudu.

## 🔴 Zorlanılanlar (Durdur)
- Yerel geliştirme ortamındaki güncel Python sürümü, Streamlit'in
  isteğe bağlı `uvloop` bağımlılığıyla uyumsuz çıktı ve web arayüzü
  ilk denemede başlatılamadı; kök nedeni (uvloop'un bu Python sürümünü
  henüz desteklememesi) bulup bağımlılığı kaldırarak çözüldü. Sprint
  3'te ortam/bağımlılık sürümlerini önceden kontrol etmek zaman
  kazandıracak.
- Geri bildirimleri "benzer konu" olarak eşleştirmek için ilk planda
  ChromaDB'yi de düşünmüştüm; basit bir kelime kesişimi algoritmasının
  yeterli olduğuna karar vermek biraz zaman aldı.

## 🟡 Denenecekler (Başla)
- Sprint 3'te PDF export ve kaynak skorlama için, agent promptlarını
  yazmadan önce çıktı formatının (şema/şablon) net bir tanımını
  yapmak.
- Gerçek Groq API anahtarıyla erken bir "smoke test" günü ayırmak;
  böylece dokümantasyon ve ekran görüntüleri son güne kalmadan
  hazırlanabilir.

## Aksiyon Maddeleri

| Aksiyon | Sorumlu | Durum |
|---|---|---|
| Gerçek API anahtarıyla uçtan uca doğrulama (CLI TR/EN + web) | Solo geliştirici | ✅ Tamamlandı (16 Temmuz 2026) |
| Doğrulama kanıtlarının görsel (PNG) ekran görüntülerini ekle | Solo geliştirici | ✅ Tamamlandı (16 Temmuz 2026) |
| Public GitHub Projects Sprint 2 board oluştur | Solo geliştirici | ✅ Tamamlandı (16 Temmuz 2026) |
| Sprint 3 için US-13/US-14 çıktı şemalarını önceden taslakla | Solo geliştirici | Sprint 3 başlangıcı |
| Bağımlılık/ortam uyumluluğunu Sprint başında kontrol et | Solo geliştirici | Sprint 3 başlangıcı |
