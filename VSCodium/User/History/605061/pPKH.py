def main():
    file_name = input()
    start_date = input()
    n_days = int(input())

    day, month, year = [int(x) for x in start_date.split(".")]

    i = 0
    while i < n_days:
        i += 1
        pass