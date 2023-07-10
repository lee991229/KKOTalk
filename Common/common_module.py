# 공통적으로 사용할 함수나 상수를 등록 or 선언하도록 합니다.

from PyQt5 import QtCore, QtGui, QtWidgets
def show_error_message(message, traceback):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    msg_box.setWindowTitle("Error")
    msg_box.setText(message)
    msg_box.exec_()
    traceback.print_exc()