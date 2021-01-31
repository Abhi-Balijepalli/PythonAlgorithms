# Author: Abhi Balijepalli
# Date: 1/30/2020
# Description: Check if a year given is leap year

# To run the file: python3 python3 leap_year.py

def leapyear():
    year = input("Please enter a year, and i will tell you if its a leap year or not: ")
    if int(year) < 0 or int(year) is None:
        print("Invalid Input \n")
        return leapyear()
    if int(year) % 4 == 0 and int(year) % 100 != 0:
        print (year, "is a leap year")
        return
    if int(year) % 100 == 0 and int(year) % 400 == 0:
        print (year, "is a leap year")
        return
    else:
        print(year, "is not a leap year")
        return
 
if __name__ == "__main__":
    leapyear()