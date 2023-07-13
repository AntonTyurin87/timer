from PyQt5 import uic
# from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from datetime import datetime
from threading import Timer

Form, Window = uic.loadUiType("timer_GUI.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

counter_start = 0  # Счетчик для нажатия на кнопку "Старт/Финиш"

work_time_pass = 0
studies_time_pass = 0
rest_time_pass = 0

#start_time = [datetime.now().time().hour, datetime.now().time().minute]

def start_time():
     global start_minutes
     start_minutes = datetime.now().time().hour * 60 + datetime.now().time().minute


def button_work_on():
    form.pushButton.setStyleSheet("background-color: rgb(46, 194, 126)")
    form.pushButton_2.setStyleSheet("background-color: rgb(245, 194, 17)")
    form.pushButton_3.setStyleSheet("background-color: rgb(245, 194, 17)")


def button_studies_on():
    form.pushButton_2.setStyleSheet("background-color: rgb(46, 194, 126)")
    form.pushButton.setStyleSheet("background-color: rgb(245, 194, 17)")
    form.pushButton_3.setStyleSheet("background-color: rgb(245, 194, 17)")


def button_rest_on():
    form.pushButton_3.setStyleSheet("background-color: rgb(46, 194, 126)")
    form.pushButton.setStyleSheet("background-color: rgb(245, 194, 17)")
    form.pushButton_2.setStyleSheet("background-color: rgb(245, 194, 17)")


def on_click_work():  # Кнопка "Рабочее время"
    global start_time, work_plane_minutes
    button_work_on()
    start_time()
    #start_time = [datetime.now().time().hour, datetime.now().time().minute]
    work_plane_minutes = (int(form.timeEdit.time().toString('hh')) * 60
                          + int(form.timeEdit.time().toString('mm')))

    if work_time_pass != 0:
        start_time[1] -= work_time_pass

    counter_work_time()

    form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")

    t_studies.cancel()
    t_rest.cancel()


def on_click_studies():  # Кнопка "Учебное время"
    global start_time, studies_plane_minutes
    button_studies_on()
    start_time()
    #start_time = [datetime.now().time().hour, datetime.now().time().minute]
    studies_plane_minutes = (int(form.timeEdit_2.time().toString('hh')) * 60
                             + int(form.timeEdit_2.time().toString('mm')))

    if studies_time_pass != 0:
        start_time[1] -= studies_time_pass

    form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")

    counter_studies_time()

    t_work.cancel()
    t_rest.cancel()


def on_click_rest():  # Кнопка "Отдых"
    global start_time, rest_plane_minutes
    button_rest_on()
    start_time()
    #start_time = [datetime.now().time().hour, datetime.now().time().minute]
    rest_plane_minutes = (int(form.timeEdit_3.time().toString('hh')) * 60
                          + int(form.timeEdit_3.time().toString('mm')))

    if rest_time_pass != 0:
        start_time[1] -= rest_time_pass

    form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")

    counter_rest_time()

    t_work.cancel()
    t_studies.cancel()


def on_click_button_4():  # Кнопка Старт/Финиш
    global counter_start
    if counter_start == 0:
        form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")
        counter_start = 1
    elif counter_start == 1:
        form.pushButton_4.setStyleSheet("background-color: rgb(237, 51, 59);")
        form.pushButton_3.setStyleSheet("background-color: rgb(237, 51, 59);")
        form.pushButton_2.setStyleSheet("background-color: rgb(237, 51, 59);")
        form.pushButton.setStyleSheet("background-color: rgb(237, 51, 59);")
        t_work.cancel()
        t_studies.cancel()
        t_rest.cancel()
        counter_start = 0


def counter_work_time():
    now_time_minytes = datetime.now().time().hour * 60 + datetime.now().time().minute
    work_time_pass = now_time_minytes - start_minutes
    work_persent = work_time_pass * 100 / work_plane_minutes

    if work_persent > 100:
        form.pushButton.setStyleSheet("background-color: rgb(237, 51, 59);")
        t_work.cancel()

    form.progressBar.setProperty("value", work_persent)
    t_work = Timer(10, counter_work_time)
    t_work.start()


def counter_studies_time():
    now_time_minytes = datetime.now().time().hour * 60 + datetime.now().time().minute
    studies_time_pass = now_time_minytes - start_minutes
    studies_persent = studies_time_pass * 100 / studies_plane_minutes

    if studies_persent > 100:
        form.pushButton_2.setStyleSheet("background-color: rgb(237, 51, 59);")
        t_studies.cancel()

    form.progressBar_2.setProperty("value", studies_persent)
    t_studies = Timer(10, counter_studies_time)
    t_studies.start()


def counter_rest_time():
    now_time_minytes = datetime.now().time().hour * 60 + datetime.now().time().minute
    rest_time_pass = now_time_minytes - start_minutes
    rest_persent = rest_time_pass * 100 / rest_plane_minutes

    if rest_persent > 100:
        form.pushButton_3.setStyleSheet("background-color: rgb(237, 51, 59);")
        t_rest.cancel()

    form.progressBar_3.setProperty("value", rest_persent)
    t_rest = Timer(10, counter_rest_time)
    t_rest.start()


t_work = Timer(10, counter_work_time)
t_studies = Timer(10, counter_studies_time)
t_rest = Timer(10, counter_rest_time)

form.pushButton_4.clicked.connect(on_click_button_4)
form.pushButton.clicked.connect(on_click_work)
form.pushButton_2.clicked.connect(on_click_studies)
form.pushButton_3.clicked.connect(on_click_rest)


app.exec_()
