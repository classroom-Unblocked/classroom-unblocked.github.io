import csv
import re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

# رابط الصفحة التي تحتوي على الألعاب
BASE_URL = "https://dnrweqffuwjtx.cloudfront.net/new-games/"  # ضع هنا الرابط الحقيقي للصفحة
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        " (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    )
}


def scrape_games_page(url):
    print("⏳ جاري قراءة الصفحة الرئيسية واستخراج روابط الألعاب...")
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"❌ فشل الاتصال بالموقع، كود الاستجابة: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ حدث خطأ أثناء الاتصال: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # استخراج روابط الألعاب داخل المحتوى
    content_area = soup.select_one(".post__entry")
    if not content_area:
        print("❌ لم يتم العثور على عنصر المحتوى الرئيسي.")
        return []

    games_data = []
    links = content_area.find_all("a")

    for a_tag in links:
        title = a_tag.get_text(strip=True)
        href = a_tag.get("href")

        # تجاهل الروابط الفارغة أو المعطوبة
        if not href or href.startswith("#") or not title:
            continue

        full_url = urljoin(url, href)
        games_data.append({"Title": title, "Page_URL": full_url})

    print(f"✅ تم العثور على {len(games_data)} لعبة في القائمة.")
    return games_data


def main():
    games = scrape_games_page(BASE_URL)

    if games:
        output_file = "scraped_games.csv"
        with open(
            output_file, mode="w", newline="", encoding="utf-8-sig"
        ) as csv_file:
            fieldnames = ["Title", "Page_URL"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(games)

        print(f"\n🎉 تم حفظ البيانات بنجاح في ملف: {output_file}")


if __name__ == "__main__":
    main()