from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_friend_list_ui import Ui_friend_list_widget


class FriendListWidget(QWidget, Ui_friend_list_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.setGeometry(250, 95, self.width(), self.height())

    # 아아 이건 오버 라이딩 이라는 것이다
    def show(self):
        self.set_initial_widget()
        super().show()

    def set_initial_widget(self):
        self.widget_3.hide() # todo:'이름 바꾸기'

    def set_btn_trigger(self):
        self.btn_tk_roomlist.clicked.connect(self.client_controller.show_talk_room_list_page)
        # self.btn_flist_close.clicked.connect()
        # self.btn_flist_search
        # self.btn_flist_click_search
        pass
    def set_friend_widget(self):
        self.client_controller.get_friend_list()