""" https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

Exercise example:
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later) """
def add_time(user_input, added_time, input_weekday = False):

    #First block : current time
    input_hour = int(user_input.split(":")[0])
    input_minute = int(user_input.split(":")[1].split()[0])
    am_pm = user_input.split(":")[1].split()[1].lower()

    #second block : added time
    added_hour = int(added_time.split(":")[0])
    added_minute = int(added_time.split(":")[1])

    #logic
    result_minutes = (input_minute+added_minute)%60
    result_hour = input_hour + added_hour + (input_minute+added_minute)//60

    if am_pm == "pm":
        am_pm = 1
    else:
        am_pm = 0

    days_gone = (result_hour + am_pm * 12)//24 #days gone calculation

    if (result_hour//12 + am_pm)%2 == 0:
        am_pm = "AM"
    else:
        am_pm = "PM"

    result_hour = result_hour%12 #calculating first if AM or PM before converting hour into 12 division

    if result_hour == 00: #if hour is at 00, it has to be shown as 12 
        result_hour = 12

    #week day calculation
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if input_weekday != False:
        input_weekday = input_weekday.lower()
        result_weekday = (week_days.index(input_weekday) + days_gone)%7
        result_weekday = week_days[result_weekday].capitalize()
    
    #output
    result_str = f"{result_hour}:{result_minutes:0>2} {am_pm}"
    
    if input_weekday != False:
        result_str += f", {result_weekday}"

    if days_gone != 0:
        if days_gone == 1:
            result_str +=" (next day)"
        else:
            result_str +=f" ({days_gone} days later)"

    return result_str