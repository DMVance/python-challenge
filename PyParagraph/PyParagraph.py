import os, re, string
from collections import Counter


path = os.path.join("raw_data", "paragraph_1.txt")

with open(path, "r") as file, open(path, "w+") as out_file:
    
    paragraph_1 = file.read()
        
    words = 0
    sentences = 0
    avg_letters = 0
    avg_sentence = 0
    
    
    # for counting words
    
    
    # for counting sentences
    
    
    # for counting letters in words and taking average
    
    
    # for counting words in a sentence (determining sentence length) and taking average
    re.split("(?<=[.!?]) +", paragraph_1)
