import json
import os
import requests

# ضع رابط الموقع الأصلي هنا
base_url = "https://dnrweqffuwjtx.cloudfront.net" 

# قراءة بيانات الألعاب
with open("games_data.json", "r", encoding="utf-8") as f:
    games_data = json.load(f)

print("🚀 جاري بدء تحميل الصور، يرجى الانتظار...")

for game in games_data:
    img_path = game["image"]
    
    # التأكد أن المسار نسبي ويبدأ بـ ./
    if img_path.startswith("./"):
        # إزالة ./ من البداية ليكون المسار مثلاً media/posts/...
        local_path = img_path[2:] 
        
        # الرابط الكامل للصورة على الإنترنت
        image_url = f"{base_url}/{local_path}"
        
        # إنشاء المجلدات محلياً إذا لم تكن موجودة
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        # تحميل الصورة إذا لم تكن محملة مسبقاً
        if not os.path.exists(local_path):
            try:
                response = requests.get(image_url, stream=True)
                if response.status_code == 200:
                    with open(local_path, 'wb') as img_file:
                        for chunk in response.iter_content(1024):
                            img_file.write(chunk)
                    print(f"✅ تم تحميل: {local_path}")
                else:
                    print(f"❌ فشل تحميل (خطأ {response.status_code}): {image_url}")
            except Exception as e:
                print(f"⚠️ حدث خطأ أثناء تحميل {image_url}: {e}")

print("\n🎉 اكتمل تحميل جميع الصور بنجاح!")