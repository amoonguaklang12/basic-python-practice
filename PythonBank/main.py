# Dependencies
import os
import csv

# Path to csv file
csvpath = os.path.join('.', 'Projects', 'basic-python-practice', 'PythonBank' ,'Resources', 'budget_data.csv')

# Reading data using csv module
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Header of CSV file
    csv_header = next(csvreader)

    # Default Variables
    last_row = [0,1088983]
    num_months = 0
    net_total = 0
    max_increase = 0
    min_increase = 0
    net_changes = 0

    # Iterating through the csv file by row
    for row in csvreader:
       
       num_months += 1
       net_total += int(row[1])
       monthly_change = int(row[1]) - int(last_row[1])
       net_changes += monthly_change

       # Calculating Max Increase and Min Increase
       if monthly_change > max_increase:
           max_increase = monthly_change
           max_row = row
       if monthly_change < min_increase:
           min_increase = monthly_change
           min_row = row
       
       last_row = row

    # Writing Analysis to txt file
    output_path = os.path.join('.', 'Projects', 'basic-python-practice', 'PythonBank', 'Analysis', 'analysis.txt')
    
    with open(output_path, 'w', newline='') as writer:
        writer.write("Financial Analysis")
        writer.write("\n" + "-" * 22)
        writer.write("\nTotal Months: " + str(num_months))
        writer.write("\nTotal: $" + str(net_total))
        writer.write("\nAverage Change: $" + str(round(net_changes/(num_months-1), 2)))
        writer.write("\nGreatest Increase in Profits: " + max_row[0] + " ($" + str(max_increase) + ")")
        writer.write("\nGreatest Decrease in Profits: " + min_row[0] + " ($" + str(min_increase) + ")")
    
