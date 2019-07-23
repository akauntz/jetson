import csv
import re
import requests

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def stock_reader(symbol):
    with open('packer/trends/'+symbol+'.csv') as csv_file_trend:
        csv_reader_trend = csv.reader(csv_file_trend, delimiter=',')
        line_count = 0
        dates_trend = []
        prices_trend = []
        for row in csv_reader_trend:
            if line_count < 3:
                line_count += 1
            elif line_count == 3:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif line_count<25:
                day=row[0]
                date_object = datetime.strptime(day, '%Y-%m-%d')
                plot_date=datetime.strftime(date_object, '%m/%d')
                dates_trend.append(plot_date)
                prices_trend.append(float(row[1])/100+7)
                #print(f'{row[0]} Close: {row[1]}')
                line_count += 1


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
                #print(f'{row[0]} Close: {row[4]}')
                line_count += 1
            #print(f'Processed {line_count} lines.')
        dates=list(reversed(dates))
        prices=list(reversed(prices))

        # plotting the points
        plt.plot(dates, prices)
        plt.plot(dates, prices_trend)
        # naming the x axis
        plt.xlabel('Date')
        # naming the y axis
        plt.ylabel('Price')

        # giving a title to my graph
        plt.title(symbol + " Daily Close")

        # function to show the plot
        plt.show()
