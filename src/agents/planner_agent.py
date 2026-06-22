"""
planner_agent.py
-----------------
PLANNER AGENT

Görevi: Kullanıcının verdiği geniş araştırma konusunu, Research Agent'ın
tek tek araştırabileceği, odaklanmış alt sorulara böler.

Bu, çok-ajanlı (multi-agent) mimarinin ilk halkasıdır:
Kullanıcı Sorusu -> [Planner Agent] -> Alt Sorular -> [Research Agent]
"""

import json
from anthropic import Anthropic
