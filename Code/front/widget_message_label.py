import datetime

from Code.domain.class_message import Message
from Code.domain.class_user import User
from Code.front.ui.ui_class_message_label import Ui_widget_message
from PyQt5.QtWidgets import *

from Common.common_module import get_subtract_time


class MessageLabel(QWidget, Ui_widget_message):
    CHAT_MESSAGE_STYLESHEET_OTHER = """
        #background_widget{
            background-color: #FFB07F;
            border-radius: 20px;
            border-style: solid;
            border-width: 2px;
            border-color: #FF52A2;
        }

        #label_nickname{
            font: bold 12pt "나눔고딕";	
            color: #F31559;
        }
        #label_message{
            font: bold 10pt "나눔고딕";	
            color: #001C30;
        }"""

    CHAT_MESSAGE_STYLESHEET_USER = """
        #background_widget{
            background-color: #A2FF86;
            border-radius: 20px;
            border-style: solid;
            border-width: 2px;
            border-color: #164B60;
        }

        #label_nickname{
            font: bold 12pt "나눔고딕";	
            color: #068FFF;
        }
        #label_message{
            font: bold 10pt "나눔고딕";	
            color: #2D4356;
        }"""

    def __init__(self, client_controller, message_obj:Message):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.message_obj = message_obj

        if isinstance(self.message_obj.user_obj, User):
            self.user_obj = self.message_obj.user_obj
        else:
            self.user_obj = self.client_controller.get_user_by_id(self.message_obj.sender_user_id)
        self.set_label()

    def set_label(self):
        self.label_message.setText(self.message_obj.contents)
        self.label_nickname.setText(self.user_obj.nickname)
        user = self.client_controller.get_user_self()
        if self.user_obj.user_id == user.user_id:
            self.spacer_right.hide()
            self.setStyleSheet(self.CHAT_MESSAGE_STYLESHEET_USER)
        else:
            self.spacer_left.hide()
            self.setStyleSheet(self.CHAT_MESSAGE_STYLESHEET_OTHER)
        timestamp = self.message_obj.send_time_stamp
        onset_time = get_subtract_time(timestamp)
        # self.label_from_time.setText(onset_time)

