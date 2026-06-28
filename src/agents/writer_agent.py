"""
writer_agent.py
----------------
WRITER AGENT

Görevi: Research Agent'ın topladığı, kaynaklı bulguları alıp; tutarlı,
akıcı ve okunabilir bir Markdown rapor haline getirmek.

Çok-ajanlı mimaride üçüncü ve son halka:
Kaynaklı Bulgular -> [Writer Agent] -> Nihai Rapor (Markdown)
"""

from anthropic import Anthropic
from src.agents.research_agent import ResearchFinding


WRITER_SYSTEM_PROMPT = """Sen deneyimli bir araştırma editörüsün. Sana
verilen, farklı alt sorulara ait bulguları birleştirip; giriş, ana
bölümler ve sonuç içeren, iyi yapılandırılmış bir Markdown raporu
oluştur. Rapor profesyonel bir tonda, akıcı ve tekrarsız olmalı.
Kaynakları raporun sonunda 'Kaynaklar' başlığı altında listele."""


class WriterAgent:
    def __init__(self, client: Anthropic, model_name: str):
        self.client = client
        self.model_name = model_name

    def write_report(self, topic: str, findings: list[ResearchFinding]) -> str:
        findings_text = "\n\n".join(
            f"### Alt Soru: {f.question}\n{f.summary}\nKaynaklar: {', '.join(f.sources) or 'yok'}"
            for f in findings
        )

        response = self.client.messages.create(
            model=self.model_name,
            max_tokens=2000,
            system=WRITER_SYSTEM_PROMPT,
