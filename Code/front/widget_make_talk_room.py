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
        self.user_item_widget_list = None
        self.user_set_talk_room_name = None
        # self.chacked_user_list = list()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    # def btn_is_chacked_check_false(self, invite_user_item):
    #     self.chacked_user_list.remove(invite_user_item)

    # def btn_is_chacked_check_true(self, invite_user_item):
    #     self.chacked_user_list.append(invite_user_item)

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
        self.set_friend_list()
        self.set_user_item_widget_to_scroll_layout()
        super().show()

    def set_friend_list(self):
        # todo : 친구 리스트 갱신해서 집어넣기
        self.friend_list = self.client_controller.friend_list

    def close(self):
        super().close()

    def set_btn_trigger(self):
        self.btn_flist_close.clicked.connect(lambda state: self.close())
        self.close_btn.clicked.connect(lambda state: self.close())
        self.decision_btn.clicked.connect(self.making_talk_room)

    # todo: 나중에 이름 바꿔
    def making_talk_room(self):
        '''
        확인 버튼을 누르면
        새로운 채팅방을 띄우는 함수 호출
        새로운 채팅방의
        서버에 초대를 원하는 유저의 user_id를 list로 보내주는 함수 호출
        클라이언트에 있는 self.open_talk_room_widget에 인스터스화한 채팅방(TalkRoomWidget)을 추가
        '''
        invite_member_list = list()
        for w in self.user_item_widget_list:
            if w.is_btn_checked():
                invite_member_list.append(w)
        print(invite_member_list)
        self.user_set_talk_room_name = self.lineEdit_user_set_talk_room_name.text()
        print(self.user_set_talk_room_name)
        self.send_user_id_list(invite_member_list)
        # todo: 위의 함수에서 받아온 톡룸아이디와 이름으로 톡룸ui를 띄워준다
        self.new_talk_room()
        self.close()
        # self.test3()

    def new_talk_room(self):
        '''
        새로운 채팅방 만들어서 띄워준다
        '''
        self.client_controller.open_talk_room_widget()

    def send_user_id_list(self, invite_member_list):
        '''
        서버에 초대를 원하는 유저의 user_id를 list로 보내준다
        todo: 이름 바꿔야한다
        '''
        invite_member_list = invite_member_list
        self.client_controller.send_make_talk_room_user_id(invite_member_list)
        # for i in invite_member_list:
        #     print(i.user_id)
        # pass

    def set_user_item_widget_to_scroll_layout(self):
        self.client_controller.clear_widget(self.invite_member_choice)  # 위젯 비우기

        friend_list = self.friend_list
        list_ = []
        for friend in friend_list:
            friend_profile = InviteUserItem(self, friend)
            list_.append(friend_profile)
            self.invite_member_choice_layout.addWidget(friend_profile)
        self.user_item_widget_list = list_
