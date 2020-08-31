import csv, os, pprint

path = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("---------------------------")

with open(path, "r") as file:
    
    csv_reader = csv.reader(file)  
    
    header = next(csv_reader) 
    
    data = list(csv_reader) 
    tot_votes = 0    
    for e in data: 
        tot_votes += 1
    print(f"Total votes: {tot_votes}\n")
print("---------------------------\n")
   
    
    
    
print("---------------------------")   
print("Winner: { }")
print("---------------------------")
