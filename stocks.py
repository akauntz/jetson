from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import re
import requests
from packer import rss
from packer import act_graph
#from packer import symbol_getter
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()

analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(sentence):
    bad=["flaw","too","plummeted", "hit", "threat", "miss", "slide", "drop","charge","sink","disappointing","low"]
    good=["launches","all-time","tops","climb","upgrade","beat","rise","double", "record-breaking", "strong", "above", "boosted", "high"]
    snt = analyser.polarity_scores(sentence)
    scores=str(snt)
    result = scores.find('compound\': ')
    comp=scores[result+11:len(scores)-1]
    fcomp=float(comp)
    fcomp=0.0

    for neg_factor in bad:
        if neg_factor in sentence:
            fcomp=fcomp-0.1
    for pos_factor in good:
        if pos_factor in sentence:
            fcomp=fcomp+0.1
    return(fcomp)



def alpha(symbol, sent):
    APIKEY="PEU86JCI19FBL1JC"
    func="TIME_SERIES_DAILY"

    url="https://www.alphavantage.co/query?function=" + func + "&symbol=" + symbol +"&apikey=" + APIKEY + "&datatype=csv"
    resp = requests.get(url)
    csv_file= "packer/stocks/" + symbol + ".csv"

    with open(csv_file, 'wb') as f:
        f.write(resp.content)

    act_graph.stock_reader(symbol, sent)


newsitems=rss.parser()
for item in newsitems:
    item=item.replace("&amp;", "&")
    #item=item.replace("&#039 ;", "''")
    if "See which" not in item and "Names on the move ahead" not in item:
        stock_sent=item
        symbol=rss.symbolget(stock_sent)
        if symbol != "none":
            score=print_sentiment_scores(stock_sent)
            print(symbol + ": " + str(score))
            alpha(symbol, score)
