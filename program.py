import time
import random
print(time.ctime())


# Add more task parameters (cycle, date format)

file1 = open("tasks.txt")
content = file1.read()
tasks = content.split("\n")[2:]
for i in range(len(tasks)):
    tasks[i] = tasks[i].split(", ")

# Optmize Random Module
# saveTask = 1
print("Daily Tasks")
for i in range(len(tasks)):
    if int(tasks[i][3]):
        print(tasks[i][0])
    elif (random.randint(0, 1)): # and (saveTask)
        print(tasks[i][0])

# Main Module

# Special Events Module

# Enter new task
def newTask():

# Work on Log


# References
# time: https://www.programiz.com/python-programming/time
# GUI: https://www.pythonguis.com/faq/which-python-gui-library/
# file io: https://www.programiz.com/python-programming/file-operation
# pyinstaller: https://pyinstaller.org/en/stable/