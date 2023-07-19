import sys

from PyQt5.QtWidgets import QApplication

from Code.domain.class_db_connector import DBConnector
from Code.domain.class_user_talk_room import UserTalkRoom
from Code.front.class_client_controller import WindowController
from Code.front.widget_login_page import LoginWidget
from Code.network.class_client import ClientApp
from Code.network.class_server import Server
from Common.common_module import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Code.domain.class_user import User
from Code.domain.class_talk_room import TalkRoom


if __name__ == '__main__':
    app = QApplication(sys.argv)

    client_object = ClientApp()

    client_controller = WindowController(client_object)

    client_controller.run()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())
