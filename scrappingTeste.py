from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

# print(soup)

table = soup.find('table', class_ = 'wikitable sortable')

#print(table)

table = soup.find_all('table')[0]

#print(table)

world_titles = table.find_all('th')

# print(world_titles)

world_table_titles = [title.text.strip() for title in world_titles]

# print(world_table_titles)

import pandas as pd

df = pd.DataFrame(columns = world_table_titles)

# print(df)

column_data = table.find_all('tr')

# print(column_data)

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)