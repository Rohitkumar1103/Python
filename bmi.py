weight= input("Enter you weight ")
height = input("Enter your height ")

weightAsInt = int(weight)
heightAsFloat = float(height)

bmi=  (weightAsInt) / (heightAsFloat **2)
print ("Your BMI is ", bmi)