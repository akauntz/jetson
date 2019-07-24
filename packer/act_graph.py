import csv
import re
import requests

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def stock_reader(symbol):
    with open('packer/stocks/'+symbol+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        dates = []
        prices = []
        for row in csv_reader:
            if line_count == 1:
                today=row[0]
                #print(date_object-timedelta(30))
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif line_count<22:
                day=row[0]
                date_object = datetime.strptime(day, '%Y-%m-%d')
                plot_date=datetime.strftime(date_object, '%m/%d')
                dates.append(plot_date)
                prices.append(float(row[4]))
                line_count += 1

        dates=list(reversed(dates))
        prices=list(reversed(prices))

        plt.plot(dates, prices)

        plt.xlabel('Date')

        plt.ylabel('Price')

        plt.title(symbol + " Daily Close")

        plt.show()
