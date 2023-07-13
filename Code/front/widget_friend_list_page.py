from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_friend_list_ui import Ui_friend_list_widget
from Code.front.widget_profile import ProfileWidget
from PyQt5.QtCore import Qt


class FriendListWidget(QWidget, Ui_friend_list_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.setGeometry(250, 95, self.width(), self.height())
        self.set_initial_widget()
        self.login_user_obj = None
        self.friend_list = None

    # 아아 이건 오버 라이딩 이라는 것이다
    def show(self):
        self.login_user_obj = self.client_controller.login_user_obj
        self.friend_list = self.client_controller.friend_list
        self.get_friend_list()
        super().show()

    def set_initial_widget(self):
        self.friend_page_search_bar_2.hide()
        self.btn_flist_search.hide()
        # self.friend_page_search_bar_1.hide()
        # self.friend_page_search_bar_1.hide()
        pass


    def page_close(self):
        self.close()
        self.client_controller.clear_widget(self.friend_list_layout_widget)

    def set_btn_trigger(self):
        self.btn_tk_roomlist.clicked.connect(lambda x: (self.client_controller.show_talk_room_list_page(), self.page_close()))
        self.btn_flist_close.clicked.connect(self.page_close)

    def profile_press(self, user_id):
        self.client_controller.show_profile_page(user_id)

    # 친구 위젯 레이아웃에 넣기
    def get_friend_list(self):
        friend_list = self.friend_list
        for friend in friend_list:
            friend_profile = ProfileWidget(self, friend)
            self.friend_list_layout.addWidget(friend_profile)
