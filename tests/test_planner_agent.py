"""
test_planner_agent.py
----------------------
PlannerAgent'ın JSON ayrıştırma mantığını, gerçek API çağrısı yapmadan
(mock kullanarak) test eder.
"""

from types import SimpleNamespace
from src.agents.planner_agent import PlannerAgent


class FakeTextBlock:
    def __init__(self, text):
        self.type = "text"
        self.text = text


class FakeAnthropicClient:
    """Anthropic client'ı taklit eden basit bir sahte (mock) sınıf."""

    def __init__(self, fake_response_text: str):
        self.fake_response_text = fake_response_text
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kwargs):
        return SimpleNamespace(content=[FakeTextBlock(self.fake_response_text)])


def test_plan_parses_valid_json():
    fake_json = '{"sub_questions": ["Soru 1?", "Soru 2?", "Soru 3?"]}'
    client = FakeAnthropicClient(fake_json)
    agent = PlannerAgent(client, model_name="fake-model", max_questions=4)

    result = agent.plan("test konusu")

    assert result == ["Soru 1?", "Soru 2?", "Soru 3?"]
