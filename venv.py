import pandas as pd
import xml.etree.ElementTree as ET
import io
from lxml import objectify

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("cnbc.xml")
root = tree.getroot()

f = open('test.csv', 'w')

csvwriter = csv.writer(f)

count = 0

head = ['title','description','pubDate']

csvwriter.writerow(head)

for time in root.findall('channel'):
    row = []
    title = time.find('title').text
    row.append(title)
    description = time.find('description').text
    row.append(description)
    pubDate = time.find('pubDate').text
    row.append(pubDate)
    csvwriter.writerow(row)
f.close()
