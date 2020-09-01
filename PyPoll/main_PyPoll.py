import csv, os

path = os.path.join("Resources", "election_data.csv")
OUT_PATH = os.path.join("Analysis", "analysis.txt")

# TEXT_FILE = "main_PyPoll.txt"

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
    print(f"Total votes: {tot_votes}")
#     print(candidates)

print("---------------------------")

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
    
    Khan_pct = round(((Khan_votes / tot_votes) * 100), 2)
    Correy_pct = round(((Correy_votes / tot_votes) * 100), 2)
    Li_pct = round(((Li_votes / tot_votes) * 100), 2)
    OTooley_pct = round(((OTooley_votes / tot_votes)) * 100, 2)
    
    print(f"Khan: {Khan_pct}% ({Khan_votes})")
    print(f"Correy: {Correy_pct}% ({Correy_votes})")
    print(f"Li: {Li_pct}% ({Li_votes})")
    print(f"O'Tooley: {OTooley_pct}% ({OTooley_votes})")
    
    winner = max(Khan_votes, Correy_votes, Li_votes, OTooley_votes)
    
print("---------------------------")   
print(f"Winner: {winner}")          # change this to write name rather than vote count
print("---------------------------")

# EXPORT TO TEXT FILE
with open(OUT_PATH, "w+") as file:
    
#     csv_writer = csv.writer(file)
    
    file.write("Election Results\n")
    file.write("---------------------------\n")
    file.write(f"Total votes: {tot_votes}\n")
    file.write("---------------------------\n")
    file.write(f"Khan: {Khan_pct}% ({Khan_votes})\n")
    file.write(f"Correy: {Correy_pct}% ({Correy_votes})\n")
    file.write(f"Li: {Li_pct}% ({Li_votes})\n")
    file.write(f"O'Tooley: {OTooley_pct}% ({OTooley_votes})\n")
    file.write("---------------------------\n")   
    file.write(f"Winner: {winner}\n")          # change this to write name rather than vote count
    file.write("---------------------------\n")


# QUESTIONS: 
#     how to format numbers to decimal places
#     best way to get max value and reference another value based on that