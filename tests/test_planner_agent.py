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
