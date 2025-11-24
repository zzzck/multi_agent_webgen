from core.manager import Manager
import os

os.makedirs("output", exist_ok=True)

brief = """
设计春节电商落地页。
产品：新疆葵花籽 500g，小包装；19.9 元。
主题：春节 × 团圆 × 嗑瓜子 × 年味。
"""

manager = Manager()
html = manager.run(brief)

with open("output/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("网页已生成：output/index.html")
