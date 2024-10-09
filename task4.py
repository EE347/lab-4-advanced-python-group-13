
filename = '/home/pi/ee347/lab-4-advanced-python-group-13/task3.txt'
    
with open(filename, 'r') as file:
    names = file.readlines()
print("Names read from the file:")
for name in names:
     print(name.strip())