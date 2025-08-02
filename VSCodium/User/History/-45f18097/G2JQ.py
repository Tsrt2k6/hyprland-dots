while True:
    editor = input().lower()
    if editor == "Visual Studio Code":
        print("an excellent choice!")
        break
    elif editor == "Word" or editor == "Notepad":
        print("awful")
    else:
        print("not good")
