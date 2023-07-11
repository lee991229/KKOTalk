import sys

from PyQt5.QtWidgets import QApplication

from Code.front.class_client_controller import WindowController
from Code.front.widget_login_page import LoginWidget
from Common.common_module import *
from PyQt5 import QtCore, QtGui, QtWidgets





if __name__ == '__main__':
    app = QApplication(sys.argv)
    client_controller = WindowController()
    client_controller.run()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())
