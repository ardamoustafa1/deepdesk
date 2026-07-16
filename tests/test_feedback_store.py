"""
test_feedback_store.py
------------------------
FeedbackStore sınıfı için birim testleri (US-11 — rapor kalitesi için
kullanıcı geri bildirim döngüsü). API anahtarı gerektirmez.
"""

import shutil
import tempfile
from pathlib import Path

import pytest

from src.memory.feedback_store import FeedbackStore


@pytest.fixture
def temp_store():
    tmp_dir = tempfile.mkdtemp()
    store = FeedbackStore(path=str(Path(tmp_dir) / "feedback.json"))
    yield store
    shutil.rmtree(tmp_dir, ignore_errors=True)


def test_empty_store_has_no_related_feedback(temp_store):
    assert temp_store.related("herhangi bir konu") == []


def test_empty_store_has_no_average_rating(temp_store):
    assert temp_store.average_rating() is None


def test_add_and_retrieve_related_feedback(temp_store):
    temp_store.add("elektrikli araç pazarı", rating=5, comment="Çok faydalı")

    related = temp_store.related("elektrikli araçlar 2026 trendleri")

    assert len(related) == 1
    assert related[0].comment == "Çok faydalı"
    assert related[0].rating == 5


def test_unrelated_topic_returns_no_feedback(temp_store):
    temp_store.add("elektrikli araç pazarı", rating=5, comment="Çok faydalı")

    related = temp_store.related("yapay zeka ajanları")

    assert related == []


def test_add_rejects_out_of_range_rating(temp_store):
    with pytest.raises(ValueError):
        temp_store.add("konu", rating=6)

    with pytest.raises(ValueError):
        temp_store.add("konu", rating=0)


def test_average_rating(temp_store):
    temp_store.add("konu 1", rating=4)
    temp_store.add("konu 2", rating=2)

    assert temp_store.average_rating() == 3.0


def test_all_returns_every_feedback_entry(temp_store):
    temp_store.add("konu 1", rating=4, comment="iyi")
    temp_store.add("konu 2", rating=2, comment="orta")

    assert len(temp_store.all()) == 2
