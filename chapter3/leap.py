# 윤년 판정
year = int(input("type a year : "))
if (year % 4 == 0 and year % 100 != 0):
    print(year, "is leap year")
else:
    print(year, "is not a leap year1")
