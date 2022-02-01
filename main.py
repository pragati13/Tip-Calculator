#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.")
bill_amt = input("What was the total bill? $")
tip_percent = input("How much tip would you like to give? 10, 12, or 15?")
no_of_people = input("How many people to split the bill?")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
# bill_amt1 = bill_amt[1:]



percent_to_num = 1 + (int(tip_percent)/100)

contri = (float(bill_amt) / int(no_of_people)) * percent_to_num

contri1 = round(contri,2)

print(f"Each person should pay: ${contri1}")
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇