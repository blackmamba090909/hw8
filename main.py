from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if users == []:
        return {}
    else:
        dict_with_birthday = dict()
        current_date = date.today()

        for user in users:
            birthday = user.get("birthday")
            names = user.get("name")
            names = names.split(" ")
            birthday = birthday.replace(year=current_date.year)
            if birthday < current_date:
                birthday = birthday.replace(year=(current_date.year + 1))
            if birthday >= current_date and birthday <= current_date + timedelta(days=7):
                day_name =  birthday.strftime("%A")
                if day_name in ("Monday", "Saturday", "Sunday"):
                    day_name = "Monday"
                dict_with_birthday.setdefault(day_name, [])
                dict_with_birthday[day_name].append(names[0])
                
                
        
        return dict_with_birthday

res = get_birthdays_per_week([
    {"name": "Jan Koum", "birthday": datetime(1976, 9, 20).date()},
    {"name": "Anastasia Bondarenko", "birthday": datetime(2003, 9, 16).date()}
])

print(res)

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
