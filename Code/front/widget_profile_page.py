from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_profile_page_ui import Ui_profile_page


class ProfilePage(QWidget, Ui_profile_page):
    def __init__(self, client_controller, friend_user_obj=None):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.friend_user_id = None
        self.friend_username = None
        self.friend_password = None
        self.friend_nickname = None
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.set_btn_trigger()
        if friend_user_obj is not None:
            self.set_profile_user_data(friend_user_obj)

    def set_btn_trigger(self):
        self.close_btn.clicked.connect(lambda state: self.close())
        self.btn_start_chat.clicked.connect(lambda state: self.open_chat_room_in_item_widget())

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)
    def close(self):
        # 함수 실행전 하고 싶은 기능
        super().close()

    def show(self):
        self.set_label_text()
        super().show()

    def open_chat_room_in_item_widget(self):
        self.client_controller.open_one_to_one_chat_room(self.friend_user_id)
        self.close()

    def set_profile_user_data(self, user_data):
        self.friend_user_id = user_data.user_id
        self.friend_username = user_data.username
        self.friend_password = user_data.password
        self.friend_nickname = user_data.nickname

    def set_label_text(self):
        self.nick_name_label.setText(self.friend_nickname)
