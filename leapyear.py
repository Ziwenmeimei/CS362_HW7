def isLeap(y):
    if y%400 == 0:
        return "Leap year"
    else:
        return "Not leap year"


year = int(input("Enter a year:"))
print(isLeap(year))