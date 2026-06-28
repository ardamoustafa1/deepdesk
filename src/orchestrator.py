"""
orchestrator.py
----------------
ORCHESTRATOR

Görevi: Planner, Research ve Writer agent'larını doğru sırayla çalıştırıp
aralarındaki veri akışını yönetmek. Ayrıca hafıza (memory) katmanıyla
konuşarak geçmiş araştırmalardan faydalanmayı ve yeni araştırmayı
kaydetmeyi sağlar.

Akış:
1. Hafızada ilgili geçmiş araştırma var mı diye bak.
2. Planner Agent -> konuyu alt sorulara böl.
3. Research Agent -> her alt soruyu web'de araştır.
4. Writer Agent -> bulguları nihai rapora dönüştür.
5. Raporu hafızaya kaydet.
"""

