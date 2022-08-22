import os
import csv
import statistics

# Path to collect data from the Resources folder
os.chdir(os.path.dirname(__file__))

#Initialise values
total = 0
sum = 0
max = 0
min = 0
maxMonth = ""
minMonth = ""
changesList = []

# Open File
csv_path = os.path.join("Resources","budget_data.csv")
with open(csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:
        #Update totals
        total += 1
        val = int(row[1])
        changesList.append(val)
        sum += val

        #Update max/min values
        if val> max:
            max = val
            maxMonth = row[0]
        if val < min:
            min = val
            minMonth = row[0]
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total}")
print(f"Total: ${sum}")
print(f"Average Change: ${int(statistics.mean(changesList))}")
print(f"Greatest Increase In Profits : {maxMonth} (${max})")
print(f"Greatest Decrease in Profits: {minMonth} (${min})")

output_path = os.path.join("analysis","results.txt")
f = open(output_path,"w")
f.write("Financial Analysis\n")
f.write("------------------------------\n")
f.write(f"Total Months: {total}\n")
f.write(f"Total: ${sum}\n")
f.write(f"Average Change: ${int(statistics.mean(changesList))}\n")
f.write(f"Greatest Increase In Profits : {maxMonth} (${max})\n")
f.write(f"Greatest Decrease in Profits: {minMonth} (${min})\n")