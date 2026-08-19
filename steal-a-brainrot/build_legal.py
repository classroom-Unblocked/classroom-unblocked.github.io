import os

site_name = "Steal a Brainrot Unblocked"
email = "davidjoseph6361@gmail.com"

# قالب HTML الأساسي
def get_template(title, content):
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {site_name}</title>
    <meta name="robots" content="noindex, follow"> <!-- لا نريد أرشفة هذه الصفحات في جوجل، لكن نريد للروبوتات تتبعها -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-gray-200 font-sans antialiased min-h-screen flex flex-col">

    <header class="bg-gray-800 border-b border-gray-700 py-4 shadow-md">
        <div class="max-w-6xl mx-auto px-4 flex justify-between items-center">
            <a href="/" class="text-2xl font-extrabold text-white tracking-tight">
                Steal a <span class="text-blue-500">Brainrot</span>
            </a>
            <nav class="hidden md:flex gap-4 text-sm font-medium">
                <a href="/" class="hover:text-blue-400 transition text-white border-b-2 border-blue-500 pb-1">Back to Home</a>
            </nav>
        </div>
    </header>

    <main class="flex-grow max-w-4xl mx-auto px-4 py-12 w-full">
        <div class="bg-gray-800 rounded-xl p-8 md:p-12 border border-gray-700 shadow-xl prose prose-invert max-w-none">
            <h1 class="text-3xl md:text-4xl font-bold text-white mb-8 border-b border-gray-700 pb-4">{title}</h1>
            <div class="space-y-6 text-gray-300 leading-relaxed">
                {content}
            </div>
        </div>
    </main>

    <footer class="bg-gray-950 py-6 border-t border-gray-800 mt-auto">
        <div class="max-w-6xl mx-auto px-4 text-center text-gray-500 text-sm flex flex-col md:flex-row justify-center items-center gap-4">
            <p>&copy; 2026 {site_name}. All rights reserved.</p>
            <div class="flex gap-4">
                <a href="privacy.html" class="hover:text-white transition">Privacy Policy</a>
                <a href="terms.html" class="hover:text-white transition">Terms of Service</a>
                <a href="contact.html" class="hover:text-white transition">Contact Us</a>
            </div>
        </div>
    </footer>
</body>
</html>"""

# 1. محتوى سياسة الخصوصية
privacy_content = f"""
    <h2 class="text-xl font-bold text-blue-400">1. Information We Collect</h2>
    <p>We do not collect any personal data from our users. We use Google Analytics to monitor standard website traffic which helps us improve your gaming experience.</p>
    <h2 class="text-xl font-bold text-blue-400">2. Cookies</h2>
    <p>We may use cookies to enhance user experience. You can choose to set your web browser to refuse cookies, or to alert you when cookies are being sent.</p>
    <h2 class="text-xl font-bold text-blue-400">3. Third-Party Links</h2>
    <p>Our site may contain links to other websites. We have no control over the content or privacy practices of these external sites.</p>
"""

# 2. محتوى شروط الاستخدام
terms_content = f"""
    <h2 class="text-xl font-bold text-blue-400">1. Acceptance of Terms</h2>
    <p>By accessing and playing games on {site_name}, you accept and agree to be bound by the terms and provision of this agreement.</p>
    <h2 class="text-xl font-bold text-blue-400">2. Website Usage</h2>
    <p>All games provided on this website are free to play. You agree not to use this website for any unlawful purpose.</p>
    <h2 class="text-xl font-bold text-blue-400">3. Intellectual Property</h2>
    <p>The games hosted on this site belong to their respective creators and copyright holders. We provide access to these games strictly for entertainment purposes.</p>
"""

# 3. محتوى اتصل بنا
contact_content = f"""
    <p>We would love to hear from you! Whether you have a game request, found a bug, or just want to say hello, feel free to reach out to us.</p>
    <div class="bg-gray-900 p-6 rounded-lg border border-gray-700 mt-6 text-center">
        <p class="text-lg text-white mb-2">You can email us directly at:</p>
        <a href="mailto:{email}" class="text-2xl font-bold text-blue-500 hover:text-blue-400 transition">{email}</a>
    </div>
"""

# إنشاء الملفات
pages = {
    "privacy.html": ("Privacy Policy", privacy_content),
    "terms.html": ("Terms of Service", terms_content),
    "contact.html": ("Contact Us", contact_content)
}

for filename, (title, content) in pages.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(get_template(title, content))

print("✅ تم إنشاء الصفحات القانونية الثلاث بنجاح (privacy.html, terms.html, contact.html)!")