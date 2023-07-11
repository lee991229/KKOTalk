from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_friend_list_ui import Ui_friend_list_widget


class FriendListWidget(QWidget, Ui_friend_list_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.start_hide_event()

    def start_hide_event(self):
        self.widget_3.hide()

    def set_btn_trigger(self):
        # self.btn_tk_roomlist.clicked.connect()
        # self.btn_flist_close.clicked.connect()
        # self.btn_flist_search
        # self.btn_flist_click_search
        pass
