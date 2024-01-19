print("welcome to the BmI calculator")
weight= int(input("Wjat id your weight? "))
height= float(input("what is your height? "))
BMI= int(weight/height**2)
print(f"Your BMi is {BMI}")
if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5:
        print("normal weight")
elif BMI == 25:
        print("normal weight")
elif BMI > 25:
        print("slightly over weight")
elif BMI == 30:
        print("slightly overweight")
elif BMI > 30:
        print ("Obese")
elif BMI == 35:
        print("Obese")
else:
        print("chronically obese")

 
