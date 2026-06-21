# Sprint 1 — Backlog Dağıtma Mantığı

**Sprint Süresi:** 19 Haziran 2026 – 5 Temmuz 2026
**Sprint Hedefi:** Çalışan bir MVP (Minimum Viable Product) — temel
3 agent akışı (Planner → Research → Writer) + hafıza katmanının uçtan
uca çalışır hale getirilmesi.

## Backlog Dağıtım Mantığı
Solo geliştirme sürecinde backlog, gerçek bir Scrum ekibindeki gibi
**bağımlılık sırasına göre** önceliklendirildi: önce mimari temel,
sonra her agent tek tek, en son entegrasyon ve test.

Story point tahmini Fibonacci serisine göre yapılmıştır (1, 2, 3, 5, 8).
Sprint 1 için toplam kapasite: **21 puan** (2 hafta, solo geliştirme).

## Sprint 1 User Story'leri

| ID | User Story | Story Point | Durum |
|---|---|---|---|
| US-01 | Proje iskeleti ve config yönetimi kurulumu | 2 | ✅ Tamamlandı |
| US-02 | Planner Agent: konuyu alt sorulara bölme | 3 | ✅ Tamamlandı |
| US-03 | Research Agent: web_search tool entegrasyonu | 5 | ✅ Tamamlandı |
| US-04 | Writer Agent: bulguları rapora dönüştürme | 3 | ✅ Tamamlandı |
| US-05 | Hafıza katmanı: ChromaDB entegrasyonu | 5 | ✅ Tamamlandı |
| US-06 | Orchestrator: agent'ları birbirine bağlama | 3 | ✅ Tamamlandı |
| US-07 | CLI arayüzü (rich ile) | 2 | ✅ Tamamlandı |
| US-08 | Birim testleri (planner + hafıza) | 3 | ✅ Tamamlandı |
| US-09 | README ve dokümantasyon | 2 | ✅ Tamamlandı |

**Toplam tamamlanan:** 28 / 21 puan (kapasitenin üzerinde — solo
geliştiricinin yoğun çalışmasıyla mümkün oldu, Sprint 2'de daha
gerçekçi bir hedef belirlenecek).

## Sprint 2'ye Aktarılan (Backlog'da Bekleyen)
| ID | User Story | Tahmini Puan |
|---|---|---|
| US-10 | Streamlit tabanlı basit web arayüzü | 5 |
| US-11 | Rapor kalitesi için kullanıcı geri bildirim döngüsü | 3 |
| US-12 | Çoklu dil desteği (EN/TR) | 3 |
