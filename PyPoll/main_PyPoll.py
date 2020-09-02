import csv, os
from collections import Counter

path = os.path.join("Resources", "election_data.csv")
OUT_PATH = os.path.join("Analysis", "PyPoll_analysis.txt")

with open(path, "r") as file, open(OUT_PATH, "w+") as out_file:
    
    reader = csv.reader(file)
    header = next(reader)            

    candidate_votes = []
    candidates = []
    
    for row in reader:
        candidate_votes.append(row[2])
    
    vote_count = dict(Counter(candidate_votes))
        
    csv_writer = csv.writer(out_file)
    
    print("Election Results")
    out_file.write("Election Results\n")
    print("------------------------------")
    out_file.write("------------------------------\n")
    print(f"Total Votes: {len(candidate_votes)}")
    out_file.write(f"Total Votes: {len(candidate_votes)}\n")
    print("------------------------------")
    out_file.write("------------------------------\n")
    
    for key, value in vote_count.items():
        print(f"{key}: {round(((value / len(candidate_votes))*100), 2)}% ({value})")
        out_file.write(f"{key}: {round(((value / len(candidate_votes))*100), 2)}% ({value})\n")
    
    print("------------------------------")
    out_file.write("------------------------------\n")
    
    winner = max(vote_count, key=vote_count.get)
    
    print(f"Winner: {winner}")
    out_file.write(f"Winner: {winner}\n")