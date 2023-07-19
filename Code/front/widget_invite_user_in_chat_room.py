from Code.front.widget_profile_item import ProfileItemWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_widget_talk_room_invite_user_list_in_chat_room import Ui_make_talk_room_widget
from Code.front.widget_invite_member import InviteUserItem


class InviteFriendListWidgetInTalkRoom(QWidget, Ui_make_talk_room_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.friend_list = None
        self.user_item_widget_list = None
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

    # 톡방 없는 유저 리스트 채우기
    def set_not_yet_invited_user_widget(self):
        not_invited_user_list = self.client_controller.get_not_yet_invited_user_list()
        layout_to_add = self.invite_member_choice.layout()
        if layout_to_add is None:
            layout_to_add = QtWidgets.QVBoxLayout(self)
            # self.invite_member_choice.
        for user in not_invited_user_list:
            widget_user_profile = ProfileItemWidget(self, user)
            # self.invite_member_choice
    def show(self):
        self.set_not_yet_invited_user_widget()
        self.set_user_item_widget_to_scroll_layout()
        super().show()


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

        user_list = self.client_controller.get_not_yet_invited_user_list()
        list_ = []
        for not_yet_user in user_list:
            user_profile = InviteUserItem(self, not_yet_user)
            list_.append(user_profile)
            self.invite_member_choice_layout.addWidget(user_profile)
        self.user_item_widget_list = list_
