import time
import requests

# === CONFIG ===
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"
SYMBOL = "BTCUSDT"

def get_price():
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={SYMBOL}"
    r = requests.get(url).json()
    return float(r['price'])

def send_signal(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    requests.post(url, data=data)

print("Future Signal Bot Started...")
while True:
    try:
        price = get_price()
        print(f"{SYMBOL} Price: {price}")
        
        # Example Simple Signal Logic
        if price > 70000:
            send_signal(f"🚀 LONG SIGNAL: {SYMBOL} is pumping! Price: {price}")
        elif price < 60000:
            send_signal(f"🔻 SHORT SIGNAL: {SYMBOL} dumping! Price: {price}")
            
        time.sleep(60) # Check every 1 minute
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
