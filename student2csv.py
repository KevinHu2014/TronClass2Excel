# -*- coding: utf-8 -*-
# 匯出學生名單
# function import BeautifulSoup
from bs4 import BeautifulSoup
import csv
# genetic import codecs
import codecs
f = codecs.open("student.htm", 'r', 'utf-8')
soup = BeautifulSoup(f.read(), 'html.parser')
row = []
content = soup.find("div", {"class": "list-content"}, {"class": "clearfix"})
for child in content.find_all("span", {"class": "ng-scope"}, {"class": "ng-binding"}):
    row.append(child.get_text())

with open('student.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    for list in [row[i:i+4] for i in range(0, len(row), 4)]:
        csv_writer.writerow(list)
