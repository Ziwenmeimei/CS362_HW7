def isLeap(y):
    if y%400 == 0:
        return "Leap year"
    elif y%100 == 0:
        return "Not leap year"        
    else:
        return "Not leap year"


year = int(input("Enter a year:"))
print(isLeap(year))