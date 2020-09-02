This program modernizes the vote counting process of a small, rural town.

The election data CSV file is opened in both read and write modes and is read in to the program with csv.reader.

Since the file is large, the contents are iterated over line by line to perform operations.

An empty list is initialized to store the instance of each vote for each candidate.

The Counter function, imported from the collections library (a part of the Python Standard Library), is used to count the number of each vote for each candidate and the results are stored in a dictionary with the candidate name as the key and the vote count as the value.

The winner's name, the key of the vote count dictionary, is retrieved using the max value function based on the highest value in the dictionary.

All results are then printed to the terminal and to a file, with calculation for the % of total votes received for each candidate.