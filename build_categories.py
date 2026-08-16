import json
import os
from jinja2 import Template

# 1. قراءة البيانات
with open("games_data.json", "r", encoding="utf-8") as f:
    games_data = json.load(f)

# 2. قراءة القالب الرئيسي
with open("template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

template = Template(template_content)

print("🚀 جاري بناء صفحات الأقسام (Categories)...")

# 3. استخراج جميع التصنيفات الفريدة (إزالة التكرار)
# نستخدم set لجمع الأسماء دون تكرار
categories = set()
for game in games_data:
    categories.add(game["category"])

# 4. بناء صفحة لكل تصنيف
for category in categories:
    # تنظيف اسم التصنيف ليكون مناسباً كاسم مجلد (مثلاً: تحويل "2 Player" إلى "2-player")
    folder_name = category.lower().replace(" ", "-").replace("'", "")
    
    # إنشاء مجلد داخل مجلد يسمى 't' (مثل الموقع الأصلي ./t/car/)
    category_path = os.path.join("t", folder_name)
    os.makedirs(category_path, exist_ok=True)
    
    # فلترة الألعاب (اختيار الألعاب التي تنتمي لهذا القسم فقط)
    category_games = []
    for game in games_data:
        if game["category"] == category:
            # بما أن صفحة القسم ستكون داخل مجلد /t/car/، نحتاج لتعديل مسارات الصور والروابط خطوتين للوراء ../../
            adjusted_game = game.copy()
            if adjusted_game["image"].startswith("./"):
                adjusted_game["image"] = "../../" + adjusted_game["image"][2:]
            else:
                adjusted_game["image"] = "../../" + adjusted_game["image"]
                
            adjusted_game["link"] = "../../" + adjusted_game["link"].replace("./", "")
            category_games.append(adjusted_game)
    
    # توليد صفحة الـ HTML الخاصة بهذا القسم فقط
    final_html = template.render(
        page_title=f"قسم ألعاب {category}",
        games=category_games,
        base_path="../../" # <--- أضف هذا السطر
    )
    
    # حفظ الصفحة
    file_path = os.path.join(category_path, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    
    print(f"✅ تم بناء قسم: {category} (يحتوي على {len(category_games)} ألعاب)")

print("\n🎉 انتهت المهمة بنجاح! جميع الأقسام جاهزة داخل مجلد 't'.")