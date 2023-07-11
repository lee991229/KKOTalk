from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_talk_room_member_plus import Ui_takl_room_member_plus_widget

class TalkRoomMemberPlusWidget(QWidget, Ui_takl_room_member_plus_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)