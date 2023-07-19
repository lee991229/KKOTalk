from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Code.front.ui.ui_class_widget_talk_room_invite_user_list import Ui_make_talk_room_widget
from Code.front.widget_invite_member import InviteUserItem


class InviteFriendListWidget(QWidget, Ui_make_talk_room_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.friend_list = None
        self.user_item_widget_list = list()
        self.user_set_talk_room_name = None
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
    def count_checked_user(self):
        count = 0
        for w in self.user_item_widget_list:
            if w.is_btn_checked():
                count += 1
        return count

    def refresh_user_nickname_list_label(self):
        invite_user_nickname_list = list()
        for w in self.user_item_widget_list:
            if w.is_btn_checked():
                user_nickname = w.get_nickname()
                invite_user_nickname_list.append(user_nickname)
        return invite_user_nickname_list

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    def show(self):
        self.set_friend_list()
        self.set_user_item_widget_to_scroll_layout()
        super().show()

    def set_friend_list(self):
        # todo : 친구 리스트 갱신해서 집어넣기
        self.friend_list = self.client_controller.get_all_user_list()

    def close(self):
        self.friend_list.clear()
        self.lineEdit_user_set_talk_room_name.clear()
        super().close()

    def set_btn_trigger(self):
        self.btn_flist_close.clicked.connect(lambda state: self.close())
        self.close_btn.clicked.connect(lambda state: self.close())
        self.decision_btn.clicked.connect(self.making_talk_room)

    def making_talk_room(self):
        '''
        확인 버튼을 누르면
        새로운 채팅방을 띄우는 함수 호출
        새로운 채팅방의
        서버에 초대를 원하는 유저의 user_id를 list로 보내주는 함수 호출
        클라이언트에 있는 self.open_talk_room_widget에 인스터스화한 채팅방(TalkRoomWidget)을 추가
        '''
        invite_member_list = list()
        invite_member_list.append(self.client_controller.get_user_self().user_id)
        for w in self.user_item_widget_list:
            w:InviteUserItem
            if w.is_btn_checked():
                invite_member_list.append(w.user_id)
        self.user_set_talk_room_name = self.lineEdit_user_set_talk_room_name.text()
        self.invite_selected_user_to_talk_room(invite_member_list)
        self.close()



    def invite_selected_user_to_talk_room(self, invite_member_list:list[int]):
        '''
        서버에 초대를 원하는 유저의 user_id를 list로 보내준다
        '''
        talk_room_name = self.lineEdit_user_set_talk_room_name.text()
        self.client_controller.send_make_talk_room_user_id(talk_room_name, invite_member_list)

    def set_user_item_widget_to_scroll_layout(self):
        self.client_controller.clear_widget(self.invite_member_choice)  # 위젯 비우기

        friend_list = self.friend_list
        self.user_item_widget_list.clear()
        selected_user_item_to_invite_talk_room = self.user_item_widget_list
        for friend in friend_list:
            friend_profile = InviteUserItem(self, friend)
            selected_user_item_to_invite_talk_room.append(friend_profile)
            self.invite_member_choice_layout.addWidget(friend_profile)
