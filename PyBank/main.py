#First thing is to import the libraries we will be using for the challenge
import os
import csv

#Then we state the file we will be using
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Declare the variables we wil be using in this case several lists
total_months = []
total_profit = []
monthly_profit_change = []

#open the file we will be using and reading from
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #This establishes the csv file to have a header
    header= next(csv_reader)        

    #We use For in order to go through each row and count the number of rows which would also be the months and storing the amount for each row
    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #We will use this For loop to figure out the change between previous month and current month ad adding that change in profit or loss in another list
    for x in range(len(total_profit)-1):

        monthly_profit_change.append(total_profit[x+1]-total_profit[x])  


    #We will use these variables to have the mac profit/loss change and greatest decrease in profit
    max_increase_value = max(monthly_profit_change)
    max_decrease_value = min(monthly_profit_change)
   
    #This is used to figure out the month in which the greatest increase and decrease of profit came from
    max_increase_month= monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_decrease_month= monthly_profit_change.index(min(monthly_profit_change)) + 1

    #This will be the section of stuff we need to print
    print("Financial Analysis")
    print("--------------------------")
    
   # The total number of months included in the dataset
    print (f'Total Months: {len(total_months)}')

    # The net total amount of "Profit/Losses" over the entire period
    print (f'Total: ${sum(total_profit)}')

    print(f'Average Change:${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}')

    # Greatest Increase in Profits:
    # Greatest Decrease in Profits: 
    print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(max_increase_value)})")
    print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(max_decrease_value)})")
    

     
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output_file = os.path.join("analysis","financial_analysis.txt")

with open(output_file, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("--------------------------\n")
    
   # The total number of months included in the dataset
    txt_file.write (f'Total Months: {len(total_months)}\n')

    # The net total amount of "Profit/Losses" over the entire period
    txt_file.write (f'Total: ${sum(total_profit)}\n')

    # The average changes in "profit/Losses" over the entire period
    txt_file.write(f'Average Change:${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n')

    # Greatest Increase in Profits:
    # Greatest Decrease in Profits: 
    txt_file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(max_increase_value)})\n")
    txt_file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(max_decrease_value)})\n")