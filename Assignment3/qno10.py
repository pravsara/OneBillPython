import datetime
import calendar
def findDay(date):
	born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
	return (calendar.day_name[born])
date = '04 02 2019'
print(findDay(date))
