from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_talk_room_list_ui import Ui_tk_room_list_widget
from PyQt5.QtCore import Qt


class TalkRoomListWidget(QWidget, Ui_tk_room_list_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.setGeometry(250, 95, self.width(), self.height())
    def show(self):
        self.set_initial_widget()
        super().show()
    def set_initial_widget(self):
        self.talk_list_page_search_bar_2.hide()
        self.btn_tkroom_search.hide()
        self.talk_list_page_search_bar_2.hide()
        # self.talk_list_page_search_bar_1.hide()
    def page_close(self):
        self.close()
        self.client_controller.clear_widget(self.tkroom_list_area)


    def set_btn_trigger(self):
        self.btn_friend_list_page.clicked.connect(lambda x: (self.client_controller.show_friend_list(), self.page_close()))
        self.btn_tallk_room_make.clicked.connect(self.client_controller.show_make_talk_room)
        self.btn_tkroom_close.clicked.connect(self.page_close)
        pass
