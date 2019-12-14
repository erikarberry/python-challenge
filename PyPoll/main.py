#!/usr/bin/env python3
#Import modules
import os
import csv

#set path/file/object
election_data_csv = os.path.join("election_data.csv")

#Define/set parameters and variables
def print_data(election_data_csv):
    total_votes = 0
    candidates = []
    candidate_vote_count = []
    candidate_vote_percent = []
#Open the CSV and store contents in the variable csvreader
    with open(election_data_csv, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)

        #Loop through each row
        for row in csvreader:
            #Calculate total number of votes cast
            total_votes += 1
            #Form conditional to list unique candidate names
            if row[2] not in candidates:
                candidates.append(row[2])
                index = candidates.index(row[2])
                candidate_vote_count.append(1)
            else:
                index = candidates.index(row[2])
                candidate_vote_count[index] += 1
        print("candidates: " + str(candidates))
        print("candidate_vote_count: " + str(candidate_vote_count))

        #Calculate the percentage of votes each candidate received
        for votes in candidate_vote_count:
            percent = (votes/total_votes) * 100
            percent = round(percent)
            percent = "%.3f%%" % percent
            candidate_vote_percent.append(percent)
        print("candidate_vote_percent: " + str(candidate_vote_percent))
        
        #Calculate the winner of the election based on popular vote
        winner = max(candidate_vote_count)
        index = candidate_vote_count.index(winner)
        winner = candidates[index]
        print("max votes: " + str(winner))

    #Print
        print("Election Results")
        print("————————————————————————————-")
        print("Total Votes: " + str(total_votes))
        print("————————————————————————————-")
        for i in range(len(candidates)):
            print(f"{candidates[i]}: {str(candidate_vote_percent[i])} ({str(candidate_vote_count[i])})")
        print("————————————————————————————-")
        print("Winner: " + str(winner))
        print("————————————————————————————-")

print_data(election_data_csv)