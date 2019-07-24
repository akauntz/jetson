from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import re
import requests
from packer import rss
from packer import act_graph
#from packer import symbol_getter

analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(sentence):
    bad=['flaw','too','plummeted', "take a hit"]
    good=['launches' 'all-time high']
    snt = analyser.polarity_scores(sentence)
    scores=str(snt)
    result = scores.find('compound\': ')
    comp=scores[result+11:len(scores)-1]
    fcomp=float(comp)
    fcomp=0.0

    if any(neg_factor in sentence for neg_factor in bad):
        fcomp=fcomp-0.1
    if any(pos_factor in sentence for pos_factor in good):
        fcomp=fcomp+0.1
    print(fcomp)

newsitems=rss.parser()
stock_sent=(newsitems[1])
print_sentiment_scores(stock_sent)
symbol=rss.symbolget(newsitems[1])

APIKEY="PEU86JCI19FBL1JC"
func="TIME_SERIES_DAILY"

url="https://www.alphavantage.co/query?function=" + func + "&symbol=" + symbol +"&apikey=" + APIKEY + "&datatype=csv"
resp = requests.get(url)
csv_file= "packer/stocks/" + symbol + ".csv"

with open(csv_file, 'wb') as f:
    f.write(resp.content)

act_graph.stock_reader(symbol)
