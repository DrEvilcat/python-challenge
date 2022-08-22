import os
import csv
import statistics

# Path to collect data from the Resources folder
os.chdir(os.path.dirname(__file__))

#Initialise values
total = 0

namesList = []
resultsDict = {}

# Open File
csv_path = os.path.join("Resources","election_data.csv")
with open(csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #Tally Votes
    for row in csvreader:
        total += 1
        
        thisName = row[2]
        #Add vote and initialise if needed
        try:
            resultsDict[thisName] = resultsDict[thisName] + 1
        except:
            resultsDict[thisName] = 1
            namesList.append(thisName)

firstName = ""
secondName = ""
thirdName = ""
firstCnt = 0
secondCnt = 0
thirdCnt = 0

#Finding first (and second and third) places
for name in namesList:
    if resultsDict[name] > firstCnt:
        thirdName = secondName
        thirdCnt = secondCnt
        secondName = firstName
        secondCnt = firstCnt
        firstName = name
        firstCnt = resultsDict[name]
    elif resultsDict[name] > secondCnt:
        thirdName = secondName
        thirdCnt = secondCnt
        secondName = name
        secondCnt = resultsDict[name]
    elif resultsDict[name] > thirdCnt:
        thirdName = name
        thirdCnt = resultsDict[name]


output_path = os.path.join("analysis","results.txt")
f = open(output_path,"w")
#Print and write results
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {total}")
print("-------------------------------")
f.write("Election Results\n")
f.write("-------------------------------\n")
f.write(f"Total Votes: {total}\n")
f.write("-------------------------------\n")
#Iterate over all entrants
for name in namesList:
    print(f"{name}: {round(resultsDict[name]/total*100,3)}% ({resultsDict[name]})")
    f.write(f"{name}: {round(resultsDict[name]/total*100,3)}% ({resultsDict[name]})\n")
print("--------------------------------")
print(f"Winner: {firstName}")
f.write("--------------------------------\n")
f.write(f"Winner: {firstName}\n")