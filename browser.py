import time

def set_alarm(alarm_time):
    current_time = time.strftime("%H:%M:%S", time.localtime())
    while current_time != alarm_time:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        time.sleep(1)
    print("Пора просыпаться!")

alarm_time = input("Введите время будильника (в формате ЧЧ:ММ:СС): ")
set_alarm(alarm_time)