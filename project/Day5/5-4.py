#Write your code below this row 👇

numRange = range(1,100)

for val in numRange:
    if val % 3 == 0 and val % 5 == 0:
        print("FizzBuzz")
    elif val % 3 == 0: 
        print("Fizz")  
    elif val % 5 == 0:
        print("Buzz")
    else:
        print(val)
    