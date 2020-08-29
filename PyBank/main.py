#!/usr/bin/env python3
# This program 

import os, csv, pprint

path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "analysis.txt")

# manually make your own csv reader
with open(path, "r") as file:

    header = file.readline()
    print("This is the header: \n")
    print(header)
    
    print("This is the data: \n")
    tot_months = 0          # Improve with a list comprehension
    for line in file:
        tot_months += 1
        print(line.strip())

print(f"Total number of months: {tot_months}")

# another way to strip newline chars and split into list format
with open(path, "r") as file:
    print([row.strip().split(",") for row in file]) #strips off newline chars from each item in list

# use csv module to read the file and separate header from data
with open(path, "r") as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)       # better for small datasets or when it's more efficient to read in whole dataset to work with
    print(header)                   # can iterate over dataset later
    data = list(csv_reader)         # use this one for PyBank
    pprint.pprint(data)    
    
    #for row in csv_reader:         # better for dealing with large datasets, read one line at a time
    #    print(row)                 # use this one for PyPoll                 

# use DictReader from csv module to take each row and move into a list of dictionaries (rather than a list of lists), preserving header info for each line
with open(path, "r") as file:
    

#print("File is open") if not in_file.closed else print("File is closed")
    #data = in_file.readlines()
    #print(data)

    #print(type(header))
    #print(type(data))

    # data has headers, so use csv.DictReader(file)? Or skip header?
    #csv_reader = csv.reader(in_file)
    #data = list(csv_reader)

    # Next, iterate over contents of file, line by line, and perform appropriate operation to obtain the desired outcomes listed below
    #months = 0
    #months = [months += 1 for months in data]

    #total_months = a count of the mumber of rows
    #net_total_profit_losses = sum of Profit/Losses column
    #avg_changes_profit_losses = calculate month to month changes in new column and take avg over entire period
    #greatest_increase_profits_(date/amount over entire period) = max of new column, provide month and value
    #greatest_decrease_losses_(date/amount over entire period) = min of new column, provide month and value
#print(months)
#print(data)

#with open(path, "w+") as out_file:
#
#    # establish name of output file?
#
#    print("Financial Analysis\n")
#    print("-------")
#    print(f"Total Months: {total_months}\n")
#    print(f"Total: ${total}\n")
#    print(f"Average Change: ${avg_change}\n")
#    print(f"Greatest Increase in Profits: {date} (${greatest_increase_profits})\n")
#    print(f"Greatest Decrease in Profits: {date} (${greatest_decrease_losses})\n")
#
#    csv.writer(txtfile)
#
#    print(analysis)
