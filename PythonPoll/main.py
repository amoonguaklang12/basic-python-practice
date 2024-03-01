# Dependencies
import os
import csv

# Reading the csv file
par_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(par_dir, "Resources", "election_data.csv")

with open(file_path, "r", newline='') as csvfile:

    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    row_count = 0
    voter_dict = {}
   
   # Determining candidate pool and tallying votes
    for row in csvreader:
        row_count += 1
        if row[2] not in voter_dict.keys():
            voter_dict[row[2]] = 0
        if row[2] in voter_dict.keys():
            voter_dict[row[2]] += 1

# Writing analysis to text file
output_path = os.path.join(par_dir, "Analysis", "analysis.txt")
with open(output_path, "w", newline='') as writer:
    writer.write("Election Results")
    writer.write("\n" + "-" * 22)
    writer.write("\nTotal Votes: " + str(row_count))
    
    max = 0
    for key in voter_dict:
        writer.write(f"\n{key}: {round(100*voter_dict[key]/row_count, 3)}% ({voter_dict[key]})")
        if voter_dict[key] > max:
            max = voter_dict[key]
            winner = key
        
    writer.write("\n" + "-" * 22)
    writer.write("\nWinner: " + winner)
    writer.write("\n" + "-" * 22)

# Displaying analysis to terminal
with open(output_path, "r") as textfile:
    lines = textfile.read()
    print(lines)