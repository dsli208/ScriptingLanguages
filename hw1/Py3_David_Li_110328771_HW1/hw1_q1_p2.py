import csv

# Create the output file
output_txt = open('prices.txt', 'w')
output_txt.write('Time' + " " + 'Price\n')

def getPriceList(filepath):
    priceList = []

    with open(filepath, 'rt') as csvfile:
        pricereader = csv.reader(csvfile, delimiter = " ", quotechar = '|')
        totalPrice = 0

        for row in pricereader: # For each row, get the information
            list = row[0].split(',')
            epochTime = list[0]
            price = float(list[1])
            priceList.append(price)

            # Convert the time from epoch to proper format for the text file
            #convertTime = datetime.datetime.fromtimestamp(1347517370).strftime('%c')
            #output_txt.write(convertTime + " " + str(price) + "\n")

            # Add price to totalPrice, as a means of calculating mean price
            totalPrice += price


        # After creating the text file, move to part 2 - mean, min, max, and std. dev.
        #print(priceList)
        meanPrice = totalPrice / len(priceList)
        minPrice = min(priceList)
        maxPrice = max(priceList)
        # calculate standard deviation
        sigmatotal = 0
        for n in priceList:
            sigmatotal += (n - meanPrice)**2
        sigmatotal /= len(priceList)
        sigmatotal = sigmatotal**(0.5)
        # The line of sigmatotal above, when finished is the standard deviation

        print("Mean: ", meanPrice)
        print("Min: ", minPrice)
        print("Max: ", maxPrice)
        print("Standard Deviation: ", sigmatotal)

getPriceList('prices_sample.csv')