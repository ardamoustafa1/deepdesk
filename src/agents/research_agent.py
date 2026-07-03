"""
research_agent.py
------------------
RESEARCH AGENT

Görevi: Planner Agent'tan gelen her bir alt soruyu, web arama aracıyla
araştırmak ve bulguları Groq Llama modeli ile özetleyip kaynaklı
bir bulgu özeti çıkarmak.
"""

import urllib.parse
from dataclasses import dataclass
from bs4 import BeautifulSoup
from groq import Groq
import httpx


RESEARCH_SYSTEM_PROMPT = """Sen bir araştırma asistanısın. Sana verilen
soruyu ve web'den elde edilen güncel bulguları inceleyerek 3-5 cümlelik,
öz ve doğrudan bilgi veren bir özet çıkar. Spekülasyon yapma; yalnızca
bulduğun bilgilere dayanarak yaz."""


@dataclass
class ResearchFinding:
    question: str
    summary: str
    sources: list[str]


def search_web_ddg(query: str, max_results: int = 3) -> list[dict[str, str]]:
    """DuckDuckGo üzerinden ücretsiz ve anahtarsız web araması yapar."""
    try:
        url = "https://html.duckduckgo.com/html/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        resp = httpx.post(url, data={"q": query}, verify=False, headers=headers, timeout=10.0)
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for result in soup.find_all("div", class_="result")[:max_results]:
            title_tag = result.find("a", class_="result__a")
            snippet_tag = result.find("a", class_="result__snippet")
            url_tag = result.find("a", class_="result__url")
            if title_tag and snippet_tag:
                title = title_tag.text.strip()
                snippet = snippet_tag.text.strip()
                href = url_tag["href"] if url_tag and "href" in url_tag.attrs else (title_tag["href"] if "href" in title_tag.attrs else "")
                if "uddg=" in href:
                    href = urllib.parse.unquote(href.split("uddg=")[1].split("&")[0])
                if href and href not in [r["url"] for r in results]:
                    results.append({"title": title, "snippet": snippet, "url": href})
        return results
    except Exception:
        # Arama hatası olursa boş liste dön
        return []


class ResearchAgent:
    def __init__(self, client: Groq, model_name: str):
        self.client = client
        self.model_name = model_name

    def research(self, question: str) -> ResearchFinding:
        """Tek bir alt soruyu web'de araştırıp özetler."""
        web_results = search_web_ddg(question)
        sources = [r["url"] for r in web_results if r.get("url")]

        context_text = "\n\n".join(
            f"Başlık: {r['title']}\nÖzet: {r['snippet']}\nURL: {r['url']}"
            for r in web_results
        ) if web_results else "Web sonucu bulunamadı. Genel bilgilerinle yanıt ver."

        prompt = f"Araştırma Sorusu: {question}\n\nWeb Arama Bulguları:\n{context_text}\n\nLütfen bu bulgulara dayanarak soruyu özetle."

        response = self.client.chat.completions.create(
            model=self.model_name,
            max_tokens=1000,
            messages=[
                {"role": "system", "content": RESEARCH_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
        )

        summary = response.choices[0].message.content or ""

        return ResearchFinding(
            question=question,
            summary=summary.strip(),
            sources=sources,
        )

    def research_all(self, questions: list[str]) -> list[ResearchFinding]:
        """Birden fazla alt soruyu sırayla araştırır."""
        return [self.research(q) for q in questions]
