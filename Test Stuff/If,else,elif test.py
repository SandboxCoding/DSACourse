#First usage of if and else
a = int(3)
b = int(2)
ab = a*b

if ab == 6:
    print("Success")
else:
    print("Failure")

#Trying some random things
month = int(input("Enter a month in numeric form from 1-12: "))

if month in list(range(1, 4)):
    print("It's the first quarter of the month.")
elif month in list(range(4, 7)):
    print("It's the second quarter of the month.")
elif month in list(range(7, 10)):
    print("It's the third quarter of the month.")
elif month in list(range(10, 13)):
    print("It's the fourth quarter of the month.")
else:
    print("The number %s does not correspond to a valid month." %(month))