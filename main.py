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
from src.utils.config import load_settings

console = Console()


def main() -> None:
    if len(sys.argv) < 2:
        console.print("[bold red]Kullanım:[/] python main.py \"araştırma konusu\"")
        sys.exit(1)

    topic = " ".join(sys.argv[1:])
    console.print(Panel(f"[bold cyan]DeepDesk Araştırma Asistanı[/]\nKonu: {topic}"))

    settings = load_settings()
    orchestrator = DeepDeskOrchestrator(settings)

    with Progress(
        SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console
    ) as progress:
        task = progress.add_task("Planlanıyor, araştırılıyor ve yazılıyor...", total=None)
        result = orchestrator.run(topic)
        progress.update(task, completed=True)

    console.print("\n[bold green]Alt Sorular:[/]")
    for q in result.sub_questions:
        console.print(f"  • {q}")

    if result.used_memory:
        console.print("\n[bold yellow]Not:[/] Geçmiş araştırmalarınızdan yararlanıldı.")

    console.print("\n[bold cyan]--- RAPOR ---[/]\n")
    console.print(result.report)

    # Raporu dosyaya kaydet
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    filename = reports_dir / f"{datetime.now():%Y%m%d_%H%M%S}_report.md"
    filename.write_text(result.report, encoding="utf-8")
    console.print(f"\n[bold green]Rapor kaydedildi:[/] {filename}")


if __name__ == "__main__":
    main()
