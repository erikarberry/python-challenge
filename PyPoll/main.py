#Import modules
import os
import csv

#set path/file/object
election_data_csv = os.path.join("election_data.csv")

#Define/set parameters and variables
def print_data(election_data_csv):
    total_votes = 0
    candidate_unique = []
    candidate_vote_count = []
    candidate_vote_percent = []
    max_vote = 0

#Open the CSV and store contents in the variable csvreader
with open(election_data_csv), newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)

    #Loop through each row
    for row in csvreader:
        VoterID = str(row[0])
        county = str(row[1])
        candidate = str(row[2])
        #Calculate total number of votes cast
        total_votes = total_votes + 1
        print("total_votes:" + str(total_votes))
        #Form conditional to list unique candidate names
        if candidate in candidate_unique:
            candidate_index = candidate_unique.index(candidate)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            candidate_unique.append(candidate)
            candidate_vote_count.append(1)
        print("candidate_unique:" + str(candidate_unique))

        #Calculate the percentage of votes each candidate received
        for i in range(len(candidate_unique)):
            percent = round(candidate_vote_count[i]/total_votes*100, 2)
            candidate_vote_percent.append(percent)
            print("candidate_vote_percent:" + str(candidate_vote_percent))
    #Calculate the winner of the election based on popular vote
            if candidate_vote_count[i] > candidate_vote_count[0]:
                max_vote = candidate_vote_count[i]
                print("max votes:" + str(candidate_vote_count[i])

#Print
print("Election Results")
print("————————————————————————————-")
print("Total Votes:" + str(total_votes))
print("————————————————————————————-")
#print canddiate name: percent won (number)
#print canddiate name: percent won (number)
#print canddiate name: percent won (number)
#print canddiate name: percent won (number)
print("————————————————————————————-")
#print("Winner: + str(winner)")
print("————————————————————————————-")

print_data(election_data_csv)