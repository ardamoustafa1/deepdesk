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
