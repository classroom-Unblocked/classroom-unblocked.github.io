import requests
from bs4 import BeautifulSoup
import json

# رابط الموقع الذي سنسحب منه البيانات
url = "https://steal-a-brainrot-unblocked.github.io/"

print("⏳ جاري الاتصال بالموقع وسحب البيانات...")
response = requests.get(url)

# التأكد من نجاح الاتصال
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    games_list = []

    # البحث عن كل الألعاب داخل قسم .grid-box
    for a_tag in soup.select('.grid-box a'):
        link = a_tag.get('href')
        img_tag = a_tag.find('img')
        
        if link and img_tag:
            img_src = img_tag.get('src')
            
            # استخراج اسم اللعبة من الرابط وتنظيفه (مثال: /go/jelly-truck.html -> Jelly Truck)
            raw_name = link.split('/')[-1].replace('.html', '')
            title = ' '.join(word.capitalize() for word in raw_name.split('-'))
            
            games_list.append({
                "title": title,
                "link": link,
                "image": img_src
            })

    # حفظ البيانات في ملف JSON
    with open('games.json', 'w', encoding='utf-8') as f:
        json.dump(games_list, f, indent=4, ensure_ascii=False)

    print(f"✅ تمت العملية بنجاح! تم استخراج {len(games_list)} لعبة وحفظها في ملف games.json")
else:
    print(f"❌ فشل الاتصال بالموقع. رمز الخطأ: {response.status_code}")