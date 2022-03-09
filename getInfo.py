import pandas as pd

def get_mean(dataframe):
    dataframe['average'] = (dataframe.iloc[:, 1:].sum(axis=1) / dataframe.iloc[:, 1:].count(axis=1))
    print(dataframe)