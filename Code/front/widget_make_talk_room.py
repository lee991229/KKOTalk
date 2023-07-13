from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_make_talk_room_ui import Ui_make_talk_room_widget
from Code.front.widget_invite_member import InviteMemberWidget


class InviteFriendListWidget(QWidget, Ui_make_talk_room_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.friend_list = None
        self.obj_list = None

    def show(self):
        self.friend_list = self.client_controller.friend_list
        self.test1()
        super().show()

    def set_btn_trigger(self):
        self.decision_btn.clicked.connect(self.test2)

    # todo: 나중에 이름 바꿔
    def test2(self):
        '''
        확인 버튼을 누르면
        새로운 채팅방을 띄우는 함수 호출
        서버에 초대를 원하는 유저의 user_id를 list로 보내주는 함수 호출
        클라이언트에 있는 self.open_talk_room_widget에 인스터스화한 채팅방(TalkRoomWidget)을 추가
        '''
        invite_member_list = list()
        for w in self.obj_list:
            if w.is_btn_checked():
                invite_member_list.append(w)

        self.new_talk_room()
        self.test3(invite_member_list)
        self.close()
        # self.test3()

    def new_talk_room(self):
        '''
        새로운 채팅방 만들어서 띄워준다
        '''
        new_talk_widget = self.client_controller.open_talk_room()
        new_talk_widget.show()

    def test3(self, invite_member_list):
        '''
        서버에 초대를 원하는 유저의 user_id를 list로 보내준다
        todo: 이름 바꿔야한다
        '''
        invite_member_list = invite_member_list
        for i in invite_member_list:
            print(i.user_id)
        pass

    def test1(self):
        self.client_controller.clear_widget(self.invite_member_choice) # 위젯 비우기

        friend_list = self.friend_list
        list_ = []
        for friend in friend_list:
            friend_profile = InviteMemberWidget(self, friend)
            list_.append(friend_profile)
            self.invite_member_choice_layout.addWidget(friend_profile)
        self.obj_list = list_
