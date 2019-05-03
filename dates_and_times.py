#!/usr/bin/env python

import time
print(time.tzname)

# print("starting...", end='', flush=True)
# time.sleep(1.5)
# print('done')

#  8/14/2012
from datetime import date, timedelta

isabelle_bd = date(2012, 8, 14)
today = date.today()

print(isabelle_bd, today)

elapsed = today - isabelle_bd

years, days = divmod(elapsed.days, 365)

print("Isabelle is {} years and {} days old".format(
    years, days
))

two_weeks = timedelta(14, 7200)

then = today + two_weeks

print(then)

