"""
feedback_store.py
------------------
GERİ BİLDİRİM (FEEDBACK) KATMANI

Görevi: Kullanıcıların ürettiği raporlara verdiği puanı (1-5) ve
yorumları JSON tabanlı basit bir depoda kalıcı olarak saklamak.

Bu geri bildirimler yeni bir rapor üretilirken Writer Agent'a bağlam
olarak verilir; böylece benzer konularda daha önce dile getirilen
eksiklikler bir sonraki raporda dikkate alınır (US-11 — rapor kalitesi
için kullanıcı geri bildirim döngüsü).
"""

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Feedback:
    topic: str
    rating: int
    comment: str
    created_at: str


class FeedbackStore:
    def __init__(self, path: str = "reports/feedback.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def add(self, topic: str, rating: int, comment: str = "") -> Feedback:
        """Yeni bir geri bildirimi doğrulayıp depoya ekler."""
        if not 1 <= rating <= 5:
            raise ValueError("Puan 1 ile 5 arasında olmalıdır.")

        feedback = Feedback(
            topic=topic,
            rating=rating,
            comment=comment.strip(),
            created_at=datetime.now().isoformat(timespec="seconds"),
        )
        entries = self._load_raw()
        entries.append(asdict(feedback))
        self.path.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
        return feedback

    def related(self, topic: str) -> list[Feedback]:
        """Konuyla ortak kelime geçen geçmiş geri bildirimleri döner.

        Basit bir kelime kesişimi kullanır; ChromaDB gibi bir vektör
        veritabanı gerektirmeden, konu benzerliğine dayalı yeterli bir
        eşleşme sağlar.
        """
        topic_words = _significant_words(topic)
        if not topic_words:
            return []

        matches = []
        for entry in self._load_raw():
            entry_words = _significant_words(entry["topic"])
            if topic_words & entry_words:
                matches.append(Feedback(**entry))
        return matches

    def average_rating(self) -> float | None:
        """Tüm geri bildirimlerin ortalama puanını döner (kayıt yoksa None)."""
        entries = self._load_raw()
        if not entries:
            return None
        return sum(e["rating"] for e in entries) / len(entries)

    def all(self) -> list[Feedback]:
        return [Feedback(**entry) for entry in self._load_raw()]

    def _load_raw(self) -> list[dict]:
        return json.loads(self.path.read_text(encoding="utf-8"))


def _significant_words(text: str) -> set[str]:
    return {w.lower() for w in text.split() if len(w) > 2}
