import os
import time  
def checkTodaysBirthdays():
    fileName = open('C:\\Users\\GANYA\\OneDrive\\Desktop\birthdayfile\a.txt', 'x')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag =1
            os.system('notify-send "Birthdays Today: ' + line[1]
            + ' ' + line[2] + '"')
    if flag == 0:
            os.system('notify-send "No Birthdays Today!"')
  
if __name__ == '__main__':
    checkTodaysBirthdays()
