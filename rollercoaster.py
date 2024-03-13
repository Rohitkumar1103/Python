print("Welcome to RollerCoaster!!")
height = int(input("What is your height in cm??"))
bill =0

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age<12: 
    bill = 5
    print("Child pay $5")
  elif 12 <= age < 18:
    bill= 7
    print("Youth pay $7")
  elif age >=45 & age <=55:
    print("You get a free ride")
  else:
    bill = 12
    print("Adult pay $12")

  photo= input("Do you want to take photo? (yes/no)")

  if photo == "yes":
    bill +=3
    print(f"Your final bill is ${bill}")

else:
  print("You need to grow taller to ride the rollercoaster")