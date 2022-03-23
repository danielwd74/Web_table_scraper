import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_weekly_dataframe(rows):
    dfColumns = ['year_month', 'week1_endDate', 'week1_value', 
    'week2_endDate', 'week2_value', 'week3_endDate', 'week3_value', 'week4_endDate',
    'week4_value', 'week5_endDate', 'week5_value']
    row_dict = {'year_month': [],
                'week1_endDate': [],
                'week1_value': [],
                'week2_endDate': [],
                'week2_value': [],
                'week3_endDate': [],
                'week3_value': [],
                'week4_endDate': [],
                'week4_value': [],
                'week5_endDate': [],
                'week5_value': []}
    dataframe = pd.DataFrame(columns=dfColumns)
    for row in rows:
        if 'class="B6"' in str(row):
            year_month = row.find("td", class_='B6')
            weeksEndDate = row.find_all("td", class_='B5')
            weeksValue = row.find_all("td", class_='B3')
            
            # Performs in O(n^2), two for loops or arrays of size n 
            # Big O time complexity where space complexity is
            # O(n^4) where there are two arrays of size bytes 4n
            
            for endDate, value in zip(weeksEndDate, weeksValue):
                new_endate = year_month.text[:6] + "-" + endDate.text[:2] + "-" + endDate.text[3:]
                if value.text.strip() == '':
                    endDateNew = None
                    valueTextNew = None
                else:
                    endDateNew = new_endate.strip()
                    valueTextNew = value.text.strip()
                #print("(", endDateNew, ")", "(", valueTextNew, ")")
                row_dict['year_month'].append(year_month.text)
                row_dict['week1_endDate'].append(endDateNew)
                row_dict['week1_value'].append(valueTextNew)
                row_dict['week2_endDate'].append(endDateNew)
                row_dict['week2_value'].append(valueTextNew)
                row_dict['week3_endDate'].append(endDateNew)
                row_dict['week3_value'].append(valueTextNew)
                row_dict['week4_endDate'].append(endDateNew)
                row_dict['week4_value'].append(valueTextNew)
                row_dict['week5_endDate'].append(endDateNew)
                row_dict['week5_value'].append(valueTextNew)
                #print(value.text, endDate.text)
            #print(year_month)
            #print(new_dict)
    #print(row_dict)
    dataframe = pd.DataFrame.from_dict(row_dict)
    print(dataframe)

    


def get_rows():
    base_url = 'https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMM_EPM0_PTE_SMA_DPG&f=w'
    try:
            page = requests.get(base_url, timeout=4)
            soup = BeautifulSoup(page.content, 'html.parser')
    except requests.exceptions.Timeout:
        print("Timeout exception occured")
    else:
        table = soup.find("table", class_="FloatTitle")
        #print(table)
        if table:
            rows = table.find_all("tr")
            return rows
        else:
            return False
            

if __name__ == '__main__':
    rows = get_rows()
    get_weekly_dataframe(rows)