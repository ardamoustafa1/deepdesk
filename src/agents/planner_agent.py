"""
planner_agent.py
-----------------
PLANNER AGENT

Görevi: Kullanıcının verdiği geniş araştırma konusunu, Research Agent'ın
tek tek araştırabileceği, odaklanmış alt sorulara böler.

Bu, çok-ajanlı (multi-agent) mimarinin ilk halkasıdır:
Kullanıcı Sorusu -> [Planner Agent] -> Alt Sorular -> [Research Agent]
"""

import json
from groq import Groq


PLANNER_SYSTEM_PROMPT_TR = """Sen bir araştırma planlama uzmanısın. Görevin,
kullanıcının verdiği araştırma konusunu, birbirini tamamlayan, odaklanmış
alt sorulara bölmek.

Kurallar:
- En fazla {max_questions} alt soru üret.
- Her alt soru bağımsız olarak web'de araştırılabilir olmalı.
- Alt sorular birbiriyle örtüşmemeli, konunun farklı yönlerini kapsamalı.
- SADECE aşağıdaki JSON formatında yanıt ver, başka hiçbir açıklama ekleme:

{{"sub_questions": ["soru 1", "soru 2", "..."]}}
"""

PLANNER_SYSTEM_PROMPT_EN = """You are a research planning expert. Your task is
to break down the research topic given by the user into complementary,
focused sub-questions.

Rules:
- Generate at most {max_questions} sub-questions.
- Each sub-question must be independently researchable on the web.
- Sub-questions must not overlap; together they should cover different
  aspects of the topic.
- Respond ONLY in the following JSON format, with no other explanation:

{{"sub_questions": ["question 1", "question 2", "..."]}}
"""

PLANNER_PROMPTS = {"tr": PLANNER_SYSTEM_PROMPT_TR, "en": PLANNER_SYSTEM_PROMPT_EN}


class PlannerAgent:
    def __init__(self, client: Groq, model_name: str, max_questions: int = 4):
        self.client = client
        self.model_name = model_name
        self.max_questions = max_questions

    def plan(self, topic: str, language: str = "tr") -> list[str]:
        """Verilen konuyu alt sorulara böler ve liste olarak döner."""
        system_prompt = PLANNER_PROMPTS.get(language, PLANNER_SYSTEM_PROMPT_TR)
        user_prompt = f"Research topic: {topic}" if language == "en" else f"Araştırma konusu: {topic}"

        response = self.client.chat.completions.create(
            model=self.model_name,
            max_tokens=500,
            messages=[
                {"role": "system", "content": system_prompt.format(max_questions=self.max_questions)},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
            response_format={"type": "json_object"},
        )

        raw_text = response.choices[0].message.content or ""

        try:
            # Model bazen JSON'u ```json bloğu içine koyabilir, temizleyelim
            cleaned = raw_text.strip().removeprefix("```json").removesuffix("```").strip()
            parsed = json.loads(cleaned)
            return parsed["sub_questions"][: self.max_questions]
        except (json.JSONDecodeError, KeyError) as exc:
            raise ValueError(
                f"Planner Agent geçerli JSON döndürmedi: {raw_text}"
            ) from exc
