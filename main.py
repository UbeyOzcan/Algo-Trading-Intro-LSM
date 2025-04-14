from src.TI import TechInd
from src.Strategy import Strategy
from src.Plot import Plot
from src.Reporting import Report


w_bb = 20
w_rsi = 6
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TI = TechInd(ticker='AAPL', start_date='2019-01-01', end_date='2025-04-14', window_bb=w_bb, window_rsi=w_rsi)
    df = TI.moving_average(df=TI.df)
    df = TI.rolling_vol(df=df)
    df = TI.bollinger_band(df=df)
    df = TI.rsi(df=df)
    ST = Strategy()
    result, df = ST.bb_rsi(df=df, lower_rsi=30, upper_rsi=70)
    Plot = Plot(df=df, result=result)
    Plot.scatter()
    R = Report(df=df, result=result)
    R.ExcelReport()
    R.JsonReport()

