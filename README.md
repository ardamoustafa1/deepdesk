# DeepDesk 🔍

> AI Agent tabanlı, hafızaya sahip otonom araştırma asistanı

## Takım İsmi
Solo — Bootcamp bursiyeri tarafından tek başına yürütülmektedir
*(Akademi ekibine bildirilmiştir — bkz. #bootcamp-2026 Slack kanalı)*

## Takım Rolleri
| İsim | Rol |
|---|---|
| [Adınız] | Product Owner |
| [Adınız] | Scrum Master |
| [Adınız] | Developer |

*Not: Solo geliştirme sürecinde tüm roller aynı kişi tarafından üstlenilmektedir.*

## Ürün İsmi
**DeepDesk** — Otonom Araştırma Asistanı

## Ürün Açıklaması
DeepDesk, kullanıcının verdiği herhangi bir araştırma konusunu otonom
olarak ele alan, çok-ajanlı (multi-agent) bir yapay zeka sistemidir.
Kullanıcı bir konu girdiğinde:

1. **Planner Agent** konuyu odaklanmış alt sorulara böler,
2. **Research Agent** her alt soruyu web'de araştırıp kaynaklı bulgular
   toplar,
3. **Writer Agent** bulguları tutarlı, profesyonel bir Markdown rapora
   dönüştürür,
4. **Hafıza (Memory) katmanı** her araştırmayı kalıcı olarak saklar ve
   yeni bir araştırma geldiğinde geçmiş ilgili çalışmalardan faydalanır.

Böylece kullanıcı, saatler sürebilecek bir araştırma sürecini dakikalar
içinde, güvenilir kaynaklara dayanan bir raporla tamamlar.

## Ürün Özellikleri
- 🤖 **Çok-ajanlı orkestrasyon**: Planner → Researcher → Writer akışı
- 🧠 **Kalıcı hafıza**: ChromaDB ile geçmiş araştırmalar saklanır ve geri çağrılır
- 🔎 **Gerçek zamanlı web araştırması**: Anthropic web_search tool entegrasyonu
- 📄 **Otomatik raporlama**: Her araştırma Markdown dosyası olarak kaydedilir
- 🎨 **Zengin terminal arayüzü**: `rich` kütüphanesi ile okunabilir çıktı
- ✅ **Test edilmiş kod**: Birim testleriyle doğrulanmış planner ve hafıza mantığı

## Hedef Kitle
- Öğrenciler (ödev/tez ön araştırması)
- Girişimciler (pazar/rakip araştırması)
- Analistler ve içerik üreticileri (hızlı ön bilgi toplama)
- 18-45 yaş arası, bilgiye hızlı ve güvenilir şekilde ulaşmak isteyen herkes

## Product Backlog
Sprint backlog ve görev dağılımı için bkz. [`docs/sprint1/backlog.md`](docs/sprint1/backlog.md)

---

## 🚀 Kurulum

```bash
# 1. Repoyu klonlayın
git clone <repo-url>
cd deepdesk

# 2. Sanal ortam oluşturun (önerilir)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Bağımlılıkları kurun
pip install -r requirements.txt

# 4. Ortam değişkenlerini ayarlayın
cp .env.example .env
# .env dosyasını açıp ANTHROPIC_API_KEY değerinizi girin
```

## ▶️ Kullanım

```bash
python main.py "elektrikli araç pazarı 2026 trendleri"
```

Rapor hem terminalde gösterilir hem de `reports/` klasörüne
`.md` dosyası olarak kaydedilir.

## 🧪 Testleri Çalıştırma

```bash
pytest tests/ -v
```

> Not: İlk çalıştırmada ChromaDB, embedding modeli için küçük bir dosya
> (~90MB) indirir; bu yüzden ilk test çalıştırması internet bağlantısı
> gerektirir ve birkaç saniye sürebilir.

## 📁 Proje Yapısı

```
deepdesk/
├── main.py                    # CLI giriş noktası
├── src/
│   ├── orchestrator.py        # Agent'ları koordine eden ana mantık
│   ├── agents/
│   │   ├── planner_agent.py   # Konuyu alt sorulara böler
│   │   ├── research_agent.py  # Web'de araştırma yapar
│   │   └── writer_agent.py    # Nihai raporu yazar
│   ├── memory/
│   │   └── vector_store.py    # Kalıcı hafıza (ChromaDB)
│   └── utils/
│       └── config.py          # Ortam değişkeni yönetimi
├── tests/                     # Birim testleri
├── docs/sprint1/               # Sprint 1 dokümantasyonu
└── reports/                    # Oluşturulan raporlar
```

## 🗺️ Yol Haritası (Sonraki Sprintler)
- [ ] Sprint 2: Basit bir web arayüzü (Streamlit/FastAPI)
- [ ] Sprint 2: Çoklu dil desteği
- [ ] Sprint 3: PDF export özelliği
- [ ] Sprint 3: Kullanıcı geri bildirimiyle rapor kalitesini iyileştirme döngüsü

## ⚠️ Diskalifiye Politikasına Uygunluk Notu
Bu proje sıfırdan, bootcamp bursiyeri tarafından geliştirilmiştir. Kod
yazım sürecinde AI destekli geliştirme araçları (Claude) bir **geliştirme
ortağı** olarak kullanılmış olup, bu kullanım bootcamp değerlendirme
kriterlerinde ayrıca puanlanan "Yapay Zeka Modeli seçimi, kullanımı,
geliştirmesi" maddesiyle uyumludur. Hazır/satın alınmış bir proje
kullanılmamıştır.
