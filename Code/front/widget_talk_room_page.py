from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_talk_room_ui import Ui_talk_room_widget


class TalkRoomWidget(QWidget, Ui_talk_room_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()

    def set_btn_trigger(self):
        self.btn_member_plus.clicked.connect(self.client_controller.show_member_plus)
        self.widget_member_count.mousePressEvent = lambda x: (self.client_controller.show_room_member_list())
