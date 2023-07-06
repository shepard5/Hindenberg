import requests
from bs4 import BeautifulSoup
import alpaca_trade_api as tradeapi
import time

API_KEY = 'YOUR ALPACA API KEY'
API_SECRET = 'YOUR PERSONAL ALPACA SECRET'
BASE_URL = 'https://paper-api.alpaca.markets'

## "https://hindenburgresearch.com/"
## Function parses Hindenburg Research HTML file and finds the most recent headline (8th link)

recursion_count = 0

def scrape_eighth_link(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all <a> tags within the body
    links = soup.find('body').find_all('a')
    
    eighth_link = None
    if len(links) >= 8:
        eighth_link = links[7]['href']

    # Send an HTTP GET request to the website and retrieve its content
    response = requests.get(eighth_link)
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the body tag and extract its text
    body_text = soup.body.get_text()
    ## TICKER SEARCH ##

    ticker_check = 'IEP'
    
    search_string_1 = "(NASDAQ:"
    search_string_2 = "(NYSE:"

    i = 1
 
    if body_text.find(search_string_1) != -1:  # If NASDAQ is found in the body of the text
        index = body_text.find(search_string_1)
        
        output = ""
        while body_text[index + len(search_string_1) + i] != ")":
            output += (body_text[index + len(search_string_1) + i]) # Incrementally add to the ticker string until ) is reached
            i += 1
        ticker = output

    elif body_text.find(search_string_2) != -1:  # If NYSE is found in the body of the text
        index = body_text.find(search_string_2)
        output = ""
        while body_text[index + len(search_string_2) + i] != ")":
            output += (body_text[index + len(search_string_2) + i]) # Incrementally add to the ticker string until ) is reached
            i += 1      
        ticker = output
    else:
        print("Ticker not found in the input. Function recursion ended")
        return
    
    ## POSITION SEARCH ##

    search_string = "Initial Disclosure: After extensive research, we have taken a short position"
    index = body_text.find(search_string)  # Find the index of the search string in the input string

    if index == -1:
        position = 0
    else:
        position = 1



#At this point, the position taken by hindenburg and the ticker are known, under the
#condition that their generic tag stating their initial disclosure is present in the article.

# Initialize the API client
    api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version='v2')

    
# Get the latest price and volume of the stock
    ticker = ticker
    latest_quote = api.get_latest_quote(ticker)
    latest_price = latest_quote.bp
    #latest_volume = latest_quote.as
    latest_quote = api.get_latest_quote(ticker)
    ask_size = getattr(latest_quote, 'as')

    
    print(latest_quote)
# Determine size of position based on stock price
    principal = 3000.0
    share_quantity = principal//latest_price

# Check if the condition is met
    if position == 1:
    # Short sell the stock
        api.submit_order(
            symbol=ticker,
            qty=share_quantity,  # Example: Short sell one share
            side='sell',
            type='market',
            time_in_force='gtc',
            order_class='simple',
        )

        print( api.submit_order(
            symbol=ticker,
            qty=3,  # Example: Short sell one share
            side='sell',
            type='market',
            time_in_force='gtc',
            order_class='simple',
        ))
        print("Short sell executed for {ticker} at {latest_price}.")
        return
        global c
        c = 1
    else:
        print("Condition not met for " + ticker)
        x=0

        ## Recursion ##

    #global recursion_count
    #recursion_count = recursion_count + 1
    
    print("Function executed " + str(recursion_count) + " times")
    #time.sleep(1)
    return

    #scrape_eighth_link(url)
        
##Almost done, as of 5/13 - 5/14 need to figure out the iterative process and counting in recursion without killing memory
    

    


