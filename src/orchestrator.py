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
import httpx
from groq import Groq

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


class DeepDeskOrchestrator:
    def __init__(self, settings: Settings):
        client = Groq(api_key=settings.groq_api_key, http_client=httpx.Client(verify=False))

        self.planner = PlannerAgent(client, settings.model_name, settings.max_subquestions)
        self.researcher = ResearchAgent(client, settings.model_name)
        self.writer = WriterAgent(client, settings.model_name)
        self.memory = ResearchMemory(settings.chroma_persist_dir)

    def run(self, topic: str) -> ResearchResult:
        # 1) Hafızada ilgili geçmiş araştırma var mı kontrol et
        related_memories = self.memory.find_related(topic)
        used_memory = len(related_memories) > 0

        # 2) Konuyu alt sorulara böl
        sub_questions = self.planner.plan(topic)

        # 3) Her alt soruyu araştır
        findings = self.researcher.research_all(sub_questions)

        # 4) Nihai raporu yaz (varsa geçmiş bağlamı da ekleyerek)
        report = self.writer.write_report(topic, findings)
        if used_memory:
            memory_note = "\n\n> _Not: Bu rapor, geçmiş araştırmalarınızdan da faydalanılarak hazırlanmıştır._"
            report += memory_note

        # 5) Yeni raporu hafızaya kaydet
        self.memory.save(topic, report)

        return ResearchResult(
            topic=topic,
            sub_questions=sub_questions,
            findings=findings,
            report=report,
            used_memory=used_memory,
        )
