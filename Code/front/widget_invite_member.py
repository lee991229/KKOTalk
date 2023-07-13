from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_invite_member_widget_ui import Ui_invite_member_widget


class InviteMemberWidget(QWidget, Ui_invite_member_widget):
    def __init__(self, make_talk_widget, friend_data):
        super().__init__()
        self.setupUi(self)
        self.parent = make_talk_widget
        self.user_id = friend_data.user_id
        self.nickname = friend_data.nickname
        self.name = friend_data.username
        self.set_label_text()

    def set_label_text(self):
        self.user_nickname_label.setText(self.nickname)

    def is_btn_checked(self):
        return self.check_btn.isChecked()

    def get_nickname(self):
        return self.nickname

    # def invite_btn_checked(self):
