import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cmap
import numpy as np


def get_average(dataframe):
    dataframe['average'] = (dataframe.iloc[:, 1:].sum(axis=1) / dataframe.iloc[:, 1:].count(axis=1))
    #print(dataframe)

def get_average_month(dataframe):
    dataframe['average'] = round((dataframe.iloc[:, [False, False, False, True, False, True, False, True, False, True, False, True]].sum(axis=1) / 
                            dataframe.iloc[:, [False, False, False, True, False, True, False, True, False, True, False, True]].count(axis=1)), 2)
    

def plot_data(dataframe):
    x = dataframe['year']
    y = dataframe['average']
    plt.title("Average gas prices per year")
    plt.xlabel("Years")
    plt.ylabel("Average gas prices in ($)")
    plt.plot(x, y, marker='o', linestyle='dashed')
    plt.tight_layout()
    plt.show()

def plot_weekly_data(dataframe):
    #plot the year_month
    x = dataframe['year_month']
    #plt.rcParams["figure.figsize"] = [len(dataframe['year_month']), len(dataframe['average'])]
    #plt.figure(figsize=)
    plt.figure(figsize=(310,5))
    plt.xticks(range(len(dataframe['year_month'])), fontsize=6)
    plt.tick_params(axis='x', labelrotation=90)
    #plot the average for 5 weeks
    y = dataframe['average']
    plt.title("Average gas prices per year by month")
    plt.margins(x=0, y=0)
    plt.xlabel("Years", labelpad=17)
    plt.ylabel("Average gas prices in ($)") 
    
    plt.plot(x, y)
   
    #plt.savefig("Weekly_Yearly_Cost.png")
    plt.show()

def plot_weekly_heatmap(df: pd.DataFrame):
    years = df['year'].unique()
    months = df['month'].unique()
    months_label = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    new_list = []
    for month in months:
        month_list = []
        for year in years:
            #print(df['average'].loc[(df['month'] == month) & (df['year'] == year)])
            average = df['average'].loc[(df['month'] == month) & (df['year'] == year)].to_list()
            if (len(average) > 0):
                month_list.append(float(average[0]))
            else:
                month_list.append(0)
        new_list.append(month_list)

    
    # used https://matplotlib.org/3.5.0/gallery/images_contours_and_fields/image_annotated_heatmap.html
    # to help me make heat map
    fig, ax = plt.subplots()
    im = ax.imshow(new_list, cmap=cmap.hot)

    ax.set_yticks(np.arange(len(months)), labels=reversed(months_label))
    ax.set_xticks(np.arange(len(years)), labels=years)

    plt.setp(ax.get_xticklabels(), rotation=90, ha='right', rotation_mode='anchor')

    for i in range(len(months)):
        for j in range(len(years)):
            text = ax.text(j, i, new_list[i][j], color="b", ha="center", va="center")

    fig.tight_layout()
    plt.show()
    
    #average = df['average'].to_list()






    