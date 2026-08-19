import json

# 1. قراءة بيانات الألعاب الـ 42
with open('games.json', 'r', encoding='utf-8') as f:
    games_data = json.load(f)

# 2. إعداد القسم العلوي من القالب (Header + Iframe + SEO Article)
html_top = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Play Steal a Brainrot Unblocked Online Free</title>
    <meta name="description" content="Play Steal a Brainrot unblocked online for free. No downloads required. Enjoy the best unblocked games for school right in your browser.">
    <meta name="keywords" content="steal a brainrot unblocked, steal a brainrot duel unblocked, unblocked games for school, play steal a brainrot online">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "VideoGame",
      "name": "Steal a Brainrot Unblocked",
      "description": "Play Steal a Brainrot unblocked directly in your browser. No downloads required.",
      "genre": "Action, Strategy",
      "gamePlatform": "Web Browser",
      "applicationCategory": "BrowserGame",
      "operatingSystem": "Windows, macOS, Linux, ChromeOS",
      "offers": { "@type": "Offer", "price": "0.00", "priceCurrency": "USD" },
      "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.7", "ratingCount": "23" }
    }
    </script>
</head>
<body class="bg-gray-900 text-gray-200 font-sans antialiased min-h-screen flex flex-col">

    <header class="bg-gray-800 border-b border-gray-700 py-4 shadow-md">
        <div class="max-w-6xl mx-auto px-4 flex justify-between items-center">
            <a href="/" class="text-2xl font-extrabold text-white tracking-tight">
                Steal a <span class="text-blue-500">Brainrot</span>
            </a>
            <nav class="hidden md:flex gap-4 text-sm font-medium">
                <a href="#about" class="hover:text-blue-400 transition">About</a>
                <a href="#more-games" class="hover:text-blue-400 transition">More Games</a>
            </nav>
        </div>
    </header>

    <main class="flex-grow max-w-6xl mx-auto px-4 py-8 w-full">
        
        <!-- Game Iframe Section -->
        <section class="mb-12">
            <div class="w-full bg-black rounded-xl border border-gray-700 shadow-2xl overflow-hidden relative" style="aspect-ratio: 16/9;">
                <!-- ⚠️ ضع رابط اللعبة الفعلي هنا ⚠️ -->
                <iframe src="https://st.8games.net/9/8g/igra-ukradi-brejnrot-original-3d/" class="absolute inset-0 w-full h-full z-10" frameborder="0" allowfullscreen></iframe>
            </div>
            <div class="flex justify-between items-center mt-4 px-2">
                <h1 class="text-2xl md:text-3xl font-bold text-white">Steal a Brainrot</h1>
                <button onclick="document.querySelector('iframe').requestFullscreen()" class="bg-blue-600 hover:bg-blue-500 text-white px-4 py-2 rounded font-bold transition shadow">Fullscreen ⛶</button>
            </div>
        </section>

        <!-- SEO Article -->
        <article id="about" class="bg-gray-800 rounded-xl p-6 border border-gray-700 shadow-lg mb-12">
            <h2 class="text-2xl font-bold text-blue-400 mb-3">Play Steal a Brainrot Unblocked Online Free</h2>
            <p class="text-gray-300 mb-4">Looking for the ultimate gaming experience during your break? You can now play <strong>Steal a Brainrot unblocked</strong> directly in your browser. Whether you are searching for unblocked games for school or just a fun way to pass the time, this game requires no downloads and runs smoothly on any network.</p>
            <h2 class="text-xl font-bold text-blue-400 mb-2">How to Play?</h2>
            <ul class="list-disc list-inside text-gray-300 space-y-1 ml-2">
                <li><strong class="text-white">Movement:</strong> Arrow keys or WASD.</li>
                <li><strong class="text-white">Action:</strong> Spacebar or Left Click.</li>
            </ul>
        </article>

        <!-- More Games Section (Grid) -->
        <section id="more-games" class="mb-12">
            <h2 class="text-2xl font-bold text-white border-l-4 border-blue-500 pl-3 mb-6">More Amazing Games</h2>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
"""

# 3. توليد شبكة الألعاب من ملف JSON
html_games = ""
for game in games_data:
    # تنسيق البطاقة باستخدام Tailwind CSS
    card = f"""
                <a href="{game['link']}" class="group block bg-gray-800 rounded-lg overflow-hidden border border-gray-700 hover:border-blue-500 hover:shadow-[0_0_15px_rgba(59,130,246,0.5)] transition duration-300">
                    <div class="relative aspect-square overflow-hidden bg-gray-900">
                        <img src="{game['image']}" alt="{game['title']}" loading="lazy" class="w-full h-full object-cover group-hover:scale-110 transition duration-300">
                    </div>
                    <div class="p-2 text-center">
                        <h3 class="text-sm font-semibold text-gray-300 group-hover:text-white truncate">{game['title']}</h3>
                    </div>
                </a>
"""
    html_games += card

# 4. إعداد القسم السفلي (Footer)
html_bottom = """
            </div>
        </section>
    </main>

    <footer class="bg-gray-950 py-6 border-t border-gray-800">
        <div class="max-w-6xl mx-auto px-4 text-center text-gray-500 text-sm">
            <p>&copy; 2026 Steal a Brainrot Unblocked. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

# 5. دمج وحفظ الملف النهائي
final_html = html_top + html_games + html_bottom

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("✅ تم بناء موقع Steal a Brainrot بنجاح! ملف index.html جاهز الآن وفيه 42 لعبة.")