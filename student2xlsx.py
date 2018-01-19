# -*- coding: utf-8 -*-
# 匯出學生名單

from bs4 import BeautifulSoup
import pandas as pd
# genetic import codecs
import codecs
f = codecs.open("student.htm", 'r', 'utf-8')
soup = BeautifulSoup(f.read(), 'html.parser')
row = []
content = soup.find("div", {"class": "list-content"}, {"class": "clearfix"})
for child in content.find_all("span", {"class": "ng-scope"}, {"class": "ng-binding"}):
    row.append(child.get_text())
# print(row)

labels = ['學號', '姓名', '系級', '課程角色']
df = pd.DataFrame.from_records([row[i:i+4] for i in range(0, len(row), 4)], columns=labels)
# print(df)
writer = pd.ExcelWriter('student.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, index=False, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Adjust the column width.
worksheet.set_column(0, 1, 15)
worksheet.set_column(1, 2, 10)
worksheet.set_column(2, 3, 35)
worksheet.set_column(3, 4, 10)
writer.save()
