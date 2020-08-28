import os, csv

path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'analysis.txt')

with open(path, "r") as file:



    #total_months = a count of the mumber of rows
    #net_total_profit_losses = sum of Profit/Losses column
    #avg_changes_profit_losses = calculate month to month changes in new column and take avg over entire period
    #greatest_increase_profits_(date/amount over entire period) = max of new column, provide month and value
    #greatest_decrease_losses_(date/amount over entire period) = min of new column, provide month and value

with open(path, "w+") as file:

    # establish name of output file?

    print("Financial Analysis\n")
    print("-------")
    print(f"Total Months: {total_months}\n")
    print(f"Total: ${total}\n")
    print(f"Average Change: ${avg_change}\n")
    print(f"Greatest Increase in Profits: {date} (${greatest_increase_profits})\n")
    print(f"Greatest Decrease in Profits: {date} (${greatest_decrease_losses})\n")

    csv.writer(txtfile)

    print(analysis)
