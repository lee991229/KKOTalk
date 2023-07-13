from Code.domain.class_db_connector import DBConnector
from Code.front.widget_friend_list_page import FriendListWidget
from Code.front.widget_join_page import JoinWidget
from Code.front.widget_login_page import LoginWidget
from Code.front.widget_talk_room_list_page import TalkRoomListWidget
from Code.front.widget_make_talk_room import InviteFriendListWidget
from Code.front.widget_talk_room_page import TalkRoomWidget
from Code.front.widget_search_talk_room_member_list_page import SearchMemberListWidget
from Code.front.widget_talk_room_member_plus_page import TalkRoomMemberPlusWidget
from Code.front.widget_profile_page import ProfilePage

from Code.domain.class_user import User


class WindowController:
    def __init__(self, db_connector=DBConnector):
        # assert isinstance(db_connector, DBConnector)
        super().__init__()
        self.db_connector = db_connector  # db연결 인스턴스
        # Domain 인스턴스
        # self.login_user =   # 스케줄러 페이지
        self.login_page = LoginWidget(self)  # 로그인 화면 ui 클래스 함수화
        self.friend_list_page = FriendListWidget(self)  # 친구창 ui 클래스 함수화
        self.join_widget = JoinWidget(self)  # 회원 가입창 ui 클래스 함수화
        self.talk_room_list = TalkRoomListWidget(self)
        # self.talk_room = TalkRoomWidget(self)
        self.make_talk_room = InviteFriendListWidget(self)
        self.room_member_list = SearchMemberListWidget(self)
        self.member_plus = TalkRoomMemberPlusWidget(self)
        self.profile_page = ProfilePage(self)
        # self.profilewidget = ProfileWidget(self, self.db_connector)
        self.all_user = None
        self.friend_list = None
        self.login_user_obj = None
        self.join_id = None
        self.join_pw = None
        self.join_ninkname = None
        self.get_all_user_list()
        self.open_talk_room_widget = list()

    def open_talk_room(self):
        # print(TalkRoomWidget(self))
        new_talk_room = TalkRoomWidget(self)
        self.open_talk_room_widget.append(new_talk_room)
        return new_talk_room

    def join_success(self):
        """
        회원가입 성공시
        :return:
        """
        join_user = User(None, str(self.join_id), str(self.join_pw), str(self.join_ninkname))
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
        self.profile_page.set_profile_user_data(friend_profile)
        self.profile_page.show()

    # def get_friend_profile(self):

    def show_talk_room(self):
        """
        채팅방 보여주는 메서드
        :return:
        """
        self.talk_room.show()

    def show_friend_list(self):
        """
        친구창 보여주는 메서드
        :return:
        """
        self.friend_list_page.show()

    def show_member_plus(self):
        """
        채팅방에 멤버추가 위젯 보여주는 메서드
        :return:
        """
        self.member_plus.show()

    def show_room_member_list(self):
        """
        채팅방에 있는 멤버 목록을 보여주는 메서드
        :return:
        """
        self.room_member_list.show()

    def show_make_talk_room(self):
        """
        채팅방 만드는 위젯 보여주는 메서드
        :return:
        """
        self.make_talk_room.show()

    # 채팅방 리스트 화면 띄우는 메서드
    def show_talk_room_list_page(self):
        """
        채팅방 보여주는 메서드
        :return:
        """
        self.talk_room_list.show()

    def show_join_page(self):
        """
        회원 가입창 띄우는 메서드
        """
        self.join_widget.show()

    def run(self):
        """
        로그인 화면 띄우는 메서드
        """
        self.login_page.show()

    def assert_login_data(self, login_id, login_pw):
        """
        기능1:
        로그인 화면에서 로그인 승인 버튼에 시그널을 주면 DB에 ID,PW가 저장 되있고 일치 하는지
        확인하는 메서드
        """
        login_user_obj = self.db_connector.user_log_in(login_id=login_id, login_pw=login_pw)

        if len(login_id) == 0:  # 아이디 칸이 비어 있거나 잘못 적었을때
            self.login_page.no_input_id()
        elif len(login_pw) == 0:  # 비밀 번호 칸이 비어 있거나 잘못 적었을때
            self.login_page.no_input_pw()
        elif isinstance(login_user_obj, User) is False:  # 아이디와 비밀번호가 틀렸을때
            self.login_page.none_id_pw()
        elif isinstance(login_user_obj, User):
            self.login_user_obj = login_user_obj  # 컨트롤러 로그인 유저 인스턴스 저장
            self.get_all_user_list()
            self.get_friend_list()
            return login_user_obj

        self.login_page.label_warning.show()

    def show_login_success(self):
        # todo: 친구창과 채팅방을 띄울때 본인의 정보를 따로 처리해야한다
        self.friend_list_page.show()  # 친구창 띄우는 함수
        # self.talk_room.show()  # 채팅방 띄우는 함수

    # 레이아웃 안에있는 위젯들 삭제
    def clear_widget(self, widget):
        if widget.layout() is not None:
            while widget.layout().count() > 0:
                item = widget.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

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
