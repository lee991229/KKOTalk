from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_talk_room_invite_user_list_in_chat_room import Ui_make_talk_room_widget
from Code.front.widget_invite_member import InviteUserItem


class TalkRoomMemberPlusWidget(QWidget, Ui_make_talk_room_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.friend_list = None
        self.talk_room_uninvite_user_list = list()
        self.user_item_widget_list = None
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    def set_talk_room_uninvite_user_list(self):
        self.talk_room_uninvite_user_list = self.client_controller.talk_room_uninvite_user_list
        print(self.talk_room_uninvite_user_list, '여기야 2')
        # self.talk_room_uninvite_user_list = uninvited_user_list

    def count_checked_user(self):
        count = 0
        for w in self.user_item_widget_list:
            if w.is_btn_checked():
                count += 1
        return count

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    def show(self):
        # todo: 채팅방에 없는 유저만 있는 리스트로 바꿔
        self.set_talk_room_uninvite_user_list()
        self.set_user_item_widget_to_scroll_layout()
        super().show()

    # def set_friend_list(self):
    #     # todo : 톡방에 없는 친구 리스트
    #     self.friend_list = self.client_controller.uninvited_friend_list()

    def close(self):
        super().close()

    def set_btn_trigger(self):
        self.btn_flist_close.clicked.connect(lambda state: self.close())
        self.close_btn.clicked.connect(lambda state: self.close())
        self.decision_btn.clicked.connect(self.user_invite_talk_room)

    # todo: 나중에 이름 바꿔
    def user_invite_talk_room(self):
        '''
        확인 버튼을 누르면
        채팅방에 유저를 초대하는 함수
        서버에 초대를 원하는 유저의 user_id를 list로 보내주는 함수 호출
        '''
        invite_member_list = list()
        for w in self.user_item_widget_list:
            if w.is_btn_checked():
                invite_member_list.append(w)

        # self.new_talk_room()
        self.send_user_id_list(invite_member_list)
        # self.test3()

    def user_plus(self):
        '''
        채팅방에 유저 추가해준다
        '''

    def send_user_id_list(self, invite_member_list):
        '''
        서버에 초대를 원하는 유저의 user_id를 list로 보내준다
        todo: 이름 바꿔야한다
        '''
        invite_member_list = invite_member_list
        for i in invite_member_list:
            print(i.user_id)
        pass

    def refresh_user_nickname_list_label(self):
        invite_user_nickname_list = list()
        for w in self.user_item_widget_list:
            if w.is_btn_checked():
                user_nickname = w.get_nickname()
                invite_user_nickname_list.append(user_nickname)
        return invite_user_nickname_list

    def set_user_item_widget_to_scroll_layout(self):
        self.client_controller.clear_widget(self.invite_member_choice)  # 위젯 비우기

        talk_room_uninvite_user_list = self.talk_room_uninvite_user_list
        list_ = []
        for uninvite_user in talk_room_uninvite_user_list:
            user_profile = InviteUserItem(self, uninvite_user)
            list_.append(user_profile)
            self.invite_member_choice_layout.addWidget(user_profile)
        self.user_item_widget_list = list_
