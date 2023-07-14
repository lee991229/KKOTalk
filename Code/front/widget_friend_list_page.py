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
        self.set_initial_widget()
        self.login_user_obj = None
        self.friend_list = None
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.client_controller.drag_start_position)
            event.accept()

    def show(self):
        self.login_user_obj = self.client_controller.login_user_obj
        self.friend_list = self.client_controller.friend_list
        self.get_friend_list()
        super().show()

    def set_initial_widget(self):
        self.friend_page_search_bar_2.hide()
        self.btn_flist_search.hide()
        pass

    def set_window_drag(self):
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    def page_close(self):
        self.close()
        self.client_controller.clear_widget(self.friend_list_layout_widget)

    def set_btn_trigger(self):
        self.btn_start_chat.clicked.connect(
            lambda x: (self.client_controller.show_talk_room_list_page(), self.page_close()))
        self.btn_flist_close.clicked.connect(self.page_close)

    def profile_press(self, user_id):
        self.client_controller.show_profile_page(user_id)

    # 친구 위젯 레이아웃에 넣기
    def get_friend_list(self):
        friend_list = self.friend_list
        for friend in friend_list:
            friend_profile = ProfileItemWidget(self, friend)
            self.friend_list_layout.addWidget(friend_profile)
