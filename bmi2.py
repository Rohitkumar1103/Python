weight= input("Enter you weight ")
height = input("Enter your height ")

weightAsInt = int(weight)
heightAsFloat = float(height)

bmi2=  (weightAsInt) / (heightAsFloat **2)
bmi =  round(bmi2)

if bmi < 18.5:
  print(f" Your BMI is {bmi},You  are underweight.")
elif 18.5 < bmi < 25:
    print(f" Your BMI is {bmi},You have a normal weight")
elif 25 < bmi < 30:
   print(f" Your BMI is {bmi},You are slightly overweight")
elif 30 < bmi < 35:
   print(f" Your BMI is {bmi},You are obese")
else:
   print(f" Your BMI is {bmi},You are clinically obese.")