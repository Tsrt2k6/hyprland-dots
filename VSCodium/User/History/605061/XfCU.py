from datetime import datetime, timedelta

def main():
    file_name = input()
    start_date = input()
    n_days = int(input())

    day, month, year = [int(x) for x in start_date.split(".")]
    start_date = datetime(year, month, day)
    time = timedelta(n_days)
    period = start_date + time

    total = 0
    date_list = []
    i = 0
    while i < n_days:
        date = input()
        total += sum([int(x) for x in date.split(" ")])
        date_list.append(start_date + timedelta(i))
        