import json
import os
import random
from jinja2 import Template

# 1. نقرأ بيانات الألعاب
with open("games_data_ready.json", "r", encoding="utf-8") as f:
    games_data = json.load(f)

with open("game_template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

template = Template(template_content)
print("🚀 جاري بناء صفحات الألعاب مع الروابط الداخلية (Internal Links)...")

for game in games_data:
    folder_name = game["link"].replace("./", "").replace("/", "")
    if not folder_name: continue
        
    os.makedirs(folder_name, exist_ok=True)
    
    # ضبط مسار الصورة للعبة الأساسية
    image_path = "../" + game["image"][2:] if game["image"].startswith("./") else "../" + game["image"]
    
    # ---------------------------------------------------------
    # سحر الروابط الداخلية: جلب ألعاب من نفس التصنيف
    # ---------------------------------------------------------
    # استخراج الألعاب التي من نفس التصنيف، واستبعاد اللعبة الحالية
    related_candidates = [g for g in games_data if g["category"] == game["category"] and g["title"] != game["title"]]
    
    # اختيار 4 ألعاب عشوائياً (أو أقل إذا كان التصنيف صغيراً)
    related_games = random.sample(related_candidates, min(4, len(related_candidates)))
    
    # ضبط مسارات الروابط والصور للألعاب المشابهة لأننا داخل مجلد اللعبة
    adjusted_related_games = []
    for rg in related_games:
        rg_copy = rg.copy()
        rg_copy["image"] = "../" + rg["image"][2:] if rg["image"].startswith("./") else "../" + rg["image"]
        rg_copy["link"] = "../" + rg["link"].replace("./", "") # مثال: ../run-3/
        adjusted_related_games.append(rg_copy)
    # ---------------------------------------------------------
        
    # تمرير كل البيانات للقالب
    final_html = template.render(
        title=game["title"],
        category=game["category"],
        image=image_path,
        home_link="../index.html",
        iframe_url=game.get("iframe_url", ""),
        related_games=adjusted_related_games  # <--- إضافة الألعاب المشابهة
    )
    
    file_path = os.path.join(folder_name, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_html)

print("🎉 تمت العملية بنجاح! جميع الصفحات مترابطة داخلياً الآن.")