import openpyxl, os, datetime, re
from openpyxl import load_workbook
from datetime import date 
from datetime import datetime

if os.path.isfile('/home/anton/repositories/timer/time_stat.xlsx'):
    print('Ok')


def last_string_find():
    pass 

# Взять файл
def take_file():
    global time_file, current_date, last_string
    time_file = load_workbook('/home/anton/repositories/timer/time_stat.xlsx')
    current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    #last_string = str(len(time_file['2023']))





# Место/строка в файле
def correct_date_string():
    current_date = date.today().strftime('%d-%m-%Y')
    pass


# Вывод статистики за 5 дней
def five_days_data():
    pass


# Вывод статистики за 21 день
def twentyone_days_data():
    pass


# Сколько надо потратить времени в минутах
def need_time():
    pass

take_file()


wb = load_workbook('/home/anton/repositories/timer/time_stat.xlsx')

subs = [ ]
sheets = wb['2023']

#print(wb.sheetnames.rows[0])

print(sheets['A'][1].value)




for i in range(1,len(sheets['B'])):
    if sheets['B'][i].value == None:
        print(sheets['B'][i-1].value)
        break 

#print(last_string)
print(current_date)

time_file  = open('/home/anton/repositories/timer/time_stat.xlsx', '+')

#time_file = load_workbook('/home/anton/repositories/timer/time_stat.xlsx')

sheets['B'][8].value = date.today().strftime('%d-%m-%Y')

print(sheets['B'][8].value)

#time_file.save('/home/anton/repositories/timer/time_stat.xlsx')

'''
for row in ws.rows:
    for cell in row:
'''