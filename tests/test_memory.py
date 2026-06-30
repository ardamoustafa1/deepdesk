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


