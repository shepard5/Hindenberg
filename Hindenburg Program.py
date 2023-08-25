# This script repeatedly refreshes http://hindenburgresearch.com/ until Hindenburg Research publishes a new report 
# Just tweak the code in Hindenburg_Enter_Position, specifically under the tradeapi.submit_order field to fit your order, 
# fill in Alpaca API information with your key and secret, and execute the Hindenburg() function in IDLE
from bs4 import BeautifulSoup
import requests
import time
import alpaca_trade_api as tradeapi
import yfinance as yf

api = tradeapi.REST('YOUR_API_KEY', 'YOUR_API_SECRET', base_url='https://paper-api.alpaca.markets')

def Hindenburg():
    i = 0
    z = 0
    
    refreshed_body_text = ''

    while True:
        response = requests.get('http://hindenburgresearch.com/')  
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find('body').find_all('a')   
        eighth_link = links[7]['href']
        response = requests.get(eighth_link)
        soup = BeautifulSoup(response.content, "html.parser")
        if i == 0:
            first_body_text = soup.body.get_text()
            print(first_body_text)
            i=1   
        if i == 1:
            refreshed_body_text = soup.body.get_text() 
        if first_body_text == refreshed_body_text:
            ticker = ticker_search(refreshed_body_text)
            position = Hindenburg_Position(refreshed_body_text)
            Hindenburg_Enter_Position(position, ticker)
            break
        time.sleep(1)
        z = z+1
        print(z)
        

def Hindenburg_Position(body_text):
    search_string = "Initial Disclosure: After extensive research, we have taken a short position"
    index = body_text.find(search_string)  # Find the index of the search string in the input string
    if index == -1:
        position = 0
    else:
        position = 1
    return position


def ticker_search(body_text):
    search_string_1 = "(NASDAQ:"
    search_string_2 = "(NYSE:"
    i = 0
    if body_text.find(search_string_1) != -1: #Search for NASDAQ key
        index = body_text.find(search_string_1)       
        output = ""
        while body_text[index + len(search_string_1) + i] != ")":
            output += (body_text[index + len(search_string_1) + i]) #Create Ticker String
            i += 1
        ticker = output
    elif body_text.find(search_string_2) != -1:  #Search for NYSE key
        index = body_text.find(search_string_2)
        output = ""
        while body_text[index + len(search_string_2) + i] != ")":
            output += (body_text[index + len(search_string_2) + i]) #Create ticker string
            i += 1      
        ticker = output
    else:
        print("Ticker not found in new publishing!")
        ticker = ''
    return ticker


def Hindenburg_Enter_Position(position,ticker):
    ticker_data = yf.Ticker(ticker)

    current_price = ticker_data.info.get("currentPrice")
    principal = 2000.0
    share_quantity = 10
    if position == 1:
    # Short sell the stock
        tradeapi.submit_order(
            symbol=ticker,
            qty=share_quantity,  # Example: Short sell one share
            side='sell',
            type='market',
            time_in_force='gtc',
            order_class='simple',
        ) 
        print(f"Short sell executed for {ticker} at {current_price}!")
        return
    else:
        print("Condition not met for " + ticker)



