# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


listName1 = list(name1.lower())
listName2 = list(name2.lower())

t = listName1.count('t') + listName2.count('t')
r = listName1.count('r') + listName2.count('r')
u = listName1.count('u') + listName2.count('u')
e = listName1.count('e') + listName2.count('e')

l = listName1.count('l') + listName2.count('l')
o = listName1.count('o') + listName2.count('o')
v = listName1.count('v') + listName2.count('v')
e = listName1.count('e') + listName2.count('e')

value1 = ( t + r + u + e ) * 10
value2 = l + o + v + e
value = value1 + value2



if value < 10 or value > 90:
    print(f"Your score is {value}, you go together like coke and mentos.")
if value > 40 and value < 50:
    print(f"Your score is {value}, you are alright together.")
elif:
    print(f"Your score is {value}.")

