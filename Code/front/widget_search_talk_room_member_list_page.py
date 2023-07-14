from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_search_talk_room_member_list import Ui_talk_room_member_list_widget


class UserListWidgetInTalkRoom(QWidget, Ui_talk_room_member_list_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.set_btn_trigger()
        self.client_controller = client_controller
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    def close(self):
        super().close()

    def set_btn_trigger(self):
        self.btn_flist_close.clicked.connect(lambda state: self.close())

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)
