"""
orchestrator.py
----------------
ORCHESTRATOR

Görevi: Planner, Research ve Writer agent'larını doğru sırayla çalıştırıp
aralarındaki veri akışını yönetmek. Ayrıca hafıza (memory) katmanıyla
konuşarak geçmiş araştırmalardan faydalanmayı ve yeni araştırmayı
kaydetmeyi sağlar.

Akış:
1. Hafızada ilgili geçmiş araştırma var mı diye bak.
2. Planner Agent -> konuyu alt sorulara böl.
3. Research Agent -> her alt soruyu web'de araştır.
4. Writer Agent -> bulguları nihai rapora dönüştür.
5. Raporu hafızaya kaydet.
"""

from dataclasses import dataclass
from anthropic import Anthropic

from src.agents.planner_agent import PlannerAgent
from src.agents.research_agent import ResearchAgent, ResearchFinding
from src.agents.writer_agent import WriterAgent
from src.memory.vector_store import ResearchMemory
from src.utils.config import Settings


@dataclass
class ResearchResult:
    topic: str
    sub_questions: list[str]
    findings: list[ResearchFinding]
    report: str
    used_memory: bool

