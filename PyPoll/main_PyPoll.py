# This program modernizes the vote counting process of a small, rural town.

import csv, os

path = os.path.join("Resources", "election_data.csv")
OUT_PATH = os.path.join("Analysis", "PyPoll_analysis.txt")

with open(path, "r") as file, open(OUT_PATH, "w+") as out_file:
    
    reader = csv.reader(file)
    header = next(reader)            

    candidates = []
    
    for row in reader:
        candidates.append(row[2])
    
    vote_tally = dict((name, candidates.count(name)) for name in set(candidates))
    sorted_tally = dict(sorted(vote_tally.items(), key=lambda x: x[1], reverse=True))    
    
    v = list(sorted_tally.values()) 
    k = list(sorted_tally.keys()) 
    winner = k[v.index(max(v))]
    
    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {len(candidates)}")
    print("------------------------------")
    
    out_file.write("Election Results\n")
    out_file.write("------------------------------\n")
    out_file.write(f"Total Votes: {len(candidates)}\n")
    out_file.write("------------------------------\n")
    
    for key, value in sorted_tally.items():
        print(f"{key}: {round(((value / len(candidates))*100), 2)}% ({value})")
        out_file.write(f"{key}: {round(((value / len(candidates))*100), 2)}% ({value})\n")
    
    print("------------------------------")
    out_file.write("------------------------------\n")
        
    print(f"Winner: {winner}")
    out_file.write(f"Winner: {winner}\n")