import calendar
import jobs
import employees
import bleach
import client
import pricing
import utils
from datetime import datetime, time, date
from collections import defaultdict
import datetime


now = datetime.datetime.now()
current_year = now.year
current_month = now.month



cal = calendar.monthcalendar(current_year, current_month)






    


def schedule_job(self, job, day, client, busy_days, client_busy, calendar):
    
    both_busy = list(set(busy_days) & set(client_busy))
    print(both_busy)  # checks for equal values and returns to both_busy
    free_days = [for days in cal if cal not in both_busy]
    print(cal) 
    
    
    
    choice =  input("day of week")
    verdict = list(set)


