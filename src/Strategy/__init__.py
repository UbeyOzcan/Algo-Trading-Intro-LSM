import pandas as pd
import numpy as np


class Strategy:
    def __init__(self):
        pass

    def bb_rsi(self, df: pd.DataFrame, lower_rsi: int, upper_rsi: int) -> [dict, pd.DataFrame]:
        df.columns = df.columns.droplevel(1)
        conditions = [(df.rsi < lower_rsi) & (df.Close < df.lower_bb),
                      (df.rsi > upper_rsi) & (df.Close > df.upper_bb)]
        choices = ['Buy', 'Sell']

        df['signal'] = np.select(conditions, choices, default='')
        df.dropna(inplace=True)
        df['signal'] = df['signal'].shift()

        position = False
        buydates, selldates = [], []
        buyprices, sellprices = [], []

        for index, row in df.iterrows():
            if not position and row['signal'] == 'Buy':
                buydates.append(index)
                buyprices.append(row['Open'])
                position = True

            if position and row['signal'] == 'Sell':
                selldates.append(index)
                sellprices.append(row['Open'])
                position = False

        R = (pd.Series([(sell - buy) / buy for sell, buy in zip(sellprices, buyprices)]) + 1).prod()
        pnl = (pd.Series([(sell - buy) for sell, buy in zip(sellprices, buyprices)])).sum()
        balance = [None if not position else df['Close'].iloc[-1]]
        return [{'Return': R, 'PnL' : pnl, 'balance' : balance, 'buydates': buydates, 'buyprices': buyprices, 'selldates': selldates, 'sellprices': sellprices}, df]
