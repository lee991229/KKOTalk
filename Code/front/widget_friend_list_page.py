from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_friend_list_ui import Ui_ui_friend_list_widget
class FriendListWidget(QWidget, Ui_ui_friend_list_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)