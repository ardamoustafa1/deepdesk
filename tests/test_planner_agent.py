"""
test_planner_agent.py
----------------------
PlannerAgent'ın JSON ayrıştırma mantığını, gerçek API çağrısı yapmadan
(mock kullanarak) test eder.
"""

from types import SimpleNamespace
from src.agents.planner_agent import PlannerAgent


class FakeMessage:
    def __init__(self, text):
        self.content = text


class FakeChoice:
    def __init__(self, text):
        self.message = FakeMessage(text)


class FakeGroqClient:
    """Groq client'ı taklit eden basit bir sahte (mock) sınıf."""

    def __init__(self, fake_response_text: str):
        self.fake_response_text = fake_response_text
        self.chat = SimpleNamespace(
            completions=SimpleNamespace(create=self._create)
        )

    def _create(self, **kwargs):
        return SimpleNamespace(choices=[FakeChoice(self.fake_response_text)])


def test_plan_parses_valid_json():
    fake_json = '{"sub_questions": ["Soru 1?", "Soru 2?", "Soru 3?"]}'
    client = FakeGroqClient(fake_json)
    agent = PlannerAgent(client, model_name="fake-model", max_questions=4)

    result = agent.plan("test konusu")

    assert result == ["Soru 1?", "Soru 2?", "Soru 3?"]


def test_plan_respects_max_questions_limit():
    fake_json = '{"sub_questions": ["S1", "S2", "S3", "S4", "S5"]}'
    client = FakeGroqClient(fake_json)
    agent = PlannerAgent(client, model_name="fake-model", max_questions=2)

    result = agent.plan("test konusu")

    assert len(result) == 2


def test_plan_strips_markdown_code_fence():
    fake_json = '```json\n{"sub_questions": ["Soru 1?"]}\n```'
    client = FakeGroqClient(fake_json)
    agent = PlannerAgent(client, model_name="fake-model", max_questions=4)

    result = agent.plan("test konusu")

    assert result == ["Soru 1?"]
