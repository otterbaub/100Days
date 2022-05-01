# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

intAge = int(age)
intYearT = 90

intYrRem = intYearT - intAge
intDayRem = str(intYrRem * 365)
intWeekRem = str(intYrRem * 52)
intMonRem = str(intYrRem * 12)

print(f"You have {intDayRem} days, {intWeekRem} weeks, and {intMonRem} months left." )
