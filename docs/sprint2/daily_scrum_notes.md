# Sprint 2 — Daily Scrum Notları

> Solo geliştirme sürecinde daily scrum, kendi kendine ilerleme takibi
> ve engel (blocker) tespiti amacıyla günlük olarak yazılı tutulmuştur.

---

### 📅 6 Temmuz 2026
- **Bugün:** Sprint 2 planlaması yapıldı; US-10, US-11, US-12 seçildi.
  Sprint 1 retrospektifindeki "gerçekçi kapasite" kararına uyularak
  kapsam bilinçli şekilde dar tutuldu.
- **Engel:** Yok.

### 📅 8 Temmuz 2026
- **Bugün:** Planner, Research ve Writer agent'larına `language`
  parametresi eklendi; TR/EN sistem promptları yazıldı (US-12).
- **Engel:** Research Agent'ın "sonuç bulunamadı" mesajının da dil
  bağımlı olması gerektiği fark edildi, ek olarak düzeltildi.

### 📅 10 Temmuz 2026
- **Bugün:** `FeedbackStore` (JSON tabanlı puan + yorum deposu)
  geliştirildi; Orchestrator, benzer konulardaki geçmiş geri
  bildirimleri Writer Agent'a bağlam olarak geçecek şekilde güncellendi
  (US-11).
- **Engel:** Geri bildirimleri "benzer konu" olarak eşleştirmek için
  önce ChromaDB kullanmayı düşündüm; basit kelime kesişimi yeterli ve
  daha az bağımlılık gerektirdiği için ondan vazgeçildi.

### 📅 12 Temmuz 2026
- **Bugün:** `web_app.py` (Streamlit arayüzü) geliştirildi: konu girişi,
  dil seçici, alt sorular/rapor gösterimi, rapor indirme, geçmiş
  raporlar paneli ve geri bildirim formu (US-10).
- **Engel:** Yok.

### 📅 14 Temmuz 2026
- **Bugün:** CLI (`main.py`) `--lang` bayrağı ve rapor sonrası
  interaktif geri bildirim akışıyla güncellendi. Yeni birim testleri
  eklendi (`test_feedback_store.py`, `test_writer_agent.py`, planner
  dil testleri).
- **Engel:** Yok.

### 📅 16 Temmuz 2026 (Bugün)
- **Bugün:** Tüm test paketi (19 test) çalıştırıldı ve geçti. Web
  arayüzü tarayıcıda manuel olarak test edildi: boş konu uyarısı, API
  anahtarı eksik hatası ve TR/EN dil geçişi doğrulandı. Sprint 2
  dokümantasyonu ve README güncellemesi tamamlanıyor.
- **Engel:** Yok.

### 📅 17-19 Temmuz 2026 (Planlanan)
- **Plan:** Gerçek API key ile canlı uçtan uca test (web + CLI),
  GitHub Projects board'un Sprint 2 kolonlarıyla güncellenmesi, ekran
  görüntülerinin alınması ve Sprint 2 teslimi.
