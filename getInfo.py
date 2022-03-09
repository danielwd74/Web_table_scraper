import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_mean(dataframe):
    dataframe['average'] = (dataframe.iloc[:, 1:].sum(axis=1) / dataframe.iloc[:, 1:].count(axis=1))
    #print(dataframe)

def plot_data(dataframe):
    x = dataframe['year']
    y = dataframe['average']
    plt.title("Average gas prices per year")
    plt.xlabel("Years")
    plt.ylabel("Average gas prices in ($)")
    plt.plot(x, y, marker='o', linestyle='dashed')
    plt.tight_layout()
    plt.show()