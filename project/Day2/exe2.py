# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


intHeight = float(height)
intWeight = float(weight)

intSqrHeight = (intHeight * intHeight)
intBmi = intWeight / intSqrHeight
print(round(intBmi))