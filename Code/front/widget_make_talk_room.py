from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_make_talk_room_ui import Ui_make_talk_room_widget

class InviteFriendListWidget(QWidget,Ui_make_talk_room_widget):
    def __init__(self,client_controller):
        super().__init__()
        self.setupUi(self)