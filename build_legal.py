import os
from jinja2 import Template

# 1. قراءة القالب
with open("page_template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

template = Template(template_content)

# 2. البيانات والنصوص الخاصة بكل صفحة
pages_data = [
    {
        "filename": "privacy.html",
        "title": "Privacy Policy",
        "content": """
            <p>At <strong>Classroom Games Unblocked</strong>, your privacy is our priority. This Privacy Policy outlines the types of information we collect and how it is used.</p>
            <h3 class="text-xl font-bold text-white mt-6 mb-2">1. Information We Collect</h3>
            <p>We do not require users to create accounts, so we do not collect personal identifying information like names or emails unless you contact us directly. We may collect non-personal information such as browser types and IP addresses for analytics purposes.</p>
            <h3 class="text-xl font-bold text-white mt-6 mb-2">2. Cookies</h3>
            <p>We use cookies to improve user experience, such as saving your recently played games. Third-party partners (like Google Analytics or Disqus) may also use cookies to serve relevant content.</p>
            <h3 class="text-xl font-bold text-white mt-6 mb-2">3. External Links</h3>
            <p>Our website may contain links to external sites. We are not responsible for the privacy practices of these third-party websites.</p>
            <p class="mt-8 text-sm text-gray-400">Last updated: August 2026</p>
        """
    },
    {
        "filename": "terms.html",
        "title": "Terms of Use",
        "content": """
            <p>Welcome to <strong>Classroom Games Unblocked</strong>. By accessing our website, you agree to these Terms of Use.</p>
            <h3 class="text-xl font-bold text-white mt-6 mb-2">1. Use of the Site</h3>
            <p>Our website provides free, unblocked web games for entertainment and educational purposes. You agree to use the site responsibly and not to engage in any activity that disrupts the website's functionality.</p>
            <h3 class="text-xl font-bold text-white mt-6 mb-2">2. Copyright and Trademarks</h3>
            <p>All games provided on this website are embedded or hosted for fair use. The intellectual property rights of the games belong to their respective developers and publishers. If you are a developer and wish for a game to be removed, please contact us.</p>
            <h3 class="text-xl font-bold text-white mt-6 mb-2">3. Disclaimer of Warranties</h3>
            <p>The site and its contents are provided "as is" without any warranties. We do not guarantee that the site will be error-free or uninterrupted.</p>
            <p class="mt-8 text-sm text-gray-400">Last updated: August 2026</p>
        """
    },
    {
        "filename": "contact.html",
        "title": "Contact Us",
        "content": """
            <p>We would love to hear from you! Whether you have a game request, feedback, or a business inquiry, feel free to reach out.</p>
            <div class="bg-gray-900 p-6 rounded-xl mt-6 border border-gray-700 text-center">
                <svg class="w-12 h-12 text-blue-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                <h3 class="text-2xl font-bold text-white mb-2">Email Us</h3>
                <a href="mailto:contact@classroomgames.com" class="text-blue-400 hover:text-blue-300 text-xl font-semibold transition">contact@classroomgames.com</a>
            </div>
            <p class="mt-6 text-gray-400 text-center">We aim to respond to all emails within 24-48 hours.</p>
        """
    }
]

# 3. بناء الملفات وحفظها
print("🚀 جاري بناء الصفحات القانونية (Privacy, Terms, Contact)...")
for page in pages_data:
    final_html = template.render(
        title=page["title"],
        content=page["content"]
    )
    with open(page["filename"], "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"✅ تم إنشاء: {page['filename']}")

print("🎉 اكتملت العملية بنجاح!")