from datetime import datetime, timedelta, date
from collections import defaultdict
from pprint import pprint 


def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days=diff_days)

def prepare_birthday(text:str):
    bd = datetime.strptime(text, '%d, %m, %Y')
    return bd.replace(year=datetime.now().year).date()

def get_birthdays_per_week(users):

    birthdays = defaultdict(list)

    today = datetime.now().date()

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)
   

    happy_users = [user for user in users if start_period <= prepare_birthday(user['birthday']) <= end_period]
   

    for user in happy_users:
        current_bd = prepare_birthday(user['birthday'])
        if current_bd.weekday() in (5,6):
            birthdays['Monday'].append(user['name'])
        else: 
            birthdays[current_bd.strftime('%A')].append(user['name'])

    return birthdays


if __name__ == "__main__":

    users = [{"name": "Oleksandr", "birthday": "27, 3, 1985"},
             {"name": "Mykola", "birthday": "28, 3, 1980"},
             {"name": "Dmytro", "birthday": "29, 3, 1982"},
             {"name": "Petro", "birthday": "30, 3, 1970"},
             {"name": "Oleksii", "birthday": "25, 3, 1985"},
             {"name": "Pavlo", "birthday": "25, 3, 1981"},
             {"name": "Igor", "birthday": "26, 3, 1989"},
             {"name": "Vadim", "birthday": "26, 3, 1984"}]
    
    
    result = get_birthdays_per_week(users)
    pprint(result)

