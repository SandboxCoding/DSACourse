#First usage of if and else
a = int(3)
b = int(2)
ab = a*b

if ab == 6:
    print("Success")
else:
    print("Failure")

#Trying some random thing
month = int(input("Enter a month in numeric form from 1-12: "))

if month in list(range(1, 3)):
    print("It's the first quarter of the month.")
elif month in list(range(4, 6)):
    print("It's the second quarter of the month.")
elif month in list(range(6, 9)):
    print("It's the third quarter of the month.")
elif month in list(range(10, 12)):
    print("It's the fourth quarter of the month.")
else:
    print("The number", month, "does not correspond to a valid month.")

