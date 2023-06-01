from flask import Flask, render_template, request
import requests
import json
from openbb_terminal.sdk import openbb

# ticker = flask.request.form['ticker'].upper()






app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def ticker_input():
    if request.method == 'POST':
        ticker_symbol = request.form['tickerInput']
        
        # Call the Open Terminal SDK to get the stock price
        stock_price = openbb.stocks.options.ta.summary(ticker_symbol)
        
        return render_template('index.html', stock_price=stock_price)
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run()














# def index():
#     return render_template('index.html')


# @app.route('/dashboard', methods = ['POST'])







# def ticker_input():
#     if request.method == 'POST':
#         ticker_symbol = request.form['tickerInput']
        
#         # Call an API or use your own logic to retrieve the stock data
#         stock_data = get_stock_data(ticker_symbol)
        
#         return render_template('index.html', stock_data=stock_data)
    
#     return render_template('index.html')

# def get_stock_data(ticker_symbol):
#     # Call an API to retrieve the stock data based on the ticker symbol
#     # Replace the API endpoint with your desired source
#     api_url = f"https://api.example.com/stocks/{ticker_symbol}"
#     response = requests.get(api_url)
    
#     if response.status_code == 200:
#         stock_data = json.loads(response.text)
#         return stock_data
    
#     return None

# if __name__ == '__main__':
#     app.run()
