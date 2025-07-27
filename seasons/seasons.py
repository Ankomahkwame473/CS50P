from datetime import date
import operator
import sys
import inflect
p = inflect.engine()

class Today_date:
    def __init__(self,todaydate):
        self.todaydate = todaydate
    def __str__(self):
        return f"{self.todaydate}"

def main():
    birthday = get_birthdate()
    todaydate = str(get_todaydate()).split("-")
    byear,bmonth,bday = birthday[0:]
    tyear,tmonth,tday = todaydate[0:]
    date_of_birth = date(int(byear),int(bmonth),int(bday))
    today_date = date(int(tyear),int(tmonth),int(tday))
    if date_of_birth > today_date:
        sys.exit("Invalid date")
    diff = convert_bdate_to_days(today_date, date_of_birth)
    days_in_min = diff * 1440
    num_to_words = p.number_to_words(days_in_min)
    num_to_words = num_to_words.replace(" and","").capitalize()
    print(f"{num_to_words} minutes")

def convert_bdate_to_days(today_date, date_of_birth):
    diff = operator.sub(today_date, date_of_birth)
    diff = diff.days
    return diff


def get_birthdate():
    try:
        birthday = input("Date of Birth: ")
        if "-" not in birthday:
            sys.exit("Invalid date")
        birthday = birthday.split("-")
        if len(birthday[0]) != 4:
            sys.exit("Invalid date")
        if int(birthday[1]) > 12:
            sys.exit("Invalid date")
        if int(birthday[2]) > 31:
            sys.exit("Invalid date")
    except ValueError:
        sys.exit("Invalid date")
    return birthday

def get_todaydate():
    todaydate = date.today()
    return Today_date(todaydate)

if __name__ == "__main__":
    main()
