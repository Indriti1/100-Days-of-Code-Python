# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
difference = 90 - age_as_int


months_left = difference * 12
weeks_left = difference * 52
days_left = difference * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")