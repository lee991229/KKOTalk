from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint, Qt

from Code.domain.class_db_connector import DBConnector
from Code.front.widget_friend_list_page import FriendListWidget
from Code.front.widget_join_page import JoinWidget
from Code.front.widget_login_page import LoginWidget
from Code.front.widget_talk_room_list_page import TalkRoomListWidget
from Code.front.widget_make_talk_room import InviteFriendListWidget
from Code.front.widget_talk_room_page import TalkRoomWidget
from Code.front.widget_search_talk_room_member_list_page import UserListWidgetInTalkRoom
from Code.front.widget_talk_room_member_plus_page import TalkRoomMemberPlusWidget
from Code.front.widget_profile_page import ProfilePage

from Code.domain.class_user import User


class WindowController():
    def __init__(self, db_connector=DBConnector):
        # assert isinstance(db_connector, DBConnector)
        super().__init__()
        self.db_connector = db_connector  # db연결 인스턴스
        # Domain 인스턴스
        self.widget_login_page = LoginWidget(self)  # 로그인 화면 ui 클래스 함수화
        self.widget_friend_list_page = FriendListWidget(self)  # 친구창 ui 클래스 함수화
        self.widget_join = JoinWidget(self)  # 회원 가입창 ui 클래스 함수화
        self.widget_talk_room_list = TalkRoomListWidget(self)
        self.widget_ask_to_make_talk_room = InviteFriendListWidget(self)
        self.widget_room_member_list = UserListWidgetInTalkRoom(self)
        self.widget_add_member_in_chat_room = TalkRoomMemberPlusWidget(self)
        self.widget_profile_window = ProfilePage(self)
        self.widget_talk_room = TalkRoomWidget(self, 1)
        self.all_user = None  # 가입되어있는 모든 유저의 정보
        self.friend_list = None  # 로그인한 유저의 친구 리스트
        self.login_user_obj = None
        self.talk_room_uninvite_user_list = list()
        self.join_id = None  # 회원가입에서 적힌 아이디
        self.join_pw = None  # 회원가입에서 적힌 비밀번호
        self.join_nickname = None  # 회원가입에서 적힌 닉네임
        self.saved_talk_room_list = list()  # todo : 클라이언트 합칠 때 변경
        self.get_all_user_list()  # 유저 정보 가져오는 함수 # todo : 클라이언트 합칠 때 변경
        self.get_user_talk_room_list()  # 유저 정보 가져오는 함수 # todo : 클라이언트 합칠 때 변경
        self.list_widget_geometry_x = None
        self.list_widget_geometry_y = None
        self.drag_start_position = QPoint(0, 0)

    def mousePressEvent(self, widget, event):
        self.drag_start_position = QPoint(widget.x(), widget.y())
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - widget.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, widget, event):
        if event.buttons() == Qt.LeftButton:
            widget.move(event.globalPos() - self.drag_start_position)
            event.accept()

    def send_make_talk_room_user_id(self, invite_member_list):
        # self.db_connector.
        # todo: 채팅방을 만들때 초대할 유저의 정보, 토크룸의 이름을 보낸다
        # 토크룸의 아이디를 받아온다
        pass

    def uninvited_user_list(self, talk_room_id):
        # print(talk_room_id)
        uninvited_user_list = self.db_connector.uninvited_users_from_talk_room(talk_room_id)
        self.talk_room_uninvite_user_list = uninvited_user_list
        print(self.talk_room_uninvite_user_list,'여기야')

    def try_join(self):
        """
        회원가입 성공시
        :return:
        """
        # 유저가 입력안 id,pw,ninkname
        join_user = User(None, self.join_id, self.join_pw, self.join_nickname)
        self.db_connector.insert_user(join_user)
        pass

    def id_duplicate_check(self):  # 아이디 중복
        all_user = self.all_user
        coice_id = self.join_id

        for user_id in all_user:
            if user_id.username == coice_id:
                self.join_id = None
                return False
        return True

    def show_profile_page(self, user_id):
        friend_profile = self.db_connector.find_user_by_user_id(user_id)
        self.widget_profile_window.set_profile_user_data(friend_profile)
        self.widget_profile_window.show()

    def show_talk_room(self, talk_room_id):
        """
        채팅방 보여주는 메서드
        채팅방에 초대 되어있지 않은 유저 목록 저장
        :return:
        """
        self.uninvited_user_list(talk_room_id)
        self.widget_talk_room.set_talk_room_id(talk_room_id)
        self.widget_talk_room.show()

    # def get_friend_profile(self):

    def show_friend_list(self):
        """
        친구창 보여주는 메서드
        :return:
        """
        cp = self.widget_talk_room_list.frameGeometry().topLeft()
        cp: QPoint
        self.list_widget_geometry_x = cp.x()
        self.list_widget_geometry_y = cp.y()
        self.widget_friend_list_page.setGeometry(self.list_widget_geometry_x, self.list_widget_geometry_y,
                                                 self.widget_friend_list_page.width(),
                                                 self.widget_friend_list_page.height())
        self.widget_friend_list_page.show()

    def show_member_plus(self):
        """
        채팅방에 멤버추가 위젯 보여주는 메서드
        :return:
        """
        self.widget_add_member_in_chat_room.show()

    def show_room_member_list(self):
        """
        채팅방에 있는 멤버 목록을 보여주는 메서드
        :return:
        """
        self.widget_room_member_list.show()

    def show_make_talk_room(self):
        """
        채팅방 만드는 위젯 보여주는 메서드
        :return:
        """
        self.widget_ask_to_make_talk_room.show()

    def show_talk_room_list_page(self):
        """
        채팅방 보여주는 메서드
        :return:
        """
        cp = self.widget_friend_list_page.frameGeometry().topLeft()
        cp: QPoint
        self.list_widget_geometry_x = cp.x()
        self.list_widget_geometry_y = cp.y()
        self.widget_talk_room_list.setGeometry(self.list_widget_geometry_x, self.list_widget_geometry_y,
                                               self.widget_talk_room_list.width(),
                                               self.widget_talk_room_list.width())
        self.widget_talk_room_list.show()

    # 채팅방 리스트 화면 띄우는 메서드
    def show_join_page(self):
        """
        회원 가입창 띄우는 메서드
        """
        self.widget_join.show()

    def run(self):
        """
        로그인 화면 띄우는 메서드
        """
        self.widget_login_page.show()

    def assert_login_data(self, login_id, login_pw):
        """
        기능1:
        로그인 화면에서 로그인 승인 버튼에 시그널을 주면 DB에 ID,PW가 저장 되있고 일치 하는지
        확인하는 메서드
        """
        login_user_obj = self.db_connector.user_log_in(login_id=login_id, login_pw=login_pw)

        if len(login_id) == 0:  # 아이디 칸이 비어 있거나 잘못 적었을때
            self.widget_login_page.no_input_id()
        elif len(login_pw) == 0:  # 비밀 번호 칸이 비어 있거나 잘못 적었을때
            self.widget_login_page.no_input_pw()
        elif isinstance(login_user_obj, User) is False:  # 아이디와 비밀번호가 틀렸을때
            self.widget_login_page.none_id_pw()
        elif isinstance(login_user_obj, User):
            self.login_user_obj = login_user_obj  # 컨트롤러 로그인 유저 인스턴스 저장
            self.get_all_user_list()
            self.get_friend_list()
            return login_user_obj

        self.widget_login_page.label_warning.show()

    def show_login_success(self):
        # todo: 친구창과 채팅방을 띄울때 본인의 정보를 따로 처리해야한다
        self.widget_friend_list_page.show()  # 친구창 띄우는 함수
        # self.talk_room.show()  # 채팅방 띄우는 함수

    @staticmethod
    def clear_widget(widget):
        if widget.layout() is not None:
            while widget.layout().count() > 0:
                item = widget.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

    # 레이아웃 안에있는 위젯들 삭제
    def open_one_to_one_chat_room(self, target_user_id):
        self.open_talk_room_widget(target_user_id)

    def open_talk_room_widget(self, talk_room_id: int = None):
        # 검증로직
        # 만약 이미 열려있는 대화창이라면, 다시 열어야할까? 톡방을 열때
        # talk_room_id = 1
        self.widget_talk_room.show()

    def get_user_talk_room_list(self):
        talk_room_list = self.db_connector.find_user_talk_room_by_user_id(1)
        # print(talk_room_list)
        self.saved_talk_room_list = talk_room_list

    def get_all_user_list(self):
        result_list = self.db_connector.find_all_user()
        self.all_user = result_list

    # 모든 유저 정보와 친구리스트 저장
    def get_friend_list(self):
        friend_list = list()
        result_list = self.all_user
        login_user_id = self.login_user_obj.user_id

        for friend in result_list:
            if friend.user_id != login_user_id:
                friend_list.append(friend)

        self.friend_list = friend_list
