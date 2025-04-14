# Here is the Python module where we compute technical indicator based on input dataframe
from src.Data import DataFactory
import pandas as pd
import ta

class TechInd:
    def __init__(self, ticker:str, start_date: str, end_date: str, window_bb:int, window_rsi:int):
        self.DF = DataFactory(ticker=ticker, start_date=start_date, end_date=end_date)
        self.df = self.DF.get_closing_price()
        self.window_bb = window_bb
        self.window_rsi = window_rsi

    def moving_average(self, df:pd.DataFrame) -> pd.DataFrame:
        df[f'ma_{self.window_bb}'] = df.Close.rolling(window=self.window_bb).mean()
        return df

    def rolling_vol(self, df:pd.DataFrame):
        df[f'vol_{self.window_bb}'] = df.Close.rolling(window=self.window_bb).std()
        return df

    def bollinger_band(self, df:pd.DataFrame) -> pd.DataFrame:
        df['upper_bb'] =  df[f'ma_{self.window_bb}'] + (2 * df[f'vol_{self.window_bb}'])
        df['lower_bb'] = df[f'ma_{self.window_bb}'] - (2 * df[f'vol_{self.window_bb}'])
        return df

    def rsi(self, df:pd.DataFrame) -> pd.DataFrame:
        df[f'rsi'] = ta.momentum.rsi(df[f'ma_{self.window_bb}'])
        return df