import json
import os

# 1. فتح ملف الألعاب الأساسي (90 لعبة)
with open('games_data_ready.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

# 2. فتح ملف مقالات السيو مع حماية ضد الملفات الفارغة أو التالفة
seo_data = []
if os.path.exists('seo_data.json') and os.path.getsize('seo_data.json') > 0:
    try:
        with open('seo_data.json', 'r', encoding='utf-8') as f:
            seo_data = json.load(f)
    except json.JSONDecodeError:
        print("⚠️ تحذير: ملف seo_data.json يحتوي على خطأ في تنسيق JSON. يجدر مراجعة محتواه.")
else:
    print("⚠️ تنبيه: ملف seo_data.json فارغ حالياً. سيعمل الموقع بالقيم الافتراضية حتى تقوم بملئه.")

seo_dict = {game['title']: game for game in seo_data}

# 3. عملية الدمج الذكية
updated_count = 0
for game in main_data:
    title = game['title']
    if title in seo_dict:
        game['long_description'] = seo_dict[title]['long_description']
        game['features'] = seo_dict[title]['features']
        updated_count += 1

# 4. حفظ البيانات المدمجة فوق الملف الأساسي
with open('games_data_ready.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, indent=4, ensure_ascii=False)

print(f"✅ تمت العملية بنجاح! تم تحديث {updated_count} لعبة بمقالات السيو من أصل {len(main_data)} لعبة.")