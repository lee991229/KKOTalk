# 공통적으로 사용할 함수나 상수를 등록 or 선언하도록 합니다.
from datetime import datetime

from PyQt5 import QtWidgets


def show_error_message(message, traceback):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    msg_box.setWindowTitle("Error")
    msg_box.setText(message)
    msg_box.exec_()
    traceback.print_exc()


def get_now_time_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_subtract_time(str_start_timestamp):
    try:
        parsed_datetime = datetime.strptime(str_start_timestamp, "%Y-%m-%d %H:%M:%S")
    except:
        return '알수 없는 시간'
    now_time = datetime.now()
    result_time_delta = now_time - parsed_datetime
    return f"{result_time_delta.min}"
