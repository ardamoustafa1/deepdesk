"""
test_memory.py
---------------
ResearchMemory sınıfı için birim testleri.
API anahtarı gerektirmez — sadece hafıza (ChromaDB) katmanını test eder.
"""

import shutil
import tempfile
import pytest

from src.memory.vector_store import ResearchMemory


@pytest.fixture
def temp_memory():
    tmp_dir = tempfile.mkdtemp()
    memory = ResearchMemory(persist_dir=tmp_dir)
    yield memory
    shutil.rmtree(tmp_dir, ignore_errors=True)


def test_empty_memory_returns_no_related(temp_memory):
    assert temp_memory.find_related("herhangi bir konu") == []


def test_save_and_retrieve(temp_memory):
    temp_memory.save(
        topic="elektrikli araç pazarı",
        report="Elektrikli araç pazarı 2026'da büyümeye devam ediyor.",
    )
    results = temp_memory.find_related("elektrikli araçlar")
    assert len(results) == 1
    assert "elektrikli araç" in results[0].lower()


def test_multiple_saves_increase_count(temp_memory):
    temp_memory.save("konu 1", "rapor 1")
    temp_memory.save("konu 2", "rapor 2")
    assert temp_memory.collection.count() == 2
