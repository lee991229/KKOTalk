from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_profile_page_ui import Ui_profile_page


class ProfilePage(QWidget, Ui_profile_page):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.user_id = None
        self.username = None
        self.password = None
        self.nickname = None

    def show(self):
        self.set_label_text()
        super().show()

    def set_profile_user_data(self, user_data):
        self.user_id = user_data.user_id
        self.username = user_data.username
        self.password = user_data.password
        self.nickname = user_data.nickname

    def set_label_text(self):
        print(self.user_id)
        self.nick_name_label.setText(self.nickname)
