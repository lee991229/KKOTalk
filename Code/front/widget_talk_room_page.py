from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_talk_room_ui import Ui_talk_room_widget
from PyQt5.QtCore import Qt


class TalkRoomWidget(QWidget, Ui_talk_room_widget):
    CHAT_MESSAGE_STYLESHEET = """QLabel{
border: 3px solid rgb(76, 150, 231);
border-radius:20px;
border-style:solid;
background-color: rgb(244, 255, 255);
font-size: 15px;
font-weight: 600;
color: rgb(0, 0, 0);
}"""

    def __init__(self, client_controller, talk_room_id):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.talk_room_id = talk_room_id
        self.talk_room_member_user_list = list()
        self.set_btn_trigger()
        self.setGeometry(850, 95, self.width(), self.height())
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    def set_talk_room_id(self, talk_room_id):
        self.talk_room_id = talk_room_id

    def set_chat_room_title(self):
        # todo: talk_room 방 이름 갱신 로직
        self.label_title.setText(f"{self.talk_room_id}번방")

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
        self.user_chatting_lineedit.clear()
        self.chatting_label(user_chat)
        pass

    def chatting_label(self, user_chat_str):
        if user_chat_str is not None or len(user_chat_str) != 0:
            chat = QLabel(self)
            chat.setStyleSheet(self.CHAT_MESSAGE_STYLESHEET)
            chat.setText(user_chat_str)
            self.widget.layout().addWidget(chat)

    def set_btn_trigger(self):
        self.btn_member_plus.clicked.connect(
            self.client_controller.show_member_plus)  # todo: 채팅방에 있는 유저 정보 저장하고 파라미터로 이거 보내
        self.widget_member_count.mouseDoubleClickEvent = lambda x: (self.client_controller.show_room_member_list())
        self.btn_chat_enter.clicked.connect(self.chat_line_edit_input)
        self.btn_flist_close.clicked.connect(lambda state: self.close())
