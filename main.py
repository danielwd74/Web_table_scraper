import requests
from bs4 import BeautifulSoup
import pandas as pd
import getInfo

def get_dataframe():
    base_url = 'https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMM_EPM0_PTE_SMA_DPG&f=M'
    try:
        page = requests.get(base_url, timeout=2)
        soup = BeautifulSoup(page.content, 'html.parser')
    except requests.exceptions.Timeout:
        print("Timeout exception occured")
    else:
        dates = []
        section = []
        months = ['year', 'january', 'febuary', 'march', 'april', 'may', 'june', 'july', 
                    'august', 'september', 'october', 'november', 'december']
        table = soup.find("table", class_="FloatTitle")
        if table:
            tablerow = table.find_all("tr")
            if tablerow:
                #O(N^2) Time complexity
                for tabledata in tablerow:
                    column = tabledata.find_all('td')
                    if len(column) > 1:
                        for data in column:
                            if data.text != '' and data.text != 'NA':
                                section.append(float(data.text.strip()))
                            else:
                                section.append(None)
                        dates.append(section)
                    section = []
            else:
                print("Could not fetch table row")
        else:
            print("Could not fetch table")

        #O(N^2) Time complexity
        '''dateDict = []
        months = ['year', 'january', 'febuary', 'march', 'april', 'may', 'june', 'july', 
                    'august', 'september', 'october', 'november', 'december']
        for dateRow in dates:
        #    i = 2003
        #    dictTitle = 'Year:' + str(i)
            entry = {}
            i = 0
            for cell in dateRow:
                entry[months[i]] = cell
                i = i + 1
            dateDict.append(entry)'''

        return pd.DataFrame(dateDict)

if __name__ == '__main__':
    dataframe = get_dataframe()
    getInfo.get_mean(dataframe)

