import os, csv

path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'analysis.txt')

with open(path, "r") as file:



    #total_months
    #net_total_profit_losses
    #avg_changes_profit_losses
    #greatest_increase_profits_(date/amount over entire period)
    #greatest_decrease_losses_(date/amount over entire period)

with open(path, "w+") as file:

    print("Financial Analysis\n")
    print("-------")
    print(f"Total Months: {total_months}\n")
    print(f"Total: ${total}\n")
    print(f"Average Change: ${avg_change}\n")
    print(f"Greatest Increase in Profits: {date} (${greatest_increase_profits})\n")
    print(f"Greatest Decrease in Profits: {date} (${greatest_decrease_losses})\n")

    csv.writer(txtfile)

    print(analysis)
