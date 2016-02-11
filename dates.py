# ------------------------------------------------- Date Methods ------------------------------------------------- ....
from datetime import date,timedelta
import time
import calendar

def actualmonth(months):
    '''This method checks the current month and 
     return with the name of the month .'''
    for i in range(1, 13):
        if time.localtime()[1] == i:
            return months[i]
			
def actualyear():
    return time.localtime()[0]
	
def maketimeformat(hour, min):
    '''This method call the expand withzero 
     method and call concatenate.'''
    h = ExpandWithZero(hour)
    m = ExpandWithZero(min)
    return concatenate(h, m)


def ExpandWithZero(Number):
    '''This expands the time expression 
     where only one digit numbers found  
     ex: 7:7 will be 07:07'''
    Number = (str(Number) if Number > 9 \
    else '0' + str(Number))
    return Number


def concatenate(hour, min):
    '''Concatenate the seperated mins and hours '''
    Result = str(hour) + ':' + str(min)
    return str(Result)

# Creating a method what can calculate the period of workdays in the current month

	

def date():
    year = str(time.localtime()[0])
    month = ExpandWithZero(time.localtime()[1])
    day = ExpandWithZero(time.localtime()[2])
    return str(year + '.' + month + '.' + day)

def firstdayofmonth():
	year = str(time.localtime()[0])
	month = ExpandWithZero(time.localtime()[1])
	day = '01'
	return str(year + '.' + month + '.' + day)

def worktimecalc(
    inhour,
    inmin,
    outhour,
    outmin,
    Meal,
    ):
    ''' This section will calculate the working mins
       and hours.The return value will be a tuple object 
       what you neeeded to seperate after call'''
    StartTime = inhour * 60 + inmin
    EndTime = outhour * 60 + outmin
    Duration = EndTime - StartTime
    if Meal == 'i':
        Duration -= 30
    work_time_hour = Duration / 60
    work_time_min = Duration % 60
    return (work_time_hour, work_time_min)

	
def mintotime(min):
    data_hours = 0
    if min < 0:
        sign = '- '
        min = abs(min)
    else:
        sign =''
    if min > 60:
        plus_hours = min / 60
        min = min % 60
        data_hours += plus_hours
        return sign + maketimeformat(data_hours, min)
    else:
        return sign + maketimeformat(0, min)  
    
	
def whatday(date):
    if date:
        datetime = date.group(3)
        year = int(datetime.split('.')[0])
        month =int( datetime.split('.')[1])
        day = int(datetime.split('.')[2])
        whatday = calendar.weekday(year,month,day)
        return whatday

