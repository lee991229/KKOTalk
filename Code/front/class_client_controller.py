from Code.domain.class_db_connector import DBConnector
from Code.front.widget_friend_list_page import FriendListWidget
from Code.front.widget_join_page import JoinWidget
from Code.front.widget_login_page import LoginWidget
from Code.front.widget_talk_room_list_page import TalkRoomListWidget

class WindowController:
    def __init__(self, db_connector=None):
        super().__init__()
        self.db_connector = db_connector  # db연결 인스턴스
        # Domain 인스턴스
        # self.login_user =   # 스케줄러 페이지
        self.login_page = LoginWidget(self)  # 로그인 화면 ui 클래스 함수화
        self.friend_list_page = FriendListWidget(self)  # 친구창 ui 클래스 함수화
        self.join_widget = JoinWidget(self)  # 회원 가입창 ui 클래스 함수화
        self.talk_room_list = TalkRoomListWidget(self)
        self.join_id = None
        self.join_pw = None
        self.join_ninkname = None

    def id_duplicate_check(self, choice_id):
        """
        회원가입 화면 아이디 중복체크 메서드
        """
        #todo:'db에 중복되는 아이디가 있는지 찾아본다'
        return True

    def show_join_page(self):
        '''
        회원 가입창 띄우는 메서드
        '''
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

        if db_id != login_id:  # 아이디칸이 비어있거나 잘못적었을때
            if len(login_id) == 0:
                self.login_page.no_input_id()
            else:
                self.login_page.none_id()
        elif db_pw != login_pw: # 비밀번호칸이 비어있거나 잘못적었을때
            if len(login_pw) == 0:
                self.login_page.label_warning.setText("비밀번호를 적어주세요")
            else:
                self.login_page.label_warning.setText("비밀번호가 일치하지 않습니다")


    def show_login_success(self):
        """
        로그인 승인 성공시(True) 친구창 화면 띄우는 메서드
        """
        self.friend_list_page.show()