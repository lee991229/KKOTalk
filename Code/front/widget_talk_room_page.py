import datetime

import Common.common_module
from Code.domain.class_message import Message
from Code.front.widget_message_label import MessageLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_talk_room_ui import Ui_talk_room_widget
from PyQt5.QtCore import Qt


class TalkRoomWidget(QWidget, Ui_talk_room_widget):

    def __init__(self, client_controller, talk_room_id):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.talk_room_id = talk_room_id
        self.talk_room_member_user_list = list()
        self.talk_room = None
        self.set_btn_trigger()
        self.setGeometry(850, 95, self.width(), self.height())
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    def set_talk_room_id(self, talk_room_id):
        self.talk_room_id = talk_room_id

    def set_chat_room_title(self):
        # todo: talk_room 방 이름 갱신 로직
        self.talk_room = self.client_controller.get_talk_by_room_id(self.talk_room_id)
        self.label_title.setText(f"{self.talk_room.talk_room_name}")

    def show(self):
        # todo: talk_room 메시지를 갱신하는 로직
        # todo: talk_room 멤버를 갱신하는 로직
        self.set_chat_room_title()
        super().show()

    def close(self):
        self.talk_room_id = None
        self.talk_room_member_user_list.clear()
        super().close()

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    # def
    def chat_line_edit_input(self):
        user_chat = self.user_chatting_lineedit.text()
        # 클라이언트앱 호출 로직 추가
        self.user_chatting_lineedit.clear()
        user_id = self.client_controller.client_app.user_id
        now_time_str = Common.common_module.get_now_time_str()
        message_obj = Message(None, user_id, self.talk_room_id, now_time_str, user_chat, None)
        self.insert_chatting_label_in_scroll_page(message_obj)
        self.client_controller.send_msg_se(self.talk_room_id, user_chat)

    def insert_chatting_label_in_scroll_page(self, message_obj: Message):
        if message_obj is not None and len(message_obj.contents) != 0:
            chat = MessageLabel(self.client_controller, message_obj)
            self.widget.layout().addWidget(chat)

    def set_btn_trigger(self):
        self.btn_member_plus.clicked.connect(lambda state:
                                             self.client_controller.show_member_plus())  # todo: 채팅방에 있는 유저 정보 저장하고 파라미터로 이거 보내
        self.widget_member_count.mouseDoubleClickEvent = lambda x: (self.client_controller.show_room_member_list())
        self.btn_chat_enter.clicked.connect(lambda state: self.chat_line_edit_input())
        self.btn_flist_close.clicked.connect(lambda state: self.close())
        self.user_chatting_lineedit.returnPressed.connect(lambda: self.chat_line_edit_input())
