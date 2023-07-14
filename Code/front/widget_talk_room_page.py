from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_talk_room_ui import Ui_talk_room_widget


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

    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.setGeometry(850, 95, self.width(), self.height())

    # def
    def chat_line_ediet_input(self):
        user_chat = self.user_chatting_lineedit.text()
        self.chatting_label(user_chat)
        pass

    def chatting_label(self, user_chat=None):
        if user_chat is not None:
            chat = QLabel(self)
            chat.setStyleSheet(self.CHAT_MESSAGE_STYLESHEET)
            chat.setText(user_chat)
            self.widget.layout().addWidget(chat)

    def set_btn_trigger(self):
        self.btn_member_plus.clicked.connect(
            self.client_controller.show_member_plus)  # todo: 채팅방에 있는 유저 정보 저장하고 파라미터로 이거 보내
        self.widget_member_count.mousePressEvent = lambda x: (self.client_controller.show_room_member_list())
        self.chat_input_button.clicked.connect(self.chat_line_ediet_input)
