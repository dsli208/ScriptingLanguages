import csv
import datetime

# Create the output file
output_txt = open('prices.txt', 'w')
output_txt.write('Time' + " " + 'Price\n')
priceList = []

# Open the input file
with open('prices_sample.csv', 'rt') as csvfile:
    pricereader = csv.reader(csvfile, delimiter = " ", quotechar = '|')
    totalPrice = 0

    for row in pricereader: # For each row, get the information
        list = row[0].split(',')
        epochTime = list[0]
        price = float(list[1])
        priceList.append(price)

        # Convert the time from epoch to proper format for the text file
        convertTime = datetime.datetime.fromtimestamp(1347517370).strftime('%c')
        output_txt.write(convertTime + " " + str(price) + "\n")

        # Add price to totalPrice, as a means of calculating mean price
        totalPrice += price

    # After creating the text file, move to part 2 - mean, min, max, and std. dev.
    mean = totalPrice / len(priceList)
    min = min(priceList)
    max = max(priceList)
    # calculate standard deviation
    sigmatotal = 0
    for n in priceList:
        sigmatotal += (n - mean)**2
    sigmatotal /= len(priceList)
    sigmatotal = sigmatotal**(0.5)
    # The line of sigmatotal above, when finished is the standard deviation

    print("Mean: ", mean)
    print("Min: ", min)
    print("Max: ", max)
    print("Standard Deviation: ", sigmatotal)