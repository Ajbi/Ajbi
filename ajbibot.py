import requests
import os
from dotenv import load_dotenv
from pybit.unified_trading import HTTP

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def dergo_mesazh(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=payload)
    print("Status kodi:", response.status_code)
    print("Përgjigjja:", response.text)

def merr_cmimin(symbol="BTCUSDT"):
    session = HTTP(testnet=False)
    data = session.get_ticker(symbol=symbol)
    price = data['result']['lastPrice']
    return f"💹 Çmimi aktual i {symbol} është: {price}"

# Test sinjal për ETHUSDT
if __name__ == "__main__":
    mesazhi = merr_cmimin("ETHUSDT")
    dergo_mesazht(mesazhi)

