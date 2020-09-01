import csv, os

path = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("---------------------------")

with open(path, "r") as file:
    
    csv_reader = csv.reader(file)  # switch to dictreader
    
    header = next(csv_reader) 
#     print(header)
    
    #data = list(csv_reader)
    tot_votes = 0
    candidates = []
    for e in csv_reader:    # see 8/26 class at ~13-min mark
        if e[2] not in candidates:
            candidates.append(e[2])
        tot_votes += 1
    print(f"Total votes: {tot_votes}\n")
#     print(candidates)

print("---------------------------\n")

with open(path, "r") as file:
    
    csv_reader = csv.DictReader(file)
    next(csv_reader)
    
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    for e in csv_reader:    # see 8/26 class at ~13-min mark
        if e["Candidate"] == "Khan":
            Khan_votes += 1
        elif e["Candidate"] == "Correy":
            Correy_votes += 1
        elif e["Candidate"] == "Li":
            Li_votes += 1
        else:
            OTooley_votes += 1
    
    Khan_pct = Khan_votes / tot_votes
    Correy_pct = Correy_votes / tot_votes
    Li_pct = Li_votes / tot_votes
    OTooley_pct = OTooley_votes / tot_votes
    
    print(f"Khan: {Khan_pct}% ({Khan_votes})")
    print(f"Correy: {Correy_pct}% ({Correy_votes})")
    print(f"Li: {Li_pct}% ({Li_votes})")
    print(f"O'Tooley: {OTooley_pct}% ({OTooley_votes})")
    
print("---------------------------")   
print("Winner: { }")
print("---------------------------")
