size = input("What size pizza do you want? S,M, or L: ")

pepperoni = input("Do you want pepperoni? y/n:")

cheese = input("Do you want cheese? y/n:")
price =0

if size == "s":
  price +=15
elif size == "m":
    price +=20
else:
    price +=25

if pepperoni == "y":
  if size == "s":
      price +=2
  else:
      price +=3

if cheese == "y":
   price +=1

print(f"Your final bill is: ${price}")

