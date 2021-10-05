height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / (height**2))
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif 18.5 < bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif 25 < bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif 30 < bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
