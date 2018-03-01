import csv
import datetime

# Create the output file
output_txt = open('prices.txt', 'w')
output_txt.write('Time' + " " + 'Price\n')
priceList = []



def convertDateTimeFormat(filepath):
    with open(filepath, 'rt') as csvfile:
        pricereader = csv.reader(csvfile, delimiter = " ", quotechar = '|')

        for row in pricereader: # For each row, get the information
            list = row[0].split(',')
            epochTime = list[0]
            price = float(list[1])
            priceList.append(price)

            # Convert the time from epoch to proper format for the text file
            convertTime = datetime.datetime.fromtimestamp(1347517370).strftime('%c')
            output_txt.write(convertTime + " " + str(price) + "\n")

# Open and convert the input file
convertDateTimeFormat('prices_sample.csv')