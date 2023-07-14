from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Code.front.ui.ui_class_widget_invite_user_item import Ui_invite_member_widget


class InviteUserItem(QWidget, Ui_invite_member_widget):
    def __init__(self, make_talk_widget, friend_data):
        super().__init__()
        self.setupUi(self)
        self.set_btn_trigger()
        self.invite_talk_room_widget = make_talk_widget
        self.user_id = friend_data.user_id
        self.nickname = friend_data.nickname
        self.name = friend_data.username
        self.set_label_text()
    def set_btn_trigger(self):
        self.check_btn.clicked.connect(lambda state: self.refresh_count_label())
    def refresh_count_label(self):
        result_number = self.invite_talk_room_widget.count_checked_user()
        self.invite_talk_room_widget.label_user_count.setText(f"{result_number}명")
        # if self.check_btn.isChecked():
        #     self.invite_talk_room_widget.btn_is_chacked_check_true(self)
        #     #클릭되어있으면
        # else:
        #     self.invite_talk_room_widget.btn_is_chacked_check_false(self)
        #     #클릭이아니면
    def set_label_text(self):
        self.user_nickname_label.setText(self.nickname)

    def is_btn_checked(self):
        return self.check_btn.isChecked()

    def get_nickname(self):
        return self.nickname

    # def invite_btn_checked(self):
