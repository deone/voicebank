import datetime

def calculate_age(born):
    today = datetime.date.today()
    try:
	birthday = born.replace(year=today.year)
    except ValueError:
	birthday = born.replace(year=today.year, day=born.day-1)

    return today.year - born.year
