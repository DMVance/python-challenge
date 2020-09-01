#!/usr/bin/env python3
# This program creates a Python script for analyzing the financial records of your company.

import os, csv, pprint

path = os.path.join("Resources", "budget_data.csv")
OUT_PATH = os.path.join("Analysis", "analysis.txt")
    
print("Financial Analysis")
print("---------------------------")

with open(path, "r") as file:

    csv_reader = csv.reader(file)  # using csv.reader() gives me the data in list format already. No need to manually split/strip to clean the data.
    
    header = next(csv_reader) # reads and exhausts first line, the header line, so the next block can deal with the actual data
#     print(header)
    
    data = list(csv_reader) # Remember: this is for calcs in aggregate and when dataset is relatively small. For large datasets, use the iterator to go line by line.
                            # see 8/26 class at ~13-min mark
        
#     next(csv_reader) #- necessary when not using data = list(csv_reader)
    
    tot_months = 0    # Improve with a list comprehension? Can't use += with list comprehension...
    total = 0         # This for loop works well because I'm doing calculations on the data in aggregate(?). For line-by-line calcs, will need a different method.
    for row in data:  # Use this with next(csv_reader) for large datasets to calc line-by-line, rather than data = list(csv_reader) with print(data). see 8/26 class at ~13-min mark
        tot_months += 1
        total += int(row[1])
    print(f"Total months: {tot_months}\nTotal: ${total}\n")
    
with open(path, "r") as file:
    
    reader = csv.DictReader(file)
    data = list(reader)

    profit_loss = []
    for row in data:
        row = dict(row)
        profit_loss.append(row["Profit/Losses"])
#         while i < int(len(profit_loss)) - 1:
#             change.append(int(profit_loss[i+1]) - int(profit_loss[i]))
            
    profit = [int(e) for e in profit_loss]

    change = []
    i = 0
    for e in profit[:-1]:
        c = int(profit[i+1]) - int(profit[i])
        change.append(c)
        i += 1
    avg_change = round((sum(change) / len(change)), 2)
#     print(change)
    
    dict_change = list(dict.fromkeys(change, "Change"))
#     print(dict_change)
    
    print(f"Average Change: ${avg_change}")

with open(path, "r") as file:     # make a dictionary to reference date based on greatest change +/-
    
    reader = list(csv.DictReader(file))
#     data = list(reader)
#     print(data)
#     for row in reader:
#         row = dict(row)
#         print(row)
#     data = dict(reader)
#     data = zip(reader, dict_change)
#     for row in data:
#         print(row)
#     for row in data:
#         print(row)
    
#     zip_change = list(zip(data, change))
#     print(zip_change)
#     for row in zip_change:
#         print(row)

    date_greatest_incr = 0
    greatest_incr = max(change)
    
#     for e in zip_change:
#         if zip_change[1] == greatest_incr:
#             date_greatest_incr = data["Date"]  

    print(f"\nGreatest Increase in Profits: {date_greatest_incr} (${greatest_incr})")
    
with open(path, "r") as file, open(OUT_PATH, "w+") as out_file:

    date_greatest_decr = 0
    greatest_decr = min(change)
#     for k, v in data.items():
#         if v == greatest_decr:
#             greatest_decr_date = data["Date"]
    print(f"Greatest Decrease in Profits: {greatest_decr_date} (${greatest_decr})")
    
    out_file.write("Financial Analysis\n")
    out_file.write("---------------------------\n")
    out_file.write(f"Total months: {tot_months}\nTotal: ${total}\n")
    out_file.write(f"Average Change: ${avg_change}")
    out_file.write(f"\nGreatest Increase in Profits: {date_greatest_incr} (${greatest_incr})\n")
    out_file.write(f"Greatest Decrease in Profits: {date_greatest_decr} (${greatest_decr})\n")

# QUESTIONS:
#     How to reference "date" value based on max(change)? add the "change" data to the Date, Profit/Losses dictionary with "Change" as the key
#     Am i opening the file too many times? if i run a process and exhaust all the lines, must re-open the file...?