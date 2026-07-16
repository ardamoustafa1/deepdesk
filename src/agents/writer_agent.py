"""
writer_agent.py
----------------
WRITER AGENT

Görevi: Research Agent'ın topladığı, kaynaklı bulguları alıp; tutarlı,
akıcı ve okunabilir bir Markdown rapor haline getirmek.

Çok-ajanlı mimaride üçüncü ve son halka:
Kaynaklı Bulgular -> [Writer Agent] -> Nihai Rapor (Markdown)
"""

from groq import Groq
from src.agents.research_agent import ResearchFinding


WRITER_SYSTEM_PROMPT_TR = """Sen deneyimli bir araştırma editörüsün. Sana
verilen, farklı alt sorulara ait bulguları birleştirip; giriş, ana
bölümler ve sonuç içeren, iyi yapılandırılmış bir Markdown raporu
oluştur. Rapor profesyonel bir tonda, akıcı ve tekrarsız olmalı.
Kaynakları raporun sonunda 'Kaynaklar' başlığı altında listele."""

WRITER_SYSTEM_PROMPT_EN = """You are an experienced research editor. Combine
the findings you are given, belonging to different sub-questions, into a
well-structured Markdown report with an introduction, main sections, and a
conclusion. The report must be professional in tone, fluent, and free of
repetition. List the sources at the end of the report under a 'Sources'
heading."""

WRITER_PROMPTS = {"tr": WRITER_SYSTEM_PROMPT_TR, "en": WRITER_SYSTEM_PROMPT_EN}


class WriterAgent:
    def __init__(self, client: Groq, model_name: str):
        self.client = client
        self.model_name = model_name

    def write_report(
        self,
        topic: str,
        findings: list[ResearchFinding],
        language: str = "tr",
        feedback_notes: list | None = None,
    ) -> str:
        sources_label = "Sources" if language == "en" else "Kaynaklar"
        none_label = "none" if language == "en" else "yok"
        subq_label = "Sub-question" if language == "en" else "Alt Soru"
        findings_text = "\n\n".join(
            f"### {subq_label}: {f.question}\n{f.summary}\n{sources_label}: {', '.join(f.sources) or none_label}"
            for f in findings
        )

        feedback_context = ""
        comments = [fb.comment for fb in (feedback_notes or []) if getattr(fb, "comment", "")]
        if comments:
            header = (
                "Past user feedback on similar topics — address these points:"
                if language == "en"
                else "Benzer konularda geçmiş kullanıcı geri bildirimleri (bu noktaları dikkate al):"
            )
            feedback_context = "\n\n" + header + "\n" + "\n".join(f"- {c}" for c in comments)

        system_prompt = WRITER_PROMPTS.get(language, WRITER_SYSTEM_PROMPT_TR)

        if language == "en":
            user_content = (
                f"Main research topic: {topic}\n\n"
                f"Collected findings:\n{findings_text}{feedback_context}\n\n"
                "Based on these findings, write the final report."
            )
        else:
            user_content = (
                f"Ana araştırma konusu: {topic}\n\n"
                f"Toplanan bulgular:\n{findings_text}{feedback_context}\n\n"
                "Bu bulgulara dayanarak nihai raporu yaz."
            )

        response = self.client.chat.completions.create(
            model=self.model_name,
            max_tokens=2000,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            temperature=0.5,
        )

        return response.choices[0].message.content or ""
