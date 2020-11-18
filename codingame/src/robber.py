'''

we are working as an inspector and there is this special box wich records the time, id, and state each time it is oppened and closes
so, the log entries for this box looks like this:

    "20:14 2344 1"  -> "time id state"
    
    time:   means the log time in format HH:mm 24 hours:minutes
    id:     id of the guy who opnes or close the box
    state:  1 for open / 0 for close

    from this data we must choose who was the robber

    The robbery happened beween 20:00 and 08:00!

    between (8pm) 1200 minutes and (12pm) 1440

    from (0hours)0 minutes to (8am)480

'''

def look_for_robber():

    n = int(input())

    robber_id = ''
    employees = {}

    for i in range(n):
        time, id, state = input().split(' ')

        hours, minutes = list(map(int,time.split(':')))

        time_in_minutes = (hours * 60 ) + minutes

        happen_in_midnight = time_in_minutes >= 1200 and time_in_minutes <= 1440
        hapend_early_in_morning = time_in_minutes >= 0 and time_in_minutes <= 480

        if happen_in_midnight or hapend_early_in_morning:
            if not id in employees:
                employees[id] = []
            
            employees[id].append(state)

    for suspect, log in employees.items():
        last_action = log.pop()
        if last_action == '1':
            robber_id = suspect
            break

    return robber_id
