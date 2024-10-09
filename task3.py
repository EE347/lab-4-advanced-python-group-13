
for _ in range(3):
        name = input("What is your name?: ")
        with open('/home/pi/ee347/lab-4-advanced-python-group-13/task3.txt', 'a') as file:
            file.write(name + '\n')
        print(f"{name} has been added to task3.txt")
