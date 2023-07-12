from Code.domain.class_db_connector import DBConnector
from Code.front.widget_friend_list_page import FriendListWidget
from Code.front.widget_join_page import JoinWidget
from Code.front.widget_login_page import LoginWidget
from Code.front.widget_talk_room_list_page import TalkRoomListWidget
from Code.front.widget_make_talk_room import InviteFriendListWidget
from Code.front.widget_talk_room_page import TalkRoomWidget
from Code.front.widget_search_talk_room_member_list_page import SearchMemberListWidget
from Code.front.widget_talk_room_member_plus_page import TalkRoomMemberPlusWidget


class WindowController:
    def __init__(self, db_connector=None):
        assert isinstance(db_connector, DBConnector)
        super().__init__()
        self.db_connector = db_connector  # db연결 인스턴스
        # Domain 인스턴스
        # self.login_user =   # 스케줄러 페이지
        self.login_page = LoginWidget(self)  # 로그인 화면 ui 클래스 함수화
        self.friend_list_page = FriendListWidget(self)  # 친구창 ui 클래스 함수화
        self.join_widget = JoinWidget(self)  # 회원 가입창 ui 클래스 함수화
        self.talk_room_list = TalkRoomListWidget(self)
        self.talk_room = TalkRoomWidget(self)
        self.make_talk_room = InviteFriendListWidget(self)
        self.room_member_list = SearchMemberListWidget(self)
        self.member_plus = TalkRoomMemberPlusWidget(self)

        self.join_id = None
        self.join_pw = None
        self.join_ninkname = None
    def join_success(self):
        """
        회원가입 성공시
        :return:
        """
        #todo:'DB에 회원가입 정보 집어넣는 기능'
        pass
    def id_duplicate_check(self):
        """
        회원가입 화면 아이디 중복체크 메서드
        """
        # todo:'db에 중복되는 아이디가 있는지 찾아본다'
        return True

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
        확인하는 메서드 저장,일치 한다면 True를 넘겨준다
        기능2:
        아이디,비밀번호가 일치하지 않거나 적지 않았을때 hide 라벨을 show해주고 라벨에 안내문구를 띄워준다

        login_id = 유저가 입력한 아이디
        login_pw = 유저가 입력한 비밀번호
        db_id = db에 저장된 id들
        db_pw = db에 저장된 password들
        """

        db_id = '1234'
        db_pw = '1234'
        if db_id == login_id and db_pw == login_pw:
            return True

        self.login_page.label_warning.show()

        if db_id != login_id:  # 아이디 칸이 비어 있거나 잘못 적었을때
            if len(login_id) == 0:
                self.login_page.no_input_id()
            else:
                self.login_page.none_id()

        elif db_pw != login_pw:  # 비밀 번호 칸이 비어 있거나 잘못 적었을때
            if len(login_pw) == 0:
                self.login_page.no_input_pw()
            else:
                self.login_page.none_pw()

    def show_login_success(self):
        """
        로그인 승인 성공시(True) 친구창,채팅방 띄우는 메서드
        """
        self.friend_list_page.show()  # 친구창 띄우는 함수
        self.talk_room.show()  # 채팅방 띄우는 함수
    def get_friend_list(self):
        #todo:데이터 베이스에서 리스트 가져오기
        # self.db_connector.
        pass