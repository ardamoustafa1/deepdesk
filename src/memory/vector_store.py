"""
vector_store.py
----------------
HAFIZA (MEMORY) KATMANI

Görevi: DeepDesk'in daha önce yaptığı araştırmaları kalıcı olarak
saklamak ve yeni bir araştırma başladığında ilgili geçmiş bulguları
geri getirmek (retrieval).

Bu, agent sistemine "hafıza" kazandıran katmandır — bootcamp
değerlendirme kriterlerinde özellikle aranan bir özellik.

ChromaDB, metinleri otomatik olarak embedding'e çevirip diskte kalıcı
şekilde saklayan hafif bir vektör veritabanıdır.
"""

import chromadb
from chromadb.config import Settings as ChromaSettings


class ResearchMemory:
    def __init__(self, persist_dir: str):
        self.client = chromadb.PersistentClient(
            path=persist_dir,
            settings=ChromaSettings(anonymized_telemetry=False),
        )
        self.collection = self.client.get_or_create_collection(
            name="research_history"
        )

    def save(self, topic: str, report: str) -> None:
        """Tamamlanan bir araştırmayı hafızaya kaydeder."""
        existing_count = self.collection.count()
        self.collection.add(
            documents=[report],
            metadatas=[{"topic": topic}],
            ids=[f"research-{existing_count + 1}"],
        )

    def find_related(self, topic: str, n_results: int = 2) -> list[str]:
        """Yeni konuyla ilgili geçmiş araştırmaları getirir.

        Koleksiyon boşsa (ilk çalıştırma) boş liste döner.
        """
        if self.collection.count() == 0:
            return []

        results = self.collection.query(
            query_texts=[topic],
            n_results=min(n_results, self.collection.count()),
        )
        documents = results.get("documents", [[]])
        return documents[0] if documents else []
