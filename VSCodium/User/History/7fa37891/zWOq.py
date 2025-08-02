name = input()
file_name = input()

with open(file_name, "w") as file:
    file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")