import datetime
import calendar

time = datetime.datetime.now()
print("Current date and time: ", time)

year = int(input("Enter a year: "))
print("Entire calendar for ", year, ":")
print(calendar.calendar(year))