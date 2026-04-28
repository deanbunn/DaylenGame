#!/usr/bin/env python3

"""y = 15
r = 7
x = 44
b = 30

if y > r:
    print('Y is greater than r!')

#Check if a number is divisable by another number
if x % b == 0:
    print('it worked')
elif x % b == 1:
    print('very close')
else:
    print('not even close')

"""

"""
lfriends = ["Nathan T", "John", "Jordan","Marcus", "Andrew", "Nathan B", "Kira"]
lfriends.sort()

notFriends = []

print(lfriends)

for f in lfriends:
    if f == "Jordan":
        print(f + ' is a fish')
    elif f == "Andrew":
        print(f + ' is an apple')
    elif f == "Nathan T":
        print(f + " is always late to history")
    elif f == "John":
        print(f + " loves to watch japanese cartoons")
    elif f == "Marcus":
        print(f + " will be removed")
        notFriends.append(f)
    elif f == "Kira":
        print(f + " will get sick")
        notFriends.append(f)
    else:
        print(f + " is a good friend")



for x in notFriends:
    lfriends.remove(x)

lfriends.reverse()
print(lfriends)

"""

name = input("Enter your name:")
age = input("Enter your age:")
city = input("Enter your location, please?:")

nAge = int(age)

if nAge > 10:
    print("you're at least a teenager")


print(f"Hello {name}. You're {age} years old and live in {city}.")

