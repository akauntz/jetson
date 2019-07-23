import csv
import re
import requests
from packer import vader
from packer import act_graph

APIKEY="PEU86JCI19FBL1JC"
func="TIME_SERIES_DAILY"
symbol=input("Stock Symbol: ").upper()
#if symbol
url="https://www.alphavantage.co/query?function=" + func + "&symbol=" + symbol +"&apikey=" + APIKEY + "&datatype=csv"
resp = requests.get(url)
csv_file= "packer/stocks/" + symbol + ".csv"

with open(csv_file, 'wb') as f:
    f.write(resp.content)

act_graph.stock_reader(symbol)
