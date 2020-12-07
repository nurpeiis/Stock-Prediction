import yfinance as yf # get financial data
from ta import add_all_ta_features #add technical indicators


def add_technical_indicators(history):
    return add_all_ta_features(history, open="Open", high="High", low="Low", close="Close", volume="Volume") # Substantiate data with momentum indicators

def get_data(stock_name, period='max', interval='1d'):
    """ 
        Given stock, it will return pandas DataFrame with various indicators of the price
        Specify period and interval, default values are max and 1d respectively
    """
    stock_ticker = yf.Ticker(stock_name)
    history = stock_ticker.history(period=period, interval=interval)
    history_with_technical_indicators = add_technical_indicators(history)
    return history_with_technical_indicators