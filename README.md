# PyPoll with Python

## Overview of the Election Audit

### A Colorado Board of Elections employee has requested an election audit of a recent congressional election. The election results were from three counties and three candidates with almost 379,000 votes recorded. The winner of the election as well as the county with the greatest voter turnout was collected.

## Election Audit Results

- Total vote count 

    ![total](./Resources/total_votes.png) 
- County level votes count and percentages

     ![county results](./Resources/county_votes.png)    
- Largest turnout

     ![county turn out](./Resources/Largest_turnout.png)   
- Candidate level vote count and percentages

     ![candidate results](./Resources/candidate_results.png)   
- Final election results

     ![final results](./Resources/election_results.png)   

### Code analysis
####
- Total vote count was obtained by reading every row in the election_data.csv file. The total_votes counter was initialized to 0 and then updated as each new row was looped through (skipping the header row).
```python
# Initialize a total vote counter.
total_votes = 0
.
.
.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
```
####
- County level votes count were collected in a dictionary. The totals were summed over the distinct county names. Within each county the percentage of the total votes was calculated.
```python
# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

    # For each row in the CSV file.
    for row in reader:

        # 3: Extract the county name from each row.
        county_name = row[1]

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
.
.
.
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        cvotes = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        cvote_percentage = float(cvotes) / float(total_votes) * 100
```
- Largest turnout was obtained from the county level percentages. The winning county was initialized to an empty string. The winning turnout and county votes were initialized to zero. Winning county, votes and percentages were updated by comparing to the best results.

```python
# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_turnout= 0
cwinning_percentage = 0

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (cvotes > winning_turnout) and (cvote_percentage > cwinning_percentage):
            winning_turnout = cvotes
            winning_county = county_name
            cwinning_percentage = cvote_percentage
```
- Candidate level vote count and percentages were calculated with the same syntax used as with county level results.

- Final election results were calculated as were the county level turnout results.

All results were printed to the terminal as well as saved in the election_analysis.txt file.

## Election Audit Summary

### These anlyses gave a nice summary of the three counties and candidates. Without any any adjustment to the code, a complete list of all counties and many more candidates could be perfomed. The layout of the csv file would be the same. It would then include rows with ballot IDs for more counties and candidates voted for in those counties. The printed and outputed code would have more rows of county level votes and percentages. The Turnout winner would be calculated and displayed in the same way. A new list of more candidates and their corresponding votes and percentages would be a longer table, but the winning candidate results would be in the same format. 
` `  
### There are opportunities to expand the code for future election audit needs. A column of party affiliation could be added to the CSV file if the Board of Elections wanted data on final results by party affiliation. Instead of county, the new list element would be party. It would be indexed with a 3 indicating its location in the new 4th column for party. The same syntax for winning candidate could be used to collect the unique party names and calculate the total votes and percentages. I added a new column to the csv file to test the code. I assigned Stockhom and Degette to Dem and Doane to Rep. Below is the modified code and the new output.

```python
party_options = []
party_votes = {}

winning_party = ""
pwinning_turnout= 0
pwinning_percentage = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1

        party_name = row[3]

        if party_name not in party_options:
            party_options.append(party_name)
            party_votes[party_name] = 0
        party_votes[party_name] += 1

    for party_name in party_votes:
        pvotes = party_votes.get(party_name)
        pvote_percentage = float(pvotes) / float(total_votes) * 100

        party_results_forterminal = (f"{party_name}: {pvote_percentage:.1f}% ({pvotes:,})")
        party_results_fortxt = (f"{party_name}: {pvote_percentage:.1f}% ({pvotes:,})\n")
        print(party_results_forterminal)

        txt_file.write(party_results_fortxt)

        if (pvotes > pwinning_turnout) and (pvote_percentage > pwinning_percentage):
            pwinning_turnout = pvotes
            winning_party = party_name
            pwinning_percentage = pvote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    winning_party_summary = (
        f"\n-----------------------------\n"
        f"Largest Party Turnout: {winning_party}\n"
        f"-----------------------------\n")
    print(winning_party_summary)

    txt_file.write(winning_party_summary)
```
### New party results
![party results](./Resources/party_results.png)   

` `  
### An expanded election audit could include the number registered voters for each of the counties. Currently the voter turnout is based on the percent of total votes. In this case the county with the largest population would always have the highest "turnout" (e.g. Hennepin county will always have the largest number of votes out of the total votes in MN). Ideally, it should be calculated based on the number of registered voters in each county and not out of the total for the state. So now let's include a new column to the CSV file (indexed at 4 now) that has number of registered voters in each county. Again, as with county there will be lots of duplicate values per county. So the code would have to be modified to add a key and value to the new reg_voters dictionary. I think the code below may do this (or else it's close).

```python
# 1: Create a county list and county votes dictionary.
regvote_options = []
regvote_voters = {}

    # For each row in the CSV file.
    for row in reader:

        # 3: Extract the county voters from each row.
        county_regvoters = row[4]

    # For each row in the CSV file.
    for row in reader:

        # 3: Extract the county name from each row.
        county_name = row[1]

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            regvote_options.append(county_name)

            # 4c: Begin tracking the county's registered voters.
            regvote_voters[county_name] = county_regvoters
```
### Now loop through the dictionary of registered voters by county to get the new county level percent turnout.
```python
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in regvote_voters:

        # 6b: Retrieve the county reg voter count.
        voters = regvote_voters.get(county_name)

        # 6c: Calculate the percentage of registered votes for the county.
        voter_percentage = float(voters) / float(county_regvoters) * 100

         # 6d: Print the county results to the terminal.
        voters_results = (f"{county_name}: {voter_percentage:.1f}% ({voters:,})")
        print(voters_results)
```



#### GIS 