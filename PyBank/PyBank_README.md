This program creates a Python script for analyzing the financial records of a company.

The budget data CSV file is opened in both read and write modes and is read in to the program with csv.DictReader into an ordered dictionary.

Variables are set to handle the counting of months, total amount of profits and losses, tracking month-to-month changes, and identifying the months with greatest increases and decreases in profits.

A for loop is used to iterate over the dataset to make the calculations.

All results are then printed to the terminal and to a file.