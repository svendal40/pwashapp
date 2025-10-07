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

# gets input from user does not save input and does not allow for extra information on specific dates except busy atribute
import calendar
from datetime import datetime, timedelta

atributes = {}


today = datetime.now().date()
day = today + timedelta(days = 14)
day_list = []
status = "free"
def bomboclat(x,y):
  while x <= y:
    day_list.append(x.day)
    x = x + timedelta(days = 1)
bomboclat(today, day)

print (day_list)
new_cal = day_list



final_busy_days = []

final_cal = []

total_busy_days = []

begenning_cal = []





def get_busy_inputs():
  CLI = input("input client busy days")
  client_busy = []
  busy = []
  #data grabber for client busy days
  cool_list = ""
  for char in CLI:
    if char != ",":
       cool_list = cool_list + (char)
    elif char == ",":
      client_busy.append(cool_list)
      cool_list = ""
  #data grabber for use busy days
  UI = input("enter user busy days")
  bad_list = ""
  for char in UI:
    if char != ",":
       bad_list = bad_list + (char)
    elif char == ",":
      busy.append(bad_list)
      bad_list = ""
  add_lists(busy,client_busy)
  type_switcher(total_busy_days)
  cool_thing(new_cal)
  
  
def type_switcher(x):
  for item in x:
    final_busy_days.append(int(item))
    
   
      

  




def add_lists(x,y):
  for dayx in x:
    if dayx not in y:
      total_busy_days.append(dayx)
  for dayY in y:
    if dayY not in x:
      total_busy_days.append(dayY)

 


def cool_thing(x):
  
  for item in x:
    if item in final_busy_days:
      final_cal.append("busy")
      
    else:
      final_cal.append(item)
  for words in final_cal:
    print(f"{words}th : {atributes}")
  
  

get_busy_inputs()