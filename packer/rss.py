import csv
import requests
import xml.etree.ElementTree as ET
import re


def loadRSS():
    # url of rss feed
    url = 'https://www.cnbc.com/id/10000664/device/rss/rss.html'
    # creating HTTP response object from given url
    resp = requests.get(url)
    # saving the xml file
    with open('cnbc.xml', 'wb') as cnbc:
        cnbc.write(resp.content)


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()

    newsitems = []
    for item in root.findall('./channel/item'):
        for child in item:
            if child.tag == 'description':
                newsitems.append(child.text)
    return newsitems


def savetoCSV(newsitems, filename):

    with open(filename, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(newsitems)

def findsym_nasdaq(newsitem):
    with open('packer/nasdaq.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        symb="none"
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                stock=row[1].replace(",", "")
                stock=stock.replace(" Corporation", "")
                stock=stock.replace(" Inc.", "")
                stock=stock.replace(" Ltd.", "")
                stock=stock.replace(" Limited", "")
                stock=stock.replace(" Corp.", "")
                stock=stock.replace(" Corp", "")
                stock=stock.replace(" Ltd", "")
                stock=stock.replace(" Inc", "")
                stock=stock.replace(" LLC", "")
                if(stock in newsitem):
                    print(row[0])
                    symb=row[0]
                line_count += 1
    return symb


def findsym_nyse(newsitem):
    with open('packer/nyse.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        symb="none"
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                stock=row[1].replace(",", "")
                stock=stock.replace(" Corporation", "")
                stock=stock.replace(" Inc.", "")
                stock=stock.replace(" Ltd.", "")
                stock=stock.replace(" Limited", "")
                stock=stock.replace(" Corp.", "")
                stock=stock.replace(" Corp", "")
                stock=stock.replace(" Ltd", "")
                stock=stock.replace(" Inc", "")
                stock=stock.replace(" LLC", "")
                stock=stock.replace(" LP", "")
                stock=stock.replace(" Company", "")
                stock=stock.replace(" Co", "")
                stock=stock.replace(" &", "")
                stock=stock.replace(" (The)", "")
                stock=stock.replace(" Financial", "")
                stock=stock.replace(" L.P.", "")
                stock=stock.replace(" AG", "")
                stock=stock.replace(" PLC", "")
                stock=stock.replace(" Group", "")
                stock=stock.replace(" Holdings", "")
                stock=stock.replace(" International", "")
                #print(stock)
                if symb=="none" and stock in newsitem:
                    #print(row[0])
                    found=1
                    symb=row[0]
                line_count += 1
    return symb


def parser():
    loadRSS()
    newsitems = parseXML('cnbc.xml')
    return(newsitems)


def symbolget(newsitem):
    symb=findsym_nyse(newsitem)
    if symb=="none":
        symb=(findsym_nasdaq(newsitem))
    return(symb)
