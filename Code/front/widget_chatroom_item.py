from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_chat_room_item_ui import Ui_chat_room_item_widget


class ChatRoomItemWidget(QWidget, Ui_chat_room_item_widget):
    def __init__(self, widget_talk_room_list, talk_room_obj):
        super().__init__()
        self.setParent(widget_talk_room_list)
        self.talk_room_list_widget = widget_talk_room_list
        self.setupUi(self)
        self.talk_room_obj = talk_room_obj
        self.message_list = None
        self.press_signal()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.set_talk_room(self.talk_room_obj)

    def set_talk_room(self, talk_room_obj):
        self.talk_room_obj = talk_room_obj
        self.profile_name_label.setText(self.talk_room_obj.talk_room_name)

    def press_signal(self):
        self.profile.mouseDoubleClickEvent = lambda x: self.talk_room_list_widget.client_controller.show_talk_room(
            self.talk_room_obj.talk_room_id)
        # , self.talk_room_list_widget.client_controller.uninvited_friend_list(self.talk_room_id))

    # def set_label_text(self):
    #     self.profile_name_label.setText(f'채팅방 아이디: {self.talk_room_id}')
    # def set_friend_widget(self):
    #     friend_list = self.client_controller.set_widget_user_list()
    #
    #     print(friend_list)
    #     print(id(friend_list))
