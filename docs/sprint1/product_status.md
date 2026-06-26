# Sprint 1 — Ürün Durumu

## Genel Durum
Sprint 1 sonunda DeepDesk'in **çekirdek MVP'si tam fonksiyonel** durumda:

✅ Kullanıcı bir araştırma konusu giriyor
✅ Planner Agent konuyu alt sorulara bölüyor
✅ Research Agent her alt soruyu web'de araştırıyor (kaynaklı)
✅ Writer Agent bulguları profesyonel bir Markdown rapora dönüştürüyor
✅ Hafıza katmanı geçmiş araştırmaları saklıyor ve geri çağırıyor
✅ Rapor otomatik olarak dosyaya kaydediliyor
✅ Zengin (rich) terminal arayüzü ile kullanıcı deneyimi iyileştirildi

## Örnek Kullanım Akışı

```bash
$ python main.py "yapay zeka ajanlarının 2026 pazar trendleri"

╭─────────────────────────────────────────╮
│ DeepDesk Araştırma Asistanı              │
│ Konu: yapay zeka ajanlarının 2026 pazar  │
│ trendleri                                │
╰─────────────────────────────────────────╯

⠋ Planlanıyor, araştırılıyor ve yazılıyor...

Alt Sorular:
  • AI agent pazarının 2026 büyüklüğü nedir?
  • Hangi sektörler AI agent'ları en çok benimsiyor?
  • Öne çıkan AI agent platformları hangileri?
  • 2026'da AI agent alanındaki temel riskler neler?

--- RAPOR ---
[... otomatik üretilen, kaynaklı Markdown rapor ...]

Rapor kaydedildi: reports/20260705_143022_report.md
```

## Bilinen Sınırlamalar (Sprint 2'de ele alınacak)
- Şu an yalnızca CLI üzerinden kullanılabiliyor (web arayüzü yok)
- Tek seferde tek konu araştırılabiliyor (batch mod yok)
- Rapor uzunluğu şu an sabit bir token limitiyle sınırlı

## Ekran Görüntüsü Notu
> Gerçek terminal çıktısının ekran görüntüsünü çekip bu dosyaya (veya
> `docs/sprint1/screenshots/` klasörüne) eklemeyi unutmayın —
> değerlendirme sürecinde görsel kanıt önemlidir.
