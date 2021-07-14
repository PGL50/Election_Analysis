# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of canditates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. THe winner of the election based on the popular vote

import csv
import os

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

# To do: perform analysis.
   print(election_data)

# Close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
#outfile.write("Hello World")

    # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver ," )
    # txt_file.write("Jefferson")
    txt_file.write("Counties in the Election\n------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()
txt_file.close()