# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime
import calendar

def get_dates_weekday(start_date, end_date):
    dt = end_date - start_date
    dates = []

    for i in range(dt.days + 1):
        date = start_date + datetime.timedelta(i)
        if calendar.weekday(date.year, date.month, date.day) < 5:
            dates.append(date)

    return dates

def gen_cal(week_number=None):
    if type(week_number) == type(None):
        today = datetime.date.today() + datetime.timedelta(7)
    else:
        today = datetime.datetime.strptime(week_number+"-1", '%GW%V-%u')
    idx = (today.weekday() + 1) % 7
    sun = today - datetime.timedelta(idx)
    sat = today - datetime.timedelta(idx-6)

    days = get_dates_weekday(sun, sat)

    day_string = []
    day_format = "[{}]({})"
    for tday in days:
        this_date = "Meetings/"+tday.strftime("%Y/%m/%d")
        this_date_short = tday.strftime("%m%d")
        day_string.append( day_format.format(this_date_short, this_date) )

    print ( "| Week", datetime.date(today.year, today.month, today.day).isocalendar()[1],  "|", " | ".join(day_string), "|")


if __name__ == "__main__":
    for weeknum in range(24, 0, -1):
        gen_cal("2020W{}".format(weeknum))
