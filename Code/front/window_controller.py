from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class WindowController(QWidget):
    def __init__(self, db_connector):
        super().__init__()
        self.db_connector = db_connector    #db연결 인스턴스
        # Domain 인스턴스
        # self.login_user =   # 스케줄러 페이지
        #


        # UI 인스턴스
        # self.widget_login = LoginWidget()
        # self.widget_chat_widget = LoginWidget()
        # self.widget_friends_list = LoginWidget()
        #
