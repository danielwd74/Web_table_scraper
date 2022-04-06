import monthlyAverage
import weeklyAverage
import getInfo

if __name__ == "__main__":
    #dataframe_month = monthlyAverage.get_dataframe()
    #getInfo.get_average(dataframe_month)
    #getInfo.plot_data(dataframe_month)

    dataframe_week = weeklyAverage.get_weekly_dataframe()
    getInfo.get_average_month(dataframe_week)
    getInfo.plot_weekly_heatmap(dataframe_week)