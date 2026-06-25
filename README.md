# Stock Price Checker

A simple stock price checker built with Python and Flask. Look up any stock ticker and get the current price and daily change.

## What it does

- Takes a stock symbol (e.g. AAPL, TSLA)
- Fetches the live price from the Alpha Vantage API
- Shows the current price, change, and percentage change
- Colour-coded: green for gains, red for losses

## Why I built it

I built this to practise working with external APIs in Python, and to have a finance-relevant project for my CV.

## Technologies used

- Python 3
- Flask
- Alpha Vantage API
- HTML/CSS/JavaScript

## How to run it

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```
