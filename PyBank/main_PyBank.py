# This program creates a Python script for analyzing the financial records of a company.

import os, csv

path = os.path.join("Resources", "budget_data.csv")
OUT_PATH = os.path.join("Analysis", "PyBank_analysis.txt")

with open(path, "r") as file, open(OUT_PATH, "w+") as out_file:

    reader = csv.DictReader(file)

    change = []
    tot_months = 0    
    total = 0 
    previous_month = 0
    great_incr_month = 0
    great_decr_month = 0
    great_incr = float('-inf')
    great_decr = float('inf')
    
    for row in reader:
        tot_months += 1
        total += int(row["Profit/Losses"])
        if tot_months == 1:
            previous_month = row["Profit/Losses"]
        else:
            current_change = int(row["Profit/Losses"]) - int(previous_month)
            change.append(current_change)
            previous_month = row["Profit/Losses"]
            if current_change > great_incr:
                great_incr = current_change
                great_incr_month = row["Date"]
            if current_change < great_decr:
                great_decr = current_change
                great_decr_month = row["Date"]
            
    avg_change = round((sum(change) / len(change)), 2)
    
    output_string = f"Financial Analysis\n"\
    f"---------------------------\n"\
    f"Total months: {tot_months}\n"\
    f"Total: ${total}\n"\
    f"Average Change: ${avg_change}\n"\
    f"Greatest Increase in Profits: {great_incr_month} (${great_incr})\n"\
    f"Greatest Decrease in Profits: {great_decr_month} (${great_decr})\n"
    
    print(output_string)
 
    output_file = f"Financial Analysis\n"\
    "---------------------------\n"\
    f"Total months: {tot_months}\n"\
    f"Total: ${total}\n"\
    f"Average Change: ${avg_change}\n"\
    f"Greatest Increase in Profits: {great_incr_month} (${great_incr})\n"\
    f"Greatest Decrease in Profits: {great_decr_month} (${great_decr})\n"
   
    out_file.write(output_file)