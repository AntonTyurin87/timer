from PyQt5 import uic
# from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from datetime import datetime
from threading import Timer
from excel_main_2 import check_date_position, set_time_plane, set_time_pass

Form, Window = uic.loadUiType("timer_GUI_2.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

red_color = "background-color: rgb(237, 51, 59)"
green_color = "background-color: rgb(51, 209, 122)"
yellow_color = "background-color: rgb(245, 194, 17)"

button_4 = form.pushButton_4.setStyleSheet
button_3 = form.pushButton_3.setStyleSheet
button_2 = form.pushButton_2.setStyleSheet
button_1 = form.pushButton.setStyleSheet
button_0 = None
buttons = [button_0, button_1, button_2, button_3, button_4]

form.pushButton_4.setStyleSheet(red_color)
form.pushButton_3.setStyleSheet(red_color)
form.pushButton_2.setStyleSheet(red_color)
form.pushButton.setStyleSheet(red_color)

scheduled_time = {  1: [int(form.timeEdit.time().toString('hh')),
                    int(form.timeEdit.time().toString('mm'))],
                    2: [int(form.timeEdit_2.time().toString('hh')),
                    int(form.timeEdit_2.time().toString('mm'))],
                    3: [int(form.timeEdit_3.time().toString('hh')),
                    int(form.timeEdit_3.time().toString('mm'))] }
'''
time_work_plane = [int(form.timeEdit.time().toString('hh')),
                   int(form.timeEdit.time().toString('mm'))]
time_studies_plane = [int(form.timeEdit_2.time().toString('hh')),
                      int(form.timeEdit_2.time().toString('mm'))]
time_rest_plane = [int(form.timeEdit_3.time().toString('hh')),
                   int(form.timeEdit_3.time().toString('mm'))]
'''


def clisked_button(button_number):
    #time.cancel()
    buttons[button_number](green_color)
    buttons[4](green_color)

    for i in range(1,4):
        if i != button_number:
            buttons[i](yellow_color)
    
    set_time_plane(check_date_position(), button_number, scheduled_time)

    time_count = 20

    time_pass = set_time_pass(check_date_position(), button_number, time_count)

    work_persent = (scheduled_time.get(button_number)[0] * 3600 + scheduled_time.get(button_number)[1] * 60) / time_pass

    form.progressBar.setProperty("value", work_persent)

    time = Timer(time_count, clisked_button)
    time.start()
    

def click_button_1():
    clisked_button(1)



#form.pushButton_4.clicked.connect(on_click_button_4)
form.pushButton.clicked.connect(click_button_1)
#form.pushButton_2.clicked.connect(on_click_studies)
#form.pushButton_3.clicked.connect(on_click_rest)


app.exec_()

'''
    form.pushButton_4.setStyleSheet("background-color: rgb(237, 51, 59);")
    form.pushButton_3.setStyleSheet("background-color: rgb(237, 51, 59);")
    form.pushButton_2.setStyleSheet("background-color: rgb(237, 51, 59);")
    form.pushButton.setStyleSheet("background-color: rgb(237, 51, 59);")

'''

