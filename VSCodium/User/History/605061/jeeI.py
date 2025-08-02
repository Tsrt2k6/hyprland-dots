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
        date_list.append(f"{str(date_add.day).zfill(2)}.{str(date_add.month).zfill(2)}.{date_add.year}")
        i += 1

    with open(file_name, "w") as file:
        file.write(f"Time period: {date_list[0]}-{date_list[-1]}\n")
        file.write(f"Total minutes: {total}\n")
        file.write(f"Average minutes: {total / n_days}\n")
        for index in range(n_days):
            file.write(f"{date_list[index]}: {minutes_list[index]}\n")


main()