# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare the empty list for candidate options
candidate_options = []
# Declare the empty dictionary for candidate votes
candidate_votes = {}

# Create a county list and county votes dictionary
county_list = []
county_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Largest county and largest county voter turnout tracker
largest_county_turnout = ""
largest_voter_turnout = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes +=1
    
        # Print the candidate name from each row
        candidate_name = row[2]

        # Print the county name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            
            # Start tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #If the county does not match any existing county
        if county_name not in county_list:
            # Add the county name to county list
            county_list.append(county_name)
            
            # Start tracking that county's vote count
            county_votes[county_name] = 0
        
        # Add a vote to that county's vote count
        county_votes[county_name] +=1

    # Save results to text file
    with open(file_to_save, "w") as txt_file:
    
    # Print final vote count    
        election_results = (
            f"\nElection Results\n"
            f"---------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------\n")
        print(election_results, end="")
        
        # Save the final vote count to text file
        txt_file.write(election_results)

        # Iterate through county dictionary
        for county in county_votes.keys():
            #Retrieve the county vote count
            county_vote_count = county_votes[county]
                
            #Calculate the percent of total votes for the county
            county_vote_percentage = (float(county_vote_count / float(total_votes) * 100))

            # Print the county results
            county_results = (f"{county}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")

            # Determine the country with the greatest vote count
            if (county_vote_count > largest_voter_turnout):
                largest_voter_turnout = county_vote_count
                largest_county_turnout = county
            print(county_results)

            # Save the county votes to text file
            txt_file.write(county_results)
        
        # Print the county with the largest vote count and its vote count
        largest_county_turnout_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {largest_county_turnout}\n"
            f"-------------------------\n")
        print(largest_county_turnout_summary)

        # Save the county with the largest turnout to a text file
        txt_file.write(largest_county_turnout_summary)

        # Determine the percentage of votes for each candidate by looping through counts
        # Iterate through the candidate list
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes
            vote_percentage = (float(votes) / float(total_votes) * 100)
            # Format percentage to one decimal place
            vote_percentage = round(vote_percentage,1)

            # Print each candidate's election results
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)

            # Save the results to text file
            txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the vote is greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = # vote_percentage
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage
        
        # Print Winner Summary
        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage: .1f}%\n"
            f"------------------------\n")
        print(winning_candidate_summary)
        # Save winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)