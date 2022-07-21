# basics
for i in range(1, 151):
    print(i)

# Multiples of 5
for x in range(5, 1001, 5):
    print(x)

# Counting, the dojo way
def counting_dojo():
    for y in range (1,101):
        if y % 5 == 0:
            print ('Coding')
        if y % 10 == 0:
            print ('Dojo')
        else:
            print (y)

counting_dojo()

# Whoa. That sucker's huge
maximum = int(500000)
total = 0

for number in range(1, maximum+1):
    if(number % 2 == 0):
        total = total + number

print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))

# Countdown by Fours
def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
count_down_four() 

# Flexible Counter
def flex_countdown(low, high, mult):
    for a in range (low, high):
        if a % mult == 0:
            print (a)
            
flex_countdown(2, 9, 3)