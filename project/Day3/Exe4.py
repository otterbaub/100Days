# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0
small = 15
med = 20
large = 25
pepSm = 2
pep = 3



if size == 'S':
    total = total + small

if size == 'M':
    total = total + med

if size == 'L':
    total = total + large

if add_pepperoni == 'Y':
    if size == 'S':
        total = total + pepSm
    else:
        total = total + pep
if extra_cheese == 'Y':
    total += 1

print(f'Your final bill is: ${total}.')