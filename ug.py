from bs4 import BeautifulSoup
import json

# 1. قراءة كود HTML من الملف الذي أنشأته
try:
    with open("site.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    games_data = []

    # 2. البحث عن الألعاب (العناصر التي تحمل كلاس c-card)
    articles = soup.find_all("article", class_="c-card")

    for article in articles:
        # استخراج اسم اللعبة والرابط
        title_element = article.find("div", class_="c-card__title").find("a")
        title = title_element.text.strip()
        link = title_element["href"]
        
        # استخراج مسار الصورة
        img_element = article.find("img")
        image_src = img_element["src"] if img_element else ""
        
        # استخراج التصنيف
        tag_element = article.find("a", class_="c-card__tag")
        tag = tag_element.text.strip() if tag_element else "بدون تصنيف"
        
        # حفظ اللعبة في القائمة
        games_data.append({
            "title": title,
            "link": link,
            "image": image_src,
            "category": tag
        })

    # 3. طباعة وحفظ النتائج
    print(f"تم بنجاح استخراج {len(games_data)} لعبة!\n")
    
    if len(games_data) > 0:
        # طباعة أول 3 ألعاب للتأكد
        print("عينة من البيانات المستخرجة:")
        print(json.dumps(games_data[:3], ensure_ascii=False, indent=2))
        
        # حفظ جميع البيانات في ملف JSON لتستخدمها لاحقاً في قالبك الجديد
        with open("games_data.json", "w", encoding="utf-8") as out_file:
            json.dump(games_data, out_file, ensure_ascii=False, indent=4)
        print("\n✅ تم حفظ جميع الألعاب بنجاح في ملف 'games_data.json' في نفس المجلد!")

except FileNotFoundError:
    print("❌ خطأ: لم أتمكن من العثور على ملف 'site.html'. يرجى التأكد من إنشائه في نفس المجلد.")