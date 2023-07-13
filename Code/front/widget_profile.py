from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_profile_ui import Ui_profile_widget


class ProfileWidget(QWidget, Ui_profile_widget):
    def __init__(self, friend_list_page, friend_data):
        super().__init__()
        self.parent = friend_list_page
        self.setupUi(self)
        self.user_id = friend_data.user_id
        self.nickname = friend_data.nickname
        self.name = friend_data.username
        self.press_signal()
        self.set_label_text()

    def press_signal(self):
        # todo: 해당 프로필 유저 id보내기
        self.profile.mouseDoubleClickEvent = lambda x: self.parent.profile_press(self.user_id)

    def set_label_text(self):
        self.profile_name_label.setText(self.nickname)
    # def set_friend_widget(self):
    #     friend_list = self.client_controller.get_friend_list()
    #
    #     print(friend_list)
    #     print(id(friend_list))
