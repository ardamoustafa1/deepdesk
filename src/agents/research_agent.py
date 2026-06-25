"""
research_agent.py
------------------
RESEARCH AGENT

Görevi: Planner Agent'tan gelen her bir alt soruyu, Anthropic API'nin
web_search tool'unu kullanarak araştırmak ve kaynaklı (citation'lı) kısa
bir bulgu özeti çıkarmak.

Çok-ajanlı mimaride ikinci halka:
Alt Sorular -> [Research Agent + web_search tool] -> Kaynaklı Bulgular
"""

from dataclasses import dataclass
from anthropic import Anthropic


RESEARCH_SYSTEM_PROMPT = """Sen bir araştırma asistanısın. Sana verilen
soruyu web'de araştır ve bulgularını 3-5 cümlelik, öz ve kaynak temelli
bir şekilde özetle. Spekülasyon yapma; yalnızca bulduğun bilgilere
dayanarak yaz."""


@dataclass
class ResearchFinding:
    question: str
    summary: str
    sources: list[str]


class ResearchAgent:
    def __init__(self, client: Anthropic, model_name: str):
        self.client = client
        self.model_name = model_name

    def research(self, question: str) -> ResearchFinding:
        """Tek bir alt soruyu web_search tool'u ile araştırır."""
        response = self.client.messages.create(
            model=self.model_name,
            max_tokens=1000,
            system=RESEARCH_SYSTEM_PROMPT,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=[{"role": "user", "content": question}],
        )

        summary_parts = []
        sources = []

        for block in response.content:
            if block.type == "text":
