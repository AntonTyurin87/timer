from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication

from datetime import datetime

from threading import Timer

Form, Window = uic.loadUiType("timer_GUI.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

counter_start = 0 # Счетчик для нажатия на кнопку "Старт/Финиш"

#time_work_plane = form.timeEdit.selectedTime()
#time_studies_plane =
#time_rest_plane =





def on_click_work(): # Кнопка "Рабочее время"
    form.pushButton.setStyleSheet("background-color: rgb(46, 194, 126)")
    form.pushButton_2.setStyleSheet("background-color: rgb(245, 194, 17)")
    form.pushButton_3.setStyleSheet("background-color: rgb(245, 194, 17)")
    time_work_plane = form.timeEdit.time().toString('hh-mm')
    # print(time_work_plane)
    start_work_time_hour = datetime.now().time().hour
    start_work_time_minute = datetime.now().time().minute

    counter()

    form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")


def on_click_studies(): # Кнопка "Учебное время"
    form.pushButton_2.setStyleSheet("background-color: rgb(46, 194, 126)")
    form.pushButton.setStyleSheet("background-color: rgb(245, 194, 17)")
    form.pushButton_3.setStyleSheet("background-color: rgb(245, 194, 17)")
    time_work_studies = form.timeEdit_2.time().toString('hh-mm')
    # print(time_work_studies)
    form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")


def on_click_rest(): # Кнопка "Отдых"
    form.pushButton_3.setStyleSheet("background-color: rgb(46, 194, 126)")
    form.pushButton.setStyleSheet("background-color: rgb(245, 194, 17)")
    form.pushButton_2.setStyleSheet("background-color: rgb(245, 194, 17)")
    time_work_rest = form.timeEdit_3.time().toString('hh-mm')
    # print(time_work_rest)
    form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")


def on_click_button_4(): # Кнопка Старт/Финиш
    global counter_start
    print("Clicked Button_4!!!")
    if counter_start == 0: 
        form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")
        counter_start = 1
        start_count_hour = datetime.now().time().hour
        start_count_minute = datetime.now().time().minute
        

        print(datetime.now().time().hour)

    elif counter_start == 1:
        form.pushButton_4.setStyleSheet("background-color: rgb(237, 51, 59);")
        counter_start = 0
    

def counter():
    #global persent_1

    #t = Timer(10, hello)
    #t.start()
    pass


form.pushButton_4.clicked.connect(on_click_button_4)
form.pushButton.clicked.connect(on_click_work)
form.pushButton_2.clicked.connect(on_click_studies)
form.pushButton_3.clicked.connect(on_click_rest)


app.exec_()