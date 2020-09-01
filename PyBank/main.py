#!/usr/bin/env python3
# This program creates a Python script for analyzing the financial records of your company.

import os, csv, pprint

path = os.path.join("Resources", "budget_data.csv")
OUT_PATH = os.path.join("Analysis", "analysis.txt")

with open(OUT_PATH, "w+") as out_file:
    
    print("Financial Analysis")
    out_file.write("Financial Analysis")
    print("---------------------------")
    out_file.write("---------------------------")

with open(path, "r") as file, open(OUT_PATH, "w+") as out_file:

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
    out_file.write(f"Total months: {tot_months}\nTotal: ${total}\n")
    
with open(path, "r") as file, open(OUT_PATH, "w+") as out_file:
    
    reader = csv.DictReader(file)
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
        c = int(profit[i+1]) - int(profit[i])
        change.append(c)
        i += 1
#     print(change)
    avg_change = round((sum(change) / len(change)), 2)

    print(f"Average Change: ${avg_change}")
    out_file.write(f"Average Change: ${avg_change}")

with open(path, "r") as file, open(OUT_PATH, "w+") as out_file:
    
    reader = csv.DictReader(file)
    data = list(reader)
#     print(data)
#     greatest_incr = max(change)
    zip_change = list(zip(data, change))
#     print(type(zip_change))
#     [print(e) for e in zip_change]
    print(zip_change[20])
    #[dict(row) for row in zip_change]
    #print(row)
    date_greatest_incr = 0
    greatest_incr = 0
    for e in zip_change:
        if zip_change[2] == greatest_incr:
            date_greatest_incr = data["Date"]
#     date_greatest_incr = 0
#     for k, v in data.items():
#         if v == greatest_incr:
#             date_greatest_incr = data["Date"]

#     change_dict = [dict(e) for e in change]
#     print(change_dict)    

    print(f"\nGreatest Increase in Profits: {date_greatest_incr} (${greatest_incr})")
    out_file.write(f"\nGreatest Increase in Profits: {date_greatest_incr} (${greatest_incr})")
    
with open(path, "r") as file, open(OUT_PATH, "w+") as out_file:
#     greatest_decr = min(change)
    greatest_decr_date = 0
    greatest_decr = 0
#     for k, v in data.items():
#         if v == greatest_decr:
#             greatest_decr_date = data["Date"]
    print(f"Greatest Decrease in Profits: {greatest_decr_date} (${greatest_decr})")
    out_file.write(f"Greatest Decrease in Profits: {greatest_decr_date} (${greatest_decr})")
                     
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