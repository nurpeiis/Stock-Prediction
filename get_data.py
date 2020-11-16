import yfinance as yf


def get_data(stock_name, period='max', interval='1d'):
    stock_ticker = yf.Ticker(stock_name)
    hist = stock_ticker.history(period=period, interval=interval)
    return hist
    """
    For detailed manipulation
    open_p = hist['Open']
    high_p = hist['High']
    low_p = hist['Low']
    close_p = hist['Close']
    dates = hist.index.to_series().values
    start_date = dates[0]
    end_date = dates[-1]
    """