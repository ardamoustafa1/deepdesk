"""
config.py
---------
Ortam değişkenlerini (environment variables) yükler ve proje genelinde
kullanılacak ayarları tek bir yerden yönetir.

Neden bu dosya var?
Sabit değerleri (API key, model adı vb.) kod içine gömmek yerine .env
dosyasından okumak, hem güvenlik hem de farklı ortamlarda (geliştirme/
test/production) kolay yapılandırma sağlar.
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

# .env dosyasını yükle (proje kök dizininde olmalı)
load_dotenv()


@dataclass(frozen=True)
class Settings:
    groq_api_key: str
    model_name: str
    chroma_persist_dir: str
    max_subquestions: int


def load_settings() -> Settings:
    api_key = os.getenv("GROQ_API_KEY") or os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise EnvironmentError(
            "GROQ_API_KEY bulunamadı. Lütfen .env dosyanızı "
            "(.env.example dosyasından kopyalayarak) oluşturun ve "
            "kendi API anahtarınızı ekleyin."
        )

    return Settings(
        groq_api_key=api_key,
        # Not: Groq modelleri zamanla güncellenebilir.
        # En güçlü çok yönlü model: llama-3.3-70b-versatile
        model_name=os.getenv("DEEPDESK_MODEL", "llama-3.3-70b-versatile"),
        chroma_persist_dir=os.getenv("DEEPDESK_MEMORY_DIR", ".chroma_memory"),
        max_subquestions=int(os.getenv("DEEPDESK_MAX_SUBQUESTIONS", "4")),
    )
