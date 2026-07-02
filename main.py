"""
main.py
-------
DeepDesk CLI giriş noktası.

Kullanım:
    python main.py "elektrikli araç pazarı 2026 trendleri"

Rapor otomatik olarak reports/ klasörüne Markdown dosyası olarak kaydedilir.
"""

import sys
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from src.orchestrator import DeepDeskOrchestrator
