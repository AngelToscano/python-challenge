## PyPoll Challenge
#Import what is needed
import os
import csv


#Then we state the file we will be using and declare variables we will be using
poll_csv = os.path.join('Resources', 'election_data.csv')
candidates = set()
candidate_list = []
total_votes = 0
candidate_count = [0,0,0]
charles_casper = 0
charles_percent = 0.0
diana_degette = 0
diana_percent =0.0
raymon_doane = 0
raymon_percent = 0.0

#Open the file an read it
with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #This establishes the csv file to have a header
    header= next(csv_reader)   
    
    #Go through the rows of the file
    for row in csv_reader:
        
        #First we need to count the total number of votes
        total_votes += 1
        
       
        #This if statement is to add up the amount of candidates' votes
        if row[2] == "Charles Casper Stockham": 
            candidate_count[0] += 1
        elif row[2] == "Diana DeGette":
            candidate_count[1] += 1
        elif row[2] == "Raymon Anthony Doane": 
            candidate_count[2] += 1
            
        #This is to figure out all of the candidates in that had votes
        if (row[2] in candidates):
            continue
        candidates.add(row[2])
        candidate_list.append(row)

    #This is figure out the percentages of each candidate
    charles_percent = candidate_count[0] / total_votes
    diana_percent = candidate_count[1] / total_votes
    raymon_percent = candidate_count[2] / total_votes

    #This is to determine who won
    if candidate_count[0] > candidate_count[1] and  candidate_count[0] > candidate_count[2]:
        winner = "Charles Casper Stockham"
    elif candidate_count[1] > candidate_count[0] and  candidate_count[1] > candidate_count[2]:
        winner = "Diana DeGette"
    elif candidate_count[2] > candidate_count[1] and  candidate_count[2] > candidate_count[0]:
        winner = "Raymon Anthony Doane"
    else:
        winner = "No One Won"
    
    #Print Commands
    print("\nElection Results\n")
    print("---------------------------\n")
    #* The total number of votes cast
    print(f'Total Votes: {str(total_votes)}')
    print("---------------------------\n")
    
    #* A complete list of candidates who received votes
    print(f'This is the list of candidates:\n {candidates}\n')
    
    #* The percentage of votes each candidate won and the total number of votes each candidate won
    print(f'Charles Casper Stockham:{charles_percent:,.3%} ({candidate_count[0]})\n')
    print(f'Diana DeGette: {diana_percent:,.3%} ({candidate_count[1]})\n')
    print(f'Raymon Anthony Doane: {raymon_percent:,.3%} ({candidate_count[2]})\n')
    
    #* The winner of the election based on popular vote.
    print(f'Winner : {winner}')

#we will use to establish where is txt file will go to
output_file = os.path.join("analysis","poll_analysis.txt")

with open(output_file, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("\n---------------------------\n")
    #* The total number of votes cast
    txt_file.write(f'Total Votes: {str(total_votes)}\n')
    txt_file.write("\n---------------------------\n")
    
    #* A complete list of candidates who received votes
    txt_file.write(f'\nThis is the list of candidates:\n {candidates}\n')
    
    #* The percentage of votes each candidate won and the total number of votes each candidate won
    txt_file.write(f'\nCharles Casper Stockham:{charles_percent:,.3%} ({candidate_count[0]})\n')
    txt_file.write(f'Diana DeGette: {diana_percent:,.3%} ({candidate_count[1]})\n')
    txt_file.write(f'Raymon Anthony Doane: {raymon_percent:,.3%} ({candidate_count[2]})\n')
    
    #* The winner of the election based on popular vote.
    txt_file.write(f'\nWinner : {winner}')