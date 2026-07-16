"""
main.py
-------
DeepDesk CLI giriş noktası.

Kullanım:
    python main.py "elektrikli araç pazarı 2026 trendleri"
    python main.py "2026 market trends for electric vehicles" --lang en

Rapor otomatik olarak reports/ klasörüne Markdown dosyası olarak kaydedilir.
Rapor sonunda isteğe bağlı olarak 1-5 arası puan ve yorum bırakılabilir;
bu geri bildirimler benzer konularda gelecekteki raporları iyileştirmek
için kullanılır (US-11).
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

SUPPORTED_LANGUAGES = ("tr", "en")

TEXT = {
    "tr": {
        "usage": 'Kullanım: python main.py "araştırma konusu" [--lang tr|en]',
        "sub_questions": "Alt Sorular:",
        "memory_note": "Not: Geçmiş araştırmalarınızdan yararlanıldı.",
        "report_header": "--- RAPOR ---",
        "saved": "Rapor kaydedildi:",
        "spinner": "Planlanıyor, araştırılıyor ve yazılıyor...",
        "feedback_header": "Geri Bildirim",
        "rating_prompt": "Bu raporu 1-5 arası puanlayın (atlamak için Enter): ",
        "comment_prompt": "Yorumunuz (opsiyonel): ",
        "feedback_saved": "Geri bildiriminiz kaydedildi. Teşekkürler!",
        "invalid_rating": "Geçersiz puan, geri bildirim kaydedilmedi.",
        "unsupported_lang": "Desteklenmeyen dil: {lang}. 'tr' veya 'en' kullanın.",
    },
    "en": {
        "usage": 'Usage: python main.py "research topic" [--lang tr|en]',
        "sub_questions": "Sub-Questions:",
        "memory_note": "Note: Your past research was used.",
        "report_header": "--- REPORT ---",
        "saved": "Report saved:",
        "spinner": "Planning, researching, and writing...",
        "feedback_header": "Feedback",
        "rating_prompt": "Rate this report 1-5 (press Enter to skip): ",
        "comment_prompt": "Your comment (optional): ",
        "feedback_saved": "Thanks, your feedback was saved!",
        "invalid_rating": "Invalid rating, feedback was not saved.",
        "unsupported_lang": "Unsupported language: {lang}. Use 'tr' or 'en'.",
    },
}


def parse_args(argv: list[str]) -> tuple[str, str | None]:
    """Argümanlardan --lang bayrağını ayıklayıp (konu, dil override) döner."""
    args = list(argv)
    language_override = None
    if "--lang" in args:
        idx = args.index("--lang")
        if idx + 1 < len(args):
            language_override = args[idx + 1].lower()
            del args[idx : idx + 2]
        else:
            del args[idx]
    topic = " ".join(args).strip()
    return topic, language_override


def ask_for_feedback(orchestrator: DeepDeskOrchestrator, topic: str, language: str) -> None:
    t = TEXT[language]
    console.print(f"\n[bold cyan]{t['feedback_header']}[/]")
    try:
        rating_input = input(t["rating_prompt"]).strip()
    except (EOFError, KeyboardInterrupt):
        return

    if not rating_input:
        return

    try:
        rating = int(rating_input)
        comment = input(t["comment_prompt"]).strip()
        orchestrator.feedback_store.add(topic, rating, comment)
        console.print(f"[bold green]{t['feedback_saved']}[/]")
    except ValueError:
        console.print(f"[bold red]{t['invalid_rating']}[/]")


def main() -> None:
    if len(sys.argv) < 2:
        console.print(f"[bold red]{TEXT['tr']['usage']}[/]")
        sys.exit(1)

    topic, language_override = parse_args(sys.argv[1:])
    if not topic:
        console.print(f"[bold red]{TEXT['tr']['usage']}[/]")
        sys.exit(1)

    settings = load_settings()
    language = language_override or settings.default_language
    if language not in SUPPORTED_LANGUAGES:
        console.print(f"[bold red]{TEXT['tr']['unsupported_lang'].format(lang=language)}[/]")
        sys.exit(1)

    t = TEXT[language]
    console.print(Panel(f"[bold cyan]DeepDesk Araştırma Asistanı[/]\nKonu: {topic}"))

    orchestrator = DeepDeskOrchestrator(settings)

    with Progress(
        SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console
    ) as progress:
        task = progress.add_task(t["spinner"], total=None)
        result = orchestrator.run(topic, language=language)
        progress.update(task, completed=True)

    console.print(f"\n[bold green]{t['sub_questions']}[/]")
    for q in result.sub_questions:
        console.print(f"  • {q}")

    if result.used_memory:
        console.print(f"\n[bold yellow]{t['memory_note']}[/]")

    console.print(f"\n[bold cyan]{t['report_header']}[/]\n")
    console.print(result.report)

    # Raporu dosyaya kaydet
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    filename = reports_dir / f"{datetime.now():%Y%m%d_%H%M%S}_report.md"
    filename.write_text(result.report, encoding="utf-8")
    console.print(f"\n[bold green]{t['saved']}[/] {filename}")

    ask_for_feedback(orchestrator, topic, language)


if __name__ == "__main__":
    main()
