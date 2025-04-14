import yfinance as yf


class DataFactory:
    def __init__(self, ticker: str, start_date: str, end_date: str):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def get_closing_price(self):
        return yf.download(tickers=self.ticker, start=self.start_date, end=self.end_date)

