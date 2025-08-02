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
    minutes_list = []
    i = 0
    while i < n_days:
        minutes = input()
        minutes_list.append(minutes.replace(" ", "/"))
        total += sum([int(x) for x in minutes.split(" ")])
        date_add = start_date + timedelta(i)
        date_list.append(f"{date_add.day}.{date_add.month}.{date_add.year}")
        i += 1

    print("Time period:", start_date + "-" + date_list[-1])
    print("Total minutes:", total)
    print("Average minutes:", total / n_days)
    for index in range(n_days):
        print(date_list[index], minutes_list[index])


main()