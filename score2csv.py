# -*- coding: utf-8 -*-

# function import BeautifulSoup
from bs4 import BeautifulSoup
import csv
# genetic import codecs
import codecs
f = codecs.open("score.htm", 'r', 'utf-8')
soup = BeautifulSoup(f.read(), 'html.parser')
content = soup.find("div", {"class": "list-content"})
row = []
for child in content.find_all("span", {"class": "ng-binding"}):
    row.append(child.get_text())

with open('score.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    for list in [row[i:i+5] for i in range(0, len(row), 5)]:
        csv_writer.writerow(list)
