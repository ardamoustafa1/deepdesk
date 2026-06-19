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
