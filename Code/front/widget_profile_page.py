from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_profile_page_ui import Ui_profile_page


class ProfilePage(QWidget, Ui_profile_page):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.user_id = None

    def set_profile_user_id(self, user_id):
        self.user_id = user_id
