from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
import re


def loadRSS():
    # url of rss feed
    url = 'https://finance.yahoo.com/rss/popularstories'
    # creating HTTP response object from given url
    resp = requests.get(url)
    # saving the xml file
    with open('cnbc.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []
    # iterate news items
    for item in root.findall('./channel/item'):
        # empty news dictionary
        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == 'description':
                #print(child.text)
                desc = child.text

                #print(desc.find("a"))
                #print(child.text
                newsitems.append(child.text)

            #else:
            #news[child.tag] = child.text
        # append news dictionary to news items list

    # return news items list
    #print (newsitems[0])
    return newsitems


def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    # writing to csv file
    with open(filename, 'w') as writeFile:
        # creating a csv dict writer object
        # writing headers (field names)
        # writing data rows
        writer = csv.writer(writeFile)

        writer.writerows(newsitems)



# load rss from web to update existing xml file
loadRSS()
# parse xml file
newsitems = parseXML('cnbc.xml')
# store news items in a csv file
savetoCSV(newsitems, 'cnbc.csv')


analyser = SentimentIntensityAnalyzer()


def print_sentiment_scores(sentence):
    bad=['flaw','too']
    snt = analyser.polarity_scores(sentence)
    #print(snt)
    #print("{:-<40} {}".format(sentence, str(snt)))
    #scores="{:-<40} {}".format(sentence, str(snt))
    scores=str(snt)
    result = scores.find('compound\': ')
    comp=scores[result+11:len(scores)-1]
    fcomp=float(comp)
    if any(neg_factor in sentence for neg_factor in bad):
    #if "flaw" in sentence:
        fcomp=fcomp-0.1
    print(fcomp)

#print_sentiment_scores(newsitems[0])
stock_sent=("")
print_sentiment_scores(stock_sent)
