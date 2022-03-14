import monthlyAverage
import weeklyAverage
import getInfo

if __name__ == "__main__":
    dataframe = monthlyAverage.get_dataframe()
    getInfo.get_mean(dataframe)
    getInfo.plot_data(dataframe)