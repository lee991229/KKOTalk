import sys

from PyQt5.QtWidgets import QApplication

from Code.domain.class_db_connector import DBConnector
from Code.front.class_client_controller import WindowController
from Code.front.widget_login_page import LoginWidget
from Common.common_module import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Code.domain.class_user import User
from Code.domain.class_talk_room import TalkRoom




if __name__ == '__main__':
    app = QApplication(sys.argv)
    conn = DBConnector()
    conn.create_tables()

    user_a = User(None, 'abc1234', '1234', '뿡뿡이')
    user_b = User(None, 'def5678', '5678', '짱구')
    user_c = User(None, 'qwe', '123', '란타로')
    user_d = User(None, 'asd', '123', '나루토')
    user_e = User(None, '123', '123', '사스케')
    user_a = conn.insert_user(user_a)
    user_b = conn.insert_user(user_b)
    user_c = conn.insert_user(user_c)
    user_d = conn.insert_user(user_d)
    user_e = conn.insert_user(user_e)

    client_controller = WindowController(conn)
    client_controller.run()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())
