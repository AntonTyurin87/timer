import openpyxl, os, datetime, re
from openpyxl import load_workbook
from datetime import date 
from datetime import datetime

time_work_plane = [1,23]
time_studies_plane = [2, 2]
time_rest_plane = [3, 45]


# Запись даты и необходимого времени
def date_and_time_wrote(time_work_plane, time_studies_plane, time_rest_plane):
    time_data = '/home/anton/repositories/timer/time_stat.xlsx'

    file_data = load_workbook(time_data)
    file_page = file_data['data']

    work_plane_minutes = time_work_plane[0] * 60 + time_work_plane[1]
    studies_plane_minutes = time_studies_plane[0] * 60 + time_studies_plane[1]
    rest_plane_minutes = time_rest_plane[0] * 60 + time_rest_plane[1]
    
    date_place = len(file_page['A'])

    if file_page['A' + str(date_place)].value != datetime.today().strftime('%Y-%m-%d'):
        file_page['A' + str(date_place + 1)].value = datetime.today().strftime('%Y-%m-%d')
        file_page['B' + str(date_place + 1)] = studies_plane_minutes
        file_page['D' + str(date_place + 1)] = work_plane_minutes
        file_page['F' + str(date_place + 1)] = rest_plane_minutes

    file_data.save(time_data)
    file_data.close()


date_and_time_wrote(time_work_plane, time_studies_plane, time_rest_plane)


'''
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


for row in ws.rows:
    for cell in row:
'''