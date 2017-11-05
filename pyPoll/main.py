import os
import csv
csvpath = 'election_data_2.csv'

tot_counter = 0
candidate = ""
candiVotes = []
candiWinner = []
candiNames = []
candidate_counter = 0
candiPercent = 0
firstRow = True

#First calculate total rows in the file 
with open(csvpath, newline='') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=',')
    for row in csvreader1:
        tot_counter = tot_counter + 1

#Calculations of votes for each candidate
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if firstRow:
            candidate = row[2]
            firstRow = False
        candidate_counter = candidate_counter + 1
        if row[2] != candidate:
            candiPercent = round((candidate_counter/tot_counter) * 100, 1)
            candiVotes.append(candidate + " : " + str(candiPercent) + "%  (" + str(candidate_counter) + ")")
            candiNames.append(candidate)
            candiWinner.append(candidate_counter)
            candidate_counter = 0
            candidate = row[2]
    #include last counter of votes in the list
    candiVotes.append(row[2] + " : " + str(round((candidate_counter/tot_counter) * 100, 1)) + "%  (" + str(candidate_counter) + ")")  

# print results to terminal
print("Election Results")
print("-------------------------------")
print("Total Votes: " + str(tot_counter))
print("-------------------------------")
for candi in candiVotes:
    print(candi)
print()
winner = 0
i=0
for cw in candiWinner:
    if cw > winner:
        winner = cw
        i = candiWinner.index(cw)
print("-------------------------------")
print("Winner is " + candiNames[i])   
print("-------------------------------")

#print results to a file
output_file = os.path.join("elections.csv")
with open(output_file, "w", newline="") as datafile:
    datafile.write("Total Votes: " + str(tot_counter) + '\n')
    datafile.write("--------------------------------" + '\n')
    for candi in candiVotes:
        datafile.write(str(candi) + '\n')
    datafile.write("-------------------------------\n")
    datafile.write("Winner is " + candiNames[i] + '\n')   
    datafile.write("-------------------------------\n")


