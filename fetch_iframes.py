import json
import requests
from bs4 import BeautifulSoup
import time

# ⚠️ اكتب الرابط هنا بالحروف الإنجليزية فقط (بدون أي حروف عربية)
base_url = "https://dnrweqffuwjtx.cloudfront.net/" 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

with open("games_data.json", "r", encoding="utf-8") as f:
    games_data = json.load(f)

print("🚀 جاري سحب روابط الـ Iframes الحقيقية...")

for game in games_data:
    game_path = game["link"].replace("./", "")
    full_url = f"{base_url}/{game_path}"
    
    try:
        response = requests.get(full_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # البحث عن Iframe
        iframe = soup.find("iframe", id="gameFrame") or soup.find("iframe")
        
        if iframe and iframe.has_attr("src"):
            iframe_src = iframe["src"]
            
            # إذا كان الرابط يبدأ بـ / (مثل /games/...) نضيف له رابط الموقع الأصلي ليعمل
            if iframe_src.startswith("/"):
                game["iframe_url"] = base_url + iframe_src
            else:
                game["iframe_url"] = iframe_src
                
            print(f"✅ تم العثور على اللعبة: {game['title']}")
        else:
            game["iframe_url"] = ""
            print(f"⚠️ لا يوجد Iframe في: {game['title']}")
            
    except Exception as e:
        game["iframe_url"] = ""
        print(f"❌ خطأ في {game['title']}")
        
    time.sleep(1)

with open("games_data_ready.json", "w", encoding="utf-8") as f:
    json.dump(games_data, f, ensure_ascii=False, indent=4)

print("\n🎉 اكتمل الفحص! تم حفظ الروابط الكاملة.")