"""
web_app.py
-----------
DeepDesk Streamlit web arayüzü (Sprint 2 — US-10).

CLI'daki (main.py) aynı DeepDeskOrchestrator akışını tarayıcı üzerinden
kullanılabilir hale getirir: konu girişi, dil seçimi, alt sorular ve
rapor gösterimi, rapor indirme ve rapor için geri bildirim (US-11).

Çalıştırma:
    streamlit run web_app.py
"""

from pathlib import Path

import streamlit as st

from src.orchestrator import DeepDeskOrchestrator
from src.utils.config import load_settings

st.set_page_config(page_title="DeepDesk", page_icon="🔎", layout="centered")

LABELS = {
    "tr": {
        "language_name": "Türkçe",
        "title": "DeepDesk Araştırma Asistanı",
        "subtitle": "Bir konu girin; çok ajanlı akış sizin için araştırıp raporlasın.",
        "topic_label": "Araştırma konusu",
        "topic_placeholder": "örn. yapay zeka ajanlarının 2026 pazar trendleri",
        "run_button": "Araştırmayı Başlat",
        "spinner": "Planlanıyor, araştırılıyor ve yazılıyor...",
        "sub_questions_header": "Alt Sorular",
        "memory_note": "Bu rapor, geçmiş araştırmalarınızdan da faydalanılarak hazırlandı.",
        "report_header": "Rapor",
        "download_button": "Raporu İndir (.md)",
        "feedback_header": "Bu raporu değerlendirin",
        "rating_label": "Puan (1-5)",
        "comment_label": "Yorumunuz (opsiyonel)",
        "feedback_button": "Geri Bildirimi Gönder",
        "feedback_saved": "Geri bildiriminiz için teşekkürler!",
        "empty_topic_warning": "Lütfen bir araştırma konusu girin.",
        "history_header": "Geçmiş Raporlar",
        "history_empty": "Henüz kaydedilmiş bir rapor yok.",
        "config_error_hint": "Lütfen .env dosyanızı .env.example'dan kopyalayıp GROQ_API_KEY girin.",
    },
    "en": {
        "language_name": "English",
        "title": "DeepDesk Research Assistant",
        "subtitle": "Enter a topic and let the multi-agent flow research and report it for you.",
        "topic_label": "Research topic",
        "topic_placeholder": "e.g. 2026 market trends for AI agents",
        "run_button": "Start Research",
        "spinner": "Planning, researching, and writing...",
        "sub_questions_header": "Sub-Questions",
        "memory_note": "This report also draws on your past research.",
        "report_header": "Report",
        "download_button": "Download Report (.md)",
        "feedback_header": "Rate this report",
        "rating_label": "Rating (1-5)",
        "comment_label": "Your comment (optional)",
        "feedback_button": "Submit Feedback",
        "feedback_saved": "Thanks for your feedback!",
        "empty_topic_warning": "Please enter a research topic.",
        "history_header": "Past Reports",
        "history_empty": "No reports saved yet.",
        "config_error_hint": "Please copy .env.example to .env and set GROQ_API_KEY.",
    },
}


@st.cache_resource
def get_orchestrator() -> DeepDeskOrchestrator:
    settings = load_settings()
    return DeepDeskOrchestrator(settings)


def render_history(t: dict) -> None:
    reports_dir = Path("reports")
    report_files = sorted(reports_dir.glob("*_report.md"), reverse=True) if reports_dir.exists() else []

    with st.expander(f"{t['history_header']} ({len(report_files)})"):
        if not report_files:
            st.caption(t["history_empty"])
            return
        for report_file in report_files[:10]:
            st.markdown(f"**{report_file.name}**")
            st.text(report_file.read_text(encoding="utf-8")[:300] + "...")
            st.divider()


def main() -> None:
    default_language = "tr"
    try:
        default_language = load_settings().default_language
    except EnvironmentError:
        pass
    if default_language not in LABELS:
        default_language = "tr"

    language = st.sidebar.selectbox(
        "Dil / Language",
        options=list(LABELS.keys()),
        index=list(LABELS.keys()).index(default_language),
        format_func=lambda code: LABELS[code]["language_name"],
    )
    t = LABELS[language]

    st.title(t["title"])
    st.caption(t["subtitle"])

    with st.form(key="research_form"):
        topic = st.text_input(t["topic_label"], placeholder=t["topic_placeholder"])
        run_clicked = st.form_submit_button(t["run_button"], type="primary")

    if run_clicked:
        if not topic.strip():
            st.warning(t["empty_topic_warning"])
        else:
            try:
                orchestrator = get_orchestrator()
            except EnvironmentError as exc:
                st.error(str(exc))
                st.caption(t["config_error_hint"])
            else:
                with st.spinner(t["spinner"]):
                    result = orchestrator.run(topic, language=language)
                st.session_state["last_result"] = result

    result = st.session_state.get("last_result")
    if result:
        result_labels = LABELS[result.language]

        st.subheader(result_labels["sub_questions_header"])
        for question in result.sub_questions:
            st.markdown(f"- {question}")

        if result.used_memory:
            st.info(result_labels["memory_note"])

        st.subheader(result_labels["report_header"])
        st.markdown(result.report)

        st.download_button(
            result_labels["download_button"],
            data=result.report,
            file_name="deepdesk_report.md",
            mime="text/markdown",
        )

        st.divider()
        st.subheader(result_labels["feedback_header"])
        with st.form(key="feedback_form"):
            rating = st.slider(result_labels["rating_label"], min_value=1, max_value=5, value=4)
            comment = st.text_area(result_labels["comment_label"])
            feedback_clicked = st.form_submit_button(result_labels["feedback_button"])

        if feedback_clicked:
            orchestrator = get_orchestrator()
            orchestrator.feedback_store.add(result.topic, rating, comment)
            st.success(result_labels["feedback_saved"])

    st.divider()
    render_history(t)


if __name__ == "__main__":
    main()
