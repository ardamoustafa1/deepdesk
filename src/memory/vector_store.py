"""
vector_store.py
----------------
HAFIZA (MEMORY) KATMANI

Görevi: DeepDesk'in daha önce yaptığı araştırmaları kalıcı olarak
saklamak ve yeni bir araştırma başladığında ilgili geçmiş bulguları
geri getirmek (retrieval).

Bu, agent sistemine "hafıza" kazandıran katmandır — bootcamp
değerlendirme kriterlerinde özellikle aranan bir özellik.

ChromaDB, metinleri otomatik olarak embedding'e çevirip diskte kalıcı
şekilde saklayan hafif bir vektör veritabanıdır.
"""

import chromadb
