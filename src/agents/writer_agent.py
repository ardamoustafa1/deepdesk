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
