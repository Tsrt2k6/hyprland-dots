while True:
    option = int(input())
    if option == 1:
        with open("diary.txt", "a") as file:
            entry = input()
            file.write(f"{entry}\n")
            print("Dairy saved")
    elif option == 2:
        with open("diary.txt") as file:
            for line in file:
                print(line)
    elif option == 0:
        print("Bye now!")
        break
