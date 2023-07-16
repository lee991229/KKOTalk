from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_profile_item_ui import Ui_profile_widget


class ProfileItemWidget(QWidget, Ui_profile_widget):
    def __init__(self, client_controller, friend_data):
        super().__init__()
        self.client_controller = client_controller
        self.setupUi(self)
        self.user_id = friend_data.user_id
        self.nickname = friend_data.nickname
        self.name = friend_data.username
        self.press_signal()
        self.set_label_text()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)


    def press_signal(self):
        # todo: 해당 프로필 유저 id보내기
        self.profile.mouseDoubleClickEvent = lambda x: self.client_controller.show_profile_page(self.user_id)

    def set_label_text(self):
        self.profile_name_label.setText(self.nickname)
