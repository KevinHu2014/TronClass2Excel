# -*- coding: utf-8 -*-

# function import BeautifulSoup
from bs4 import BeautifulSoup
# genetic import codecs
import codecs
import csv
import pandas as pd

f = codecs.open("score.htm", 'r', 'utf-8')
soup = BeautifulSoup(f.read(), 'html.parser')
content = soup.find("div", {"class": "list-content"})
row = []
for index,child in enumerate(content.find_all("span", {"class": "ng-binding"}), 1):
    # 去掉開頭的數字
    if index % 5 != 1:
        row.append(child.get_text())
# print(row)


labels = ['學號', '姓名', '系級', '成績']
df = pd.DataFrame.from_records([row[i:i+4] for i in range(0, len(row), 4)], columns=labels)
# print(df)
writer = pd.ExcelWriter('score.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, index=False, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Adjust the column width.
worksheet.set_column(0, 1, 15)
worksheet.set_column(1, 2, 10)
worksheet.set_column(2, 3, 40)
worksheet.set_column(3, 4, 10)
writer.save()
