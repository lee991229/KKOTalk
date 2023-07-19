from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_talk_room_list_ui import Ui_tk_room_list_widget
from PyQt5.QtCore import Qt

from Code.front.widget_chatroom_item import ChatRoomItemWidget


class TalkRoomListWidget(QWidget, Ui_tk_room_list_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.setGeometry(250, 95, self.width(), self.height())
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    def show(self):
        self.set_initial_widget()
        self.client_controller.clear_widget(self.tkroom_list_area)
        self.refresh_chat_room_list()
        super().show()

    def set_initial_widget(self):
        user = self.client_controller.get_user_self()
        self.label_title.setText(f"{user.nickname} 크크오톡 친구목록")
        self.talk_list_page_search_bar_2.hide()
        self.btn_tkroom_search.hide()
        self.talk_list_page_search_bar_2.hide()

    def close(self):
        super().close()

    def set_btn_trigger(self):
        self.btn_friend_list_page.clicked.connect(lambda state: self.show_talk_room())
        self.btn_tallk_room_make.clicked.connect(self.client_controller.show_make_talk_room)
        self.btn_tkroom_close.clicked.connect(lambda state: self.close())

    def show_talk_room(self):
        self.client_controller.show_friend_list()
        self.close()
    def refresh_chat_room_list(self):
        for talk_room in self.client_controller.get_all_talk_room():
            talk_room_item = ChatRoomItemWidget(self, talk_room)
            self.tkroom_list_area.layout().addWidget(talk_room_item)
