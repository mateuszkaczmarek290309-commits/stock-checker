from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock')
def stock():
    symbol = request.args.get('symbol', '').upper()
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"
    response = requests.get(url)
    data = response.json()

    price = data.get('c')
    change = data.get('d')
    change_percent = data.get('dp')

    if not price:
        return jsonify({"error": "Stock not found"})

    return jsonify({
        "symbol": symbol,
        "price": round(price, 2),
        "change": round(change, 2),
        "change_percent": round(change_percent, 2)
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
