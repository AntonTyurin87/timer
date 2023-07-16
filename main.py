from PyQt5 import uic
# from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from datetime import datetime
from threading import Timer
from excel_main import date_and_time_wrote


Form, Window = uic.loadUiType("timer_GUI_2.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

counter_start = 1  # Счетчик для нажатия на кнопку "Старт/Финиш"

work_time_pass = 0
studies_time_pass = 0
rest_time_pass = 0

time_work_plane = [int(form.timeEdit.time().toString('hh')),
                   int(form.timeEdit.time().toString('mm'))]
time_studies_plane = [int(form.timeEdit_2.time().toString('hh')),
                      int(form.timeEdit_2.time().toString('mm'))]
time_rest_plane = [int(form.timeEdit_3.time().toString('hh')),
                   int(form.timeEdit_3.time().toString('mm'))]

form.pushButton_4.setStyleSheet("background-color: rgb(237, 51, 59)")

def now_time():
    return [datetime.now().time().hour, datetime.now().time().minute]


def work_button_on():
    form.pushButton.setStyleSheet("background-color: rgb(46, 194, 126)")
    form.pushButton_2.setStyleSheet("background-color: rgb(245, 194, 17)")
    form.pushButton_3.setStyleSheet("background-color: rgb(245, 194, 17)")


def studies_button_on():
    form.pushButton_2.setStyleSheet("background-color: rgb(46, 194, 126)")
    form.pushButton.setStyleSheet("background-color: rgb(245, 194, 17)")
    form.pushButton_3.setStyleSheet("background-color: rgb(245, 194, 17)")


def rest_button_on():
    form.pushButton_3.setStyleSheet("background-color: rgb(46, 194, 126)")
    form.pushButton.setStyleSheet("background-color: rgb(245, 194, 17)")
    form.pushButton_2.setStyleSheet("background-color: rgb(245, 194, 17)")


def on_click_work():  # Кнопка "Рабочее время"
    global start_time, time_work_plane
    work_button_on()
    start_time = now_time()

    if work_time_pass != 0:
        start_time[1] -= work_time_pass

    counter_work_time()

    form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")

    t_studies.cancel()
    t_rest.cancel()
    


def on_click_studies():  # Кнопка "Учебное время"
    global start_time, time_studies_plane
    studies_button_on()
    start_time = now_time()

    if studies_time_pass != 0:
        start_time[1] -= studies_time_pass

    form.pushButton_4.setStyleSheet("background-color: rgb(51, 209, 122)")

    counter_studies_time()

    t_work.cancel()
    t_rest.cancel()


def on_click_rest():  # Кнопка "Отдых"
    global start_time, time_rest_plane
    rest_button_on()
    start_time = now_time()

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
    global t_work, start_time, work_time_pass
    work_plane_minutes = time_work_plane[0] * 60 + time_work_plane[1]
    now_time_minytes = datetime.now().time().hour * 60 + datetime.now().time().minute
    start_work_minutes = start_time[0] * 60 + start_time[1]
    work_time_pass = now_time_minytes - start_work_minutes
    work_persent = work_time_pass * 100 / work_plane_minutes
    if work_persent > 100:
        form.pushButton.setStyleSheet("background-color: rgb(237, 51, 59);")
        t_work.cancel()
    form.progressBar.setProperty("value", work_persent)
    t_work = Timer(10, counter_work_time)
    t_work.start()


def counter_studies_time():
    global t_studies, start_time, studies_time_pass
    studies_plane_minutes = time_studies_plane[0] * 60 + time_studies_plane[1]
    now_time_minytes = datetime.now().time().hour * 60 + datetime.now().time().minute
    start_studies_minutes = start_time[0] * 60 + start_time[1]
    studies_time_pass = now_time_minytes - start_studies_minutes
    studies_persent = studies_time_pass * 100 / studies_plane_minutes
    if studies_persent > 100:
        form.pushButton_2.setStyleSheet("background-color: rgb(237, 51, 59);")
        t_studies.cancel()
    form.progressBar_2.setProperty("value", studies_persent)
    t_studies = Timer(10, counter_studies_time)
    t_studies.start()


def counter_rest_time():
    global t_rest, start_time, rest_time_pass
    rest_plane_minutes = time_rest_plane[0] * 60 + time_rest_plane[1]
    now_time_minytes = datetime.now().time().hour * 60 + datetime.now().time().minute
    start_rest_minutes = start_time[0] * 60 + start_time[1]
    rest_time_pass = now_time_minytes - start_rest_minutes
    rest_persent = rest_time_pass * 100 / rest_plane_minutes
    if rest_persent >= 100:
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

date_and_time_wrote(time_work_plane, time_studies_plane, time_rest_plane)

#form.tabWidget.tabBarClicked.connect(print_qt) # клик по вкладкам

app.exec_()
