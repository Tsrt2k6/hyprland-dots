from datetime import datetime, timedelta

def main():
    file_name = input()
    start_date = input()
    n_days = int(input())

    day, month, year = [int(x) for x in start_date.split(".")]
    start_date = datetime(year, month, day)
    time = timedelta(1)

    i = 0
    while i < n_days:
        i += 1
        