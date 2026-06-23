from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "6CD7NFJV0747ZBFJ"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock')
def stock():
    symbol = request.args.get('symbol', '').upper()
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    quote = data.get('Global Quote', {})
    if not quote:
        return jsonify({"error": "Stock not found"})

    return jsonify({
        "symbol": quote.get('01. symbol'),
        "price": quote.get('05. price'),
        "change": quote.get('09. change'),
        "change_percent": quote.get('10. change percent')
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
