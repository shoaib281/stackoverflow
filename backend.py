import numpy as np 
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

class stocks():
    def __init__(self):
        pass

    def generateGraph(self, ticker):
        df = web.DataReader(ticker,data_source="yahoo", start="1/14/2009",end="4/1/2022")
        df = df[["Close"]]


        df.plot()
        plt.savefig("static/" + ticker + ".png")

