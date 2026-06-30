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

