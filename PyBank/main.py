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
last = 0
changesSum = 0

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
        
        sum += val

        if last != 0:
            changesSum += val - last
        

        #Update max/min values
        if val - last > max:
            max = val - last
            maxMonth = row[0]
        if val - last < min:
            min = val - last
            minMonth = row[0]
        last = val
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total}")
print(f"Total: ${sum}")
print(f"Average Change: ${round(changesSum/(total-1),2)}")
print(f"Greatest Increase In Profits : {maxMonth} (${max})")
print(f"Greatest Decrease in Profits: {minMonth} (${min})")

output_path = os.path.join("analysis","results.txt")
f = open(output_path,"w")
f.write("Financial Analysis\n")
f.write("------------------------------\n")
f.write(f"Total Months: {total}\n")
f.write(f"Total: ${sum}\n")
f.write(f"Average Change: ${round(changesSum/(total-1),2)}\n")
f.write(f"Greatest Increase In Profits : {maxMonth} (${max})\n")
f.write(f"Greatest Decrease in Profits: {minMonth} (${min})\n")
