year=int(input("Enter a year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")
# The code checks if a given year is a leap year or not. A year is a leap year if it is divisible by 4, but not divisible by 100, unless it is also divisible by 400.