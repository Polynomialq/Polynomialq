age = input("What is your current age?\n")
ageLeft = 90 - int(age)
days = ageLeft * 365
weeks = ageLeft * 52
months = ageLeft * 12
print(f"You have {days} days, {weeks} weeks or {months} months left.")
