import alpaca_trade_api as tradeapi
import yfinance

def Hindenburg_Enter_Position(position,ticker):
    ticker_data = yfinance.Ticker(ticker)
    current_price = ticker.info["RegularMarketPrice"]

    principal = 2000.0
    share_quantity = principal//current_price


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


        
        print("Short sell executed for {ticker} at {current_price}.")
        return

    else:
        print("Condition not met for " + ticker)

