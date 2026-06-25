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

