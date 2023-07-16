from Code.front.widget_profile_item import ProfileItemWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_search_talk_room_member_list import Ui_talk_room_member_list_widget


class UserListWidgetInTalkRoom(QWidget, Ui_talk_room_member_list_widget):
    def __init__(self, client_controller, widget_talk_room):
        super().__init__()
        self.setupUi(self)
        self.widget_talk_room = widget_talk_room
        self.set_btn_trigger()
        self.client_controller = client_controller
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    def show(self):
        self.set_geometry_position()
        self.set_already_invited_user_widget()
        super().show()

    def set_geometry_position(self):
        current_position = self.widget_talk_room.frameGeometry().topLeft()
        x_pos = current_position.x() + 30
        y_pos = current_position.y() + 110
        self.setGeometry(x_pos, y_pos, self.width(), self.height())

    # 현재 있는 유저 리스트를 추가해야함
    def set_already_invited_user_widget(self):
        self.client_controller.clear_widget(self.widget_user_list)
        user_list = self.client_controller.get_already_invited_user_list()
        layout_to_add = self.widget_user_list.layout()
        if layout_to_add is None:
            layout_to_add = QtWidgets.QVBoxLayout(self)
            self.widget_user_list.setLayout(layout_to_add)
        for user in user_list:
            user_item_widget = ProfileItemWidget(self.client_controller, user)
            layout_to_add.addWidget(user_item_widget)



    def close(self):
        super().close()

    def set_btn_trigger(self):
        self.btn_flist_close.clicked.connect(lambda state: self.close())

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)
