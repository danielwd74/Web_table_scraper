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
        entry = {}
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
                        i = 0
                        for data in column:
                            if data.text != '' and data.text != 'NA':
                                if 'class="B4"' not in str(data):
                                    entry[months[i]] = float(data.text.strip())
                                else:
                                    #save year as a string instead of float
                                    entry[months[i]] = data.text.strip()
                            else:
                                entry[months[i]] = None
                            i = i + 1
                        dates.append(entry)
                    entry = {}
            else:
                print("Could not fetch table row")
        else:
            print("Could not fetch table")


        return pd.DataFrame(dates)

if __name__ == '__main__':
    dataframe = get_dataframe()
    getInfo.get_mean(dataframe)

