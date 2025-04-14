import pandas as pd
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, df: pd.DataFrame, result:dict):
        self.df = df
        self.result = result

    def scatter(self):
        plt.plot(self.df['Close'])
        plt.scatter(self.df.loc[self.result['buydates']].index, self.df.loc[self.result['buydates']].Close, marker = '^', c = 'g')
        plt.scatter(self.df.loc[self.result['selldates']].index, self.df.loc[self.result['selldates']].Close, marker='v', c='r')
        plt.savefig('Strategy.png')