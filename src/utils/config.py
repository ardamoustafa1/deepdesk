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
    anthropic_api_key: str
    model_name: str
    chroma_persist_dir: str
    max_subquestions: int


def load_settings() -> Settings:
    api_key = os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise EnvironmentError(
            "ANTHROPIC_API_KEY bulunamadı. Lütfen .env dosyanızı "
            "(.env.example dosyasından kopyalayarak) oluşturun ve "
            "kendi API anahtarınızı ekleyin."
        )

    return Settings(
        anthropic_api_key=api_key,
        # Not: Model adları zamanla güncellenebilir.
        # Güncel liste için: https://docs.claude.com/en/docs/about-claude/models
        model_name=os.getenv("DEEPDESK_MODEL", "claude-sonnet-5"),
        chroma_persist_dir=os.getenv("DEEPDESK_MEMORY_DIR", ".chroma_memory"),
        max_subquestions=int(os.getenv("DEEPDESK_MAX_SUBQUESTIONS", "4")),
    )
