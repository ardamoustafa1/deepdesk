# Sprint 2 — Sprint Review

**Tarih:** 16 Temmuz 2026
**Katılımcılar:** Solo geliştirici (tüm Scrum rolleriyle)

## Sprint Hedefine Ulaşıldı mı?
✅ **Evet.** Sprint 1'in CLI-only MVP'sinden devralınan üç user story
(US-10, US-11, US-12) eksiksiz tamamlandı ve mevcut Sprint 1 işlevselliği
bozulmadan korundu.

## Tamamlanan İşler (Demo Edilenler)
- Streamlit web arayüzünden bir araştırma konusu girilip; alt sorular,
  rapor ve rapor indirme (.md) akışının uçtan uca çalışması
- Boş konu, eksik API anahtarı ve dil değişimi durumlarının arayüzde
  doğru şekilde ele alınması
- Rapor sonrası 1-5 arası puan + yorum bırakılabilmesi (hem CLI hem web)
  ve bu geri bildirimlerin `reports/feedback.json` içinde kalıcı olması
- Benzer bir konu tekrar araştırıldığında geçmiş geri bildirim
  yorumlarının Writer Agent'ın rapor promptuna otomatik eklenmesi
- `python main.py "konu" --lang en` ile İngilizce; bayrak verilmeden
  Türkçe rapor üretilmesi
- 19/19 birim testinin geçmesi (7 yeni test bu sprintte eklendi)

## Tamamlanamayan / Ertelenen İşler
Yok — planlanan US-10, US-11, US-12 tamamlandı. Gerçek Groq API
anahtarıyla canlı uçtan uca çalıştırma (CLI TR/EN + web arayüzü)
16 Temmuz 2026'da yapıldı; görsel ekran görüntüleri ve public GitHub
Projects Sprint 2 board'u (bkz. [sprint_board.md](sprint_board.md))
eklendi.

## Paydaş (Stakeholder) Geri Bildirimi
> Solo geliştirme sürecinde bu rol, bootcamp eğitim asistanı ile
> yapılan ofis saati görüşmelerinde karşılanmaya çalışılmıştır.
> Sprint 1 retrospektifinde belirlenen "eğitim asistanından erken geri
> bildirim isteme" aksiyonu bu sprintte de sürdürülmüştür.

## Sonraki Sprint'e Taşınan Öncelikler
1. PDF export (US-13)
2. Gelişmiş kaynak doğrulama ve rapor skorlama (US-14)
