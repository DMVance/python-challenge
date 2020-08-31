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
#     my_dict = dict(data)
#     profit_loss = my_dict["Profit/Losses"]
#     pprint.pprint(profit_loss)
    profit_loss = []
    for row in data:
        row = dict(row)
#         print(row)
        profit_loss.append(row["Profit/Losses"])
#         while i < int(len(profit_loss)) - 1:
#             change.append(int(profit_loss[i+1]) - int(profit_loss[i]))
            
#     pprint.pprint(profit_loss)
#     print(change[0:2])
#     print(type(profit_loss[1]))
    profit = [int(e) for e in profit_loss]
#     print(type(profit[1]))

    change = []
    i = 0
    for e in profit[:-1]:
#     while i <= (len(profit) - 1):    
        c = int(profit[i+1]) - int(profit[i])
        change.append(c)
        i += 1
                
    avg_change = sum(change) / len(change)

    print(f"Average Change: ${avg_change}")
    
    greatest_incr = max(change)
    greatest_incr_date = 
    print(f"\nGreatest Increase in Profits: {date} (${greatest_incr})")
    
    greatest_decr_date = 
    greatest_decr = min(change)
    print(f"Greatest Decrease in Profits: {date} (${greatest_decr})")
    
# with open(path, "r") as file:    # Try to do both max and min in "change" block
#     Date = 0
#     greatest_incr = max(change)
    
#     # Use a Max() function on the newly-created Change column
    
#     print(f"\nGreatest Increase in Profits: {Date} (${greatest_incr})")
    
# with open(path, "r") as file:
#     Date = 0
#     greatest_decr = min(change)
    
#     # Use a Min() function on the newly-created Change column
    
#     print(f"Greatest Decrease in Profits: {Date} (${greatest_decr})")
                     
# header = file.readline()  # Switch to csv.reader to clean the data and eliminate the strip/split work.
#     data = file.readlines()
#     cleandata = [row.strip().split(",") for row in data]
#     change = [profit[date + 1] - profit[date] for date, profit in cleandata]
#     print(change)
#     data = dict(csv.DictReader(file))


# with open(path, "r") as file:
    
#     reader = csv.DictReader(file)    # Try DictReader again...
#     #print(reader)
# #     for row in reader:
# #         print(row['Date'], row['Profit/Losses'])
# #         print(dict(row))
    
# #     pprint.pprint([dict(ordered_dict) for ordered_dict in reader])
# #     avg_change = 0 #change / tot
# #     tot = 0 
# #     #i = 0
#     changed = list(reader)
#     change = int(changed[0]['Profit/Losses'])
# #     change_list = []
#     next(reader)
#     for row in reader:    # Want to ignore the first value in Profit/Losses column. Use only for calculating change to next row.
#         change = int(row['Profit/Losses']) - change
#         change_list.append(change)
#         #i += 1
#         tot += 1
#     pprint.pprint(change_list)
# #     change = [profit[date + 1] - profit[date] for date, profit in file]
# #     for line in data:
# #         tot += 1
# #         profit = int(data[line]["Profit/Losses"]
# #         print(profit)
        
# #     print(f"Average Change: ${avg_change}")