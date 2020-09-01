import csv, os, pprint

path = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("---------------------------")

with open(path, "r") as file:
    
    csv_reader = csv.reader(file)  # switch to dictreader
    
    header = next(csv_reader) 
    print(header)
    
    #data = list(csv_reader)
    tot_votes = 0
    candidates = []
    for e in csv_reader:    # see 8/26 class at ~13-min mark
        if e[2] not in candidates:
            candidates.append(e[2])
        tot_votes += 1
    print(f"Total votes: {tot_votes}\n")
    print(candidates)

print("---------------------------\n")

with open(path, "r") as file:
    
    csv_reader = csv.DictReader(file)
    
    #count number of votes by candidate
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    for e in csv_reader:    # see 8/26 class at ~13-min mark
        if e[candidate] = "Khan":
            Khan_votes += 1
        elif e[candidate] = "Correy":
            Correy_votes += 1
        elif e[candidate] = "Li":
            Li_votes += 1
        else:
            OTooley_votes += 1
    
    Khan_pct = 
    Correy_pct =
    Li_pct = 
    OTooley_pct =
    
    print(f"Khan: {}% ({Khan_votes})")
    print(f"Correy: {}% ({Correy_votes})")
    print(f"Li: {}% ({Li_votes})")
    print(f"O'Tooley: {}% ({OTooley_votes})")
    
print("---------------------------")   
print("Winner: { }")
print("---------------------------")
