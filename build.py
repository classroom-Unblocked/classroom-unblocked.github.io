import json
from jinja2 import Template

with open("games_data.json", "r", encoding="utf-8") as f:
    games_data = json.load(f)

with open("template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

template = Template(template_content)

# أضفنا base_path هنا
final_html = template.render(
    page_title="جميع الألعاب",
    games=games_data,
    base_path="./" 
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)
print("✅ تم بناء الصفحة الرئيسية بنجاح!")