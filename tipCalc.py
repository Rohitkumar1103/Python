print("Welcome to Tip Calculator")

bill = float(input("What was the total Bill?$"))

tip = int(input("What percentage tip would you give? 10, 12, or 15?  "))   

people = int(input("How many people to slipt the bill"))

bill_with_tip = tip/100 * bill + bill
print(bill_with_tip)

bill_per_person = bill_with_tip /people
final_amount= round(bill_per_person,2)

print("Each person has to pay : $", final_amount)
