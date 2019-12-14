#!/usr/bin/env python 3
#Import modules
import os
import csv

#Set path/file/object
budget_data_csv = os.path.join("budget_data.csv")

#Define/set parameters and variables
def print_data(budget_data_file):
	count_month = 0
	revenue = 0
	total_revenue = 0
	month_change = 0
	previous_month_revenue = 0
	greatest_increase = 0
	greatest_decrease = 0
	#Open the CSV and store contents in the variable csvreader
	with open(budget_data_file, newline="") as csvfile:
		csvreader = csv.reader(csvfile, delimiter=",")
		csv_header = next(csvreader)
		print(csv_header)
	#Loop through each row and add an element to list (pull out the index of the item selected)	 
		for row in csvreader:
			month = str(row[0])
			print("month:" + str(month))
			revenue = int(row[1])
			print("revenue:" + str(revenue))
	#Calculate total number of months
			count_month = count_month + 1
			print("count_month:" + str(count_month))
	#Calculate net total amount of revenue
			total_revenue = total_revenue + revenue
			print("total_revenue:" + str(total_revenue))
	#Calculate month to month revenue change (calcluate a list in a variable, then iterate and append the column’s data to the list)
			if count_month > 1:
				month_change = month_change + (previous_month_revenue - revenue)
				previous_month_revenue = revenue
			else:
				previous_month_revenue = revenue
			print("month_change:" + str(month_change))
			if (count_month > 2):
				print("month_change/count:" + str(month_change/(count_month)))
	#Calculate the greatest increase in revenue and include date
			if month_change > greatest_increase:
				greatest_increase = month_change
			print("greatest_increase:" + str(greatest_increase))
	#Calculate greatest decrease in revenue and include date
			if month_change < greatest_decrease: 
				greatest_decrease = month_change
			print("greatest_decrease:" + str(greatest_decrease))
	# Print 
	print("Financial Analysis")
	print("————————————————————————————-")
	print("Total Months: " + str(count_month))
	print("Total: $" + str(total_revenue))
	print("Average Change: $" + str(month_change/count_month))
	print("Greatest Increase in Profits: " + str(month) + " $" + str(greatest_increase))
	print("Greatest Decrease in Profits: " + str(month) + " $" + str(greatest_decrease))
	#Specify the file to write to
	output_path = os.path.join("Financial_Analysis.txt")
	# Open the file using "write" mode. Specify the variable to hold the contents
	with open(output_path, 'w', newline='') as output_file:
		output_file.write("Financial Analysis")
		output_file.write("\n")
		output_file.write("————————————————————————————-")
		output_file.write("\n")
		output_file.write("Total Months: " + str(count_month))
		output_file.write("\n")
		output_file.write("Total: $" + str(total_revenue))
		output_file.write("\n")
		output_file.write("Average Change: $" + str(month_change/count_month))
		output_file.write("\n")
		output_file.write("Greatest Increase in Profits: " + str(month) + " $" + str(greatest_increase))
		output_file.write("\n")
		output_file.write("Greatest Decrease in Profits: " + str(month) + " $" + str(greatest_decrease))
		output_file.write("\n")
print_data(budget_data_csv)