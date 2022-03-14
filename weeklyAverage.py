import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_weekly_dataframe():
    pass


base_url = 'https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMM_EPM0_PTE_SMA_DPG&f=w'
try:
        page = requests.get(base_url, timeout=4)
        soup = BeautifulSoup(page.content, 'html.parser')
except requests.exceptions.Timeout:
    print("Timeout exception occured")
else:
    dataframe = pd.DataFrame(columns=['year_month', 'week1_endDate', 'week1_value', 
    'week2_endDate', 'week2_value', 'week3_endDate', 'week3_value', 'week4_endDate',
    'week4_value', 'week5_endDate', 'week5_value'])
    #print(soup.prettify())
    table = soup.find("table", class_="FloatTitle")
    #print(table)
    if table:
        rows = table.find_all("tr")
        for row in rows:
            if 'class="B6"' in str(row):
                year_month = row.find("td", class_='B6')
                weeksEndDate = row.find_all("td", class_='B5')
                weeksValue = row.find_all("td", class_='B3')
                
                dataframe['year_month'].append(pd.Series(year_month.text))
                for endDate, value in zip(weeksEndDate, weeksValue):
                    print(endDate, value)
                #print(year_month)
                #print(new_dict)
        print(dataframe)