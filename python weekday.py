# Created by: Brian Shortiss
# Created on: 16 February 2020

# Write a program that outputs whether or not today is a weekday.

# Sources:
# https://www.codespeedy.com/how-to-find-day-name-from-date-in-python/
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
# https://stackoverflow.com/questions/38063300/php-if-elseif-else-for-day-and-time

import datetime
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursady', 'Friday']
now = datetime.datetime.now().strftime('%A')
if now in weekday:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")


#day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
#print (day_name[now])
#day = datetime.datetime.weekday()
# print(now)
#print (date)

#import datetime
# datetime_object = datetime.datetime.now()
# print(datetime_object)
