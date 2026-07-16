"""
test_writer_agent.py
----------------------
WriterAgent'ın dil desteğini (US-12) ve geçmiş geri bildirimleri rapor
bağlamına doğru şekilde eklediğini (US-11) test eder. Gerçek API çağrısı
yapmaz — Groq client'ı taklit eder.
"""

from types import SimpleNamespace

from src.agents.research_agent import ResearchFinding
from src.agents.writer_agent import WriterAgent


class FakeMessage:
    def __init__(self, text):
        self.content = text


class FakeChoice:
    def __init__(self, text):
        self.message = FakeMessage(text)


class FakeGroqClient:
    def __init__(self, fake_response_text: str = "rapor içeriği"):
        self.fake_response_text = fake_response_text
        self.last_kwargs = None
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    def _create(self, **kwargs):
        self.last_kwargs = kwargs
        return SimpleNamespace(choices=[FakeChoice(self.fake_response_text)])


class FakeFeedback:
    def __init__(self, comment):
        self.comment = comment


def _sample_findings():
    return [ResearchFinding(question="Soru 1?", summary="Özet 1", sources=["https://ornek.com"])]


def test_write_report_uses_turkish_prompt_by_default():
    client = FakeGroqClient()
    agent = WriterAgent(client, model_name="fake-model")

    agent.write_report("test konusu", _sample_findings())

    system_message = client.last_kwargs["messages"][0]["content"]
    assert "araştırma editörüsün" in system_message


def test_write_report_uses_english_prompt_when_requested():
    client = FakeGroqClient()
    agent = WriterAgent(client, model_name="fake-model")

    agent.write_report("test topic", _sample_findings(), language="en")

    system_message = client.last_kwargs["messages"][0]["content"]
    user_message = client.last_kwargs["messages"][1]["content"]
    assert "research editor" in system_message
    assert "Main research topic: test topic" in user_message


def test_write_report_includes_past_feedback_comments():
    client = FakeGroqClient()
    agent = WriterAgent(client, model_name="fake-model")

    agent.write_report(
        "test konusu",
        _sample_findings(),
        feedback_notes=[FakeFeedback("Kaynaklar daha güncel olmalı")],
    )

    user_message = client.last_kwargs["messages"][1]["content"]
    assert "Kaynaklar daha güncel olmalı" in user_message


def test_write_report_ignores_feedback_without_comment():
    client = FakeGroqClient()
    agent = WriterAgent(client, model_name="fake-model")

    agent.write_report(
        "test konusu",
        _sample_findings(),
        feedback_notes=[FakeFeedback("")],
    )

    user_message = client.last_kwargs["messages"][1]["content"]
    assert "geçmiş kullanıcı geri bildirimleri" not in user_message
