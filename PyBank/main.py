#!/usr/bin/env python3
# This program creates a Python script for analyzing the financial records of your company.

import os, csv, pprint

path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "analysis.txt")

print("Financial Analysis")
print("---------------------------") # is there a report formatting way to do this?

# use DictReader from csv module to take each row and move into a list of dictionaries (rather than a list of lists), preserving header info for each line
with open(path, "r") as file:
    
    dict_reader = csv.DictReader(file)
    #pprint.pprint([dict(ordered_dict) for ordered_dict in dict_reader])
        
    tot_months = 0           # Improve with a list comprehension?
    for line in dict_reader: # if i had used file instead of dict_reader, it would have counted the header line
        tot_months += 1
    print(f"Total months: {tot_months} \n")

with open(path, "r") as file:

    data = csv.reader(file)

    next(file)
    
    total = 0  # Improve with a list comprehension?
    for line in data:
        #print(line[1])
        total += int(line[1])
    
print(f"Total: ${total}")
    
    # Iterate over contents of file, line by line, and perform appropriate operation to obtain the desired outcomes listed below
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
