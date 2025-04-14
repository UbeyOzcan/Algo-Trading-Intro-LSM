import pandas as pd
import json
import numpy as np

class Report:
    def __init__(self, df: pd.DataFrame, result: dict):
        self.df = df
        self.result = result

    def ExcelReport(self):
        self.df.to_excel('report.xlsx')

    def JsonReport(self):
        self.result['buydates'] = [str(i) for i in self.result['buydates']]
        self.result['selldates'] = [str(i) for i in self.result['selldates']]
        with open("result.json", "w") as outfile:
            json.dump(self.result, outfile)
