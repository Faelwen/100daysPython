print("Welcome to the tip calculator.")
bill_total = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage would you like to give? 10,12, or 15? "))
number_people = int(input("How many people to split the bill? "))

final_bill = round(bill_total * (1 + percentage_tip/100) / number_people, 2)
final_bill_formatted = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${final_bill_formatted}")
