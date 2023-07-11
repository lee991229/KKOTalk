# 공통적으로 사용할 함수나 상수를 등록 or 선언하도록 합니다.
import json
from json import JSONEncoder, JSONDecoder

from PyQt5 import QtCore, QtGui, QtWidgets

from Code.domain.class_message import Message
from Code.domain.class_user import User


def show_error_message(message, traceback):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    msg_box.setWindowTitle("Error")
    msg_box.setText(message)
    msg_box.exec_()
    traceback.print_exc()


class KKOEncoder(JSONEncoder):

    def __init__(self):
        super().__init__()

    def default(self, o):
        return o.__dict__


class KKODecoder(JSONDecoder):
    def __init__(self):
        super().__init__()

    def decode(self, o, **kwargs):
        dict_obj = super().decode(o, **kwargs)
        if 'user_id' in dict_obj.keys():
            return User(dict_obj['user_id'], dict_obj['username'], dict_obj['password'], dict_obj['nickname'])
        elif 'message_id' in dict_obj.keys():
            return Message(dict_obj['message_id'], dict_obj['sender_user_id'], dict_obj['talk_room_id'],
                           dict_obj['contents'], dict_obj['send_time_stamp'], dict_obj['long_contents_id'])
