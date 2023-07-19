from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_friend_list_ui import Ui_friend_list_widget
from Code.front.widget_profile_item import ProfileItemWidget
from PyQt5.QtCore import Qt


class FriendListWidget(QWidget, Ui_friend_list_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.setGeometry(250, 95, self.width(), self.height())
        self.login_user_obj = None
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    def show(self):
        self.set_widget_user_list()
        self.set_initial_widget()
        super().show()

    def set_initial_widget(self):
        user = self.client_controller.get_user_self()
        self.label_title.setText(f"{user.nickname}의 크크오톡 친구목록")
        self.friend_page_search_bar_2.hide()
        self.btn_flist_search.hide()

    def set_window_drag(self):
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    def close(self):
        self.client_controller.clear_widget(self.friend_list_layout_widget)
        super().close()

    def set_btn_trigger(self):
        self.btn_start_chat.clicked.connect(
            lambda x: (self.client_controller.show_talk_room_list_page(), self.close()))
        self.btn_flist_close.clicked.connect(lambda state: self.close())

    def profile_press(self, user_id):
        self.client_controller.show_profile_page(user_id)

    # 친구 위젯 레이아웃에 넣기
    def set_widget_user_list(self):
        self.client_controller.clear_widget(self.friend_list_layout)
        friend_list = self.client_controller.get_all_user_list()
        user_self = self.client_controller.get_user_self()
        for user in friend_list:
            if user.user_id == user_self.user_id:
                continue
            friend_profile = ProfileItemWidget(self.client_controller, user)
            self.friend_list_layout.addWidget(friend_profile)
