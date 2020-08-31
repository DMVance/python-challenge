#!/usr/bin/env python3
# This program creates a Python script for analyzing the financial records of your company.

import os, csv, pprint

path = os.path.join("Resources", "budget_data.csv")
OUT_PATH = os.path.join("analysis", "analysis.txt")
OUT_HEADER = [
    "Date",
    "Profits/Losses",
    "Change",
    "Max",
    "Min"
]

print("Financial Analysis")
print("---------------------------") # is there a report formatting way to do this?

with open(path, "r") as file:

    csv_reader = csv.reader(file)  # using csv.reader() gives me the data in list format already. No need to manually split/strip to clean the data.
    
    header = next(csv_reader) # reads and exhausts first line, the header line, so the next block can deal with the actual data
#     print(header)
    
    data = list(csv_reader) # Remember: this is for calcs in aggregate and when dataset is relatively small. For large datasets, use the iterator to go line by line.
#     print(data)             # see 8/26 class at ~13-min mark
    
#     next(csv_reader) #- necessary when not using data = list(csv_reader)
    
    tot_months = 0    # Improve with a list comprehension?
    total = 0         # This for loop works well because I'm doing calculations on the data in aggregate(?). For line-by-line calcs, will need a different method.
    for row in data:  # Use this with next(csv_reader) for large datasets to calc line-by-line, rather than data = list(csv_reader) with print(data). see 8/26 class at ~13-min mark
#         print(row)
        tot_months += 1
        total += int(row[1])
    print(f"Total months: {tot_months}")
    print(f"Total: ${total}\n")
    
with open(path, "r") as file:
    
    reader = csv.DictReader(file)    # Try DictReader again...
    data = list(reader)
#     print(data)
   
    avg_change = 0
   
    #change = []
    
    for row in data:
        #print(dict(row))
        row = dict(row)
        row["Change"] = (row["Profits/Losses"] - )
    
    avg_change =    
    
    print(f"Average Change: ${avg_change}")
    
with open(path, "r") as file:    # Try to do both max and min in "change" block
    Date = 0
    greatest_incr = 0
    
    # Use a Max() function on the newly-created Change column
    
    print(f"\nGreatest Increase in Profits: {Date} (${greatest_incr})")
    
with open(path, "r") as file:
    Date = 0
    greatest_decr = 0
    
    # Use a Min() function on the newly-created Change column
    
    print(f"Greatest Decrease in Profits: {Date} (${greatest_decr})")
                     
# header = file.readline()  # Switch to csv.reader to clean the data and eliminate the strip/split work.
#     data = file.readlines()
#     cleandata = [row.strip().split(",") for row in data]
#     change = [profit[date + 1] - profit[date] for date, profit in cleandata]
#     print(change)
#     data = dict(csv.DictReader(file))
    
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
