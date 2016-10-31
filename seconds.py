#!/usr/bin/python
# This is a comment by Holly

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

seconds_in_a_minute = 60
minutes_in_an_hour = 60
hours_in_a_day = 24
days_in_a_week = 7
days_in_a_year = 365

seconds_in_a_day = seconds_in_a_minute * minutes_in_an_hour * hours_in_a_day
seconds_in_a_week = seconds_in_a_minute * minutes_in_an_hour * hours_in_a_day * days_in_a_week
seconds_in_a_year = seconds_in_a_day * days_in_a_year
seconds_in_a_leap_year =seconds_in_a_year + seconds_in_a_day

# locale.format("%d", 99909999998989898, grouping=True)


print("there are " + locale.format("%d", (seconds_in_a_day), grouping=True) + " seconds in a day!")
print("there are " + locale.format("%d", (seconds_in_a_week) , grouping=True) + " seconds in a week!")
print("there are " + locale.format("%d", (seconds_in_a_year), grouping=True)  + " seconds in a year!")
print("there are " + locale.format("%d", (seconds_in_a_leap_year), grouping=True)  + " seconds in a leap year!")

print("there are a tons of seconds in a century!")

print("holy cow!!!!")
# WHATTTT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


####################################################################
# To Do:
# Make the program tell us how many seconds in a week
# Make it tell us how many seconds in a month of 30 days
####################################################################

