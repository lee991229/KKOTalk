from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, Qt, pyqtSignal

from Code.domain.class_db_connector import DBConnector
from Code.front.class_custom_message_box import NoFrameMessageBox
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
from Code.network.class_client import ClientApp
from Common.class_json import KKOEncoder, KKODecoder


class WindowController(QtWidgets.QWidget):
    # signal 클래스 변수
    assert_same_id_signal = pyqtSignal(bool)
    sign_up_signal = pyqtSignal(bool)
    log_in_signal = pyqtSignal(bool)
    enter_square_signal = pyqtSignal(bool)
    all_user_list_signal = pyqtSignal(str)
    user_talk_room_signal = pyqtSignal(str)
    talk_room_user_list_se_signal = pyqtSignal(str)
    out_talk_room_signal = pyqtSignal(bool)
    send_msg_se_signal = pyqtSignal(str)
    invite_user_talk_room_signal = pyqtSignal(bool)
    make_talk_room_signal = pyqtSignal(bool)

    def __init__(self, client_app=ClientApp):
        # assert isinstance(db_connector, DBConnector)
        super().__init__()
        self.client_app = client_app  # db연결 인스턴스
        self.client_app.set_widget(self)
        self.db_connector = None
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
        self.stored_user_list = list()  # 가입되어있는 모든 유저의 정보
        self.stored_talk_room_id_list = list()  # 로그인한 유저의 친구 리스트
        self.talk_room_related_user_id_list = list()
        self.stored_user_obj = None
        self.valid_duplication_id = None  # 중복 체크 여부 확인 변수 -> 기초 false set / 중복확인 후 결과 따라 True 됨
        self.join_id = None  # 회원가입에서 적힌 아이디
        self.join_pw = None  # 회원가입에서 적힌 비밀번호
        self.join_nickname = None  # 회원가입에서 적힌 닉네임
        self.encoder = KKOEncoder()
        self.decoder = KKODecoder()
        self.initial_trigger_setting()

        # ui 동작 관련 변수
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

    def get_user_self(self):
        return self.client_app.get_user_self()

    def get_user_by_id(self, user_id):
        return self.client_app.get_user_by_id(user_id)

    def send_make_talk_room_user_id(self, invite_member_list):
        # self.db_connector.
        # todo: 채팅방을 만들때 초대할 유저의 정보, 토크룸의 이름을 보낸다
        # 토크룸의 아이디를 받아온다
        pass

    def uninvited_user_list(self, talk_room_id):
        """
        todo: 만일 채팅방에서 초대되지 않은 인원을 파악하고자 할 때 유저 리스트를 반환함
        :param talk_room_id:
        :return:
        """

    def show_profile_page(self, user_id):
        self.client_app: ClientApp
        selected_user = [x for x in self.client_app.all_user_list_in_memory if x.user_id == user_id]
        selected_user = selected_user[0]
        self.widget_profile_window.set_profile_user_data(selected_user)
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

    # ==== 클라이언트 response 함수 ================================================================
    def initial_trigger_setting(self):
        self.valid_duplication_id = False
        self.assert_same_id_signal.connect(self.assert_same_name_res)
        self.sign_up_signal.connect(self.sign_up_res)
        self.log_in_signal.connect(self.log_in_res)
        self.enter_square_signal.connect(self.enter_square_res)
        self.all_user_list_signal.connect(self.all_user_list_res)
        self.user_talk_room_signal.connect(self.user_talk_room_list_res)
        self.talk_room_user_list_se_signal.connect(self.talk_room_user_list_se_res)
        self.out_talk_room_signal.connect(self.out_talk_room_res)
        self.send_msg_se_signal.connect(self.send_msg_se_res)
        self.invite_user_talk_room_signal.connect(self.invite_user_talk_room_res)
        self.make_talk_room_signal.connect(self.make_talk_room_res)

    # client function =================================
    # 클라 -> 서버 아이디 중복 체크 요청

    def assert_same_username(self, join_username):  # 아이디 중복
        self.client_app.send_join_id_for_assert_same_username(join_username)

    def assert_same_name_res(self, return_result: bool):
        if return_result is True:
            self.valid_duplication_id = True
            return NoFrameMessageBox(self, "가능", "중복 없는 아이디, 써도됌", "about")
        elif return_result is False:
            return NoFrameMessageBox(self, "불가능", "중복 아이디, 새로 쓰기", "about")

        # 클라 -> 서버 회원가입 요청

    def join_access(self):
        join_username = self.widget_join.lineEdit_join_username.text()
        join_pw = self.widget_join.lineedit_join_pw.text()
        join_nickname = self.widget_join.lineedit_join_user_nickname.text()
        self.client_app.send_join_id_and_pw_for_join_access(join_username, join_pw, join_nickname)

        # 서버 -> 클라 회원가입 결과 체크 결과 대응

    def sign_up_res(self, return_result: bool):
        if return_result is True:
            result = NoFrameMessageBox(self, "성공", "회원가입 성공", "about")
            self.widget_join.close()
            return
        elif return_result is False:
            return NoFrameMessageBox(self, "실패", "회원가입 실패", "about")

        #  클라 -> 서버 로그인 요청

    def assert_login_data(self, login_id, login_pw):
        """
        기능1:
        로그인 화면에서 로그인 승인 버튼에 시그널을 주면 서버에 ID,PW가 저장 되있고 일치여부 요청
        """
        self.client_app.user_id = None
        self.client_app.username = login_id
        self.client_app.user_pw = login_pw
        self.client_app.user_nickname = None
        self.client_app.send_login_id_and_pw_for_login_access(login_id, login_pw)

    def log_in_res(self, return_result: bool):
        if return_result is True:
            # 모든건 로그인 버튼을 누르면 시작한다. 나중에 수정
            # 받아와야할 정보 : 전체 회원 리스트, 본인이 포함된 톡방 리스트
            user_id = self.client_app.user_id
            username = self.client_app.username
            user_pw = self.client_app.user_pw
            user_nickname = self.client_app.user_nickname
            self.widget_friend_list_page.login_user_obj = User(user_id, username, user_pw, user_nickname)
            self.all_user_list()

            self.user_talk_room_list()
            self.talk_room_user_list_se()
            # self.out_talk_room()
            return NoFrameMessageBox(self, "성공", "login 성공", "about")
        elif return_result is False:
            return NoFrameMessageBox(self, "실패", "login 실패", "about")

        # 클라 -> 서버 초기 체팅방 입장, 로그인시 실행

    def enter_square(self):
        self.client_app.send_enter_square()
        # 전체 회원방 메시지 요청

        # 서버 -> 클라 초기 체팅방 입장 결과 체크

    def enter_square_res(self):
        # 화면 띄우기? 화면전환?
        # 전체 회원방 메시지 저장
        print("초기방 입장 완료")

        # 클라 -> 서버 유저 리스트 요청, 로그인시 할 수도있음

    def all_user_list(self):
        self.client_app.send_all_user_list()

        # 서버 -> 클라 유저 리스트 정보 받음

    def all_user_list_res(self, return_result: str):
        user_list = self.decoder.decode_any(return_result)
        self.widget_login_page.close()
        self.client_app.all_user_list_in_memory = user_list
        self.widget_friend_list_page.friend_list = user_list.copy()
        self.widget_friend_list_page.show()
        # 클라 -> 서버 채팅방 리스트 요청

    def get_talk_by_room_id(self, talk_room_id):
        return self.client_app.get_talk_by_room_id(talk_room_id)

    def user_talk_room_list(self):
        self.client_app.send_user_talk_room_list()

        # 서버 -> 클라 채팅방 리스트 정보 받음

    def user_talk_room_list_res(self, return_result: str):
        result_list = self.decoder.decode_any(return_result)
        self.client_app.talk_room_list = result_list
        self.widget_talk_room_list.talk_room_list.clear()
        self.widget_talk_room_list.talk_room_list = self.client_app.talk_room_list.copy()
        self.widget_talk_room_list.refresh_chat_room_list()

        # 클라 -> 서버 채팅방 관련 유저 정보 요청
        # 방 아이디를 넘겨줘야 할듯 하다.

    def talk_room_user_list_se(self):
        self.client_app.send_talk_room_user_list_se(1)

        # 서버 -> 클라 톡방 유저 객체 정보 획득

    def talk_room_user_list_se_res(self, return_result: str):
        user_list = self.decoder.decode_any(return_result)
        # print('방에 존재하는 유저 정보', user_list)

        # 클라 -> 서버 채팅방 나가기 요청
        # 방 아이디를 넘겨줘야 할듯 하다

    def out_talk_room(self):
        self.client_app.send_out_talk_room(talk_room_id)

        # 채팅방 나가기 결과 반환
        # 메세지 박스를 화면 전환 해주세요

    def out_talk_room_res(self, return_result: bool):
        if return_result is True:
            return NoFrameMessageBox(self, "성공", "방탈출 성공", "about")
        elif return_result is False:
            return NoFrameMessageBox(self.widget_join, "실패", "방탈출 실패", "about")
        # 화면 전환후 채팅방 목록 불러오기

        # 클라 -> 서버 메시지 전달

    def send_msg_se(self, talk_room_id, txt_message):
        self.client_app.send_send_msg_se(talk_room_id, txt_message)

        # 서버 -> 클라 메시지 받기

    def send_msg_se_res(self, return_result: str):
        message = self.decoder.decode_any(return_result)
        self.text_edit_chat_room.appendPlainText(
            f"{message.user_obj.nickname} : {message.contents} > {message.send_time_stamp}")
        # todo: send 메시지

        # 클라 -> 서버 단톡방 초대 요청

    def invite_user_talk_room(self):
        self.client_app.send_invite_user_talk_room(talk_room_id, invite_user)

        # 서버 -> 클라 단톡방 초대 완료

    def invite_user_talk_room_res(self, return_result: bool):
        print('초대완료')

        # 채팅방 개설하기

    def make_talk_room(self):
        # 시간은 어떻게 받을 지몰라서 그대로 둠. user_id도 같인 이유
        self.client_app.send_make_talk_room(room_name, guest_list, open_time_stmp)

    def make_talk_room_res(self, return_result: bool):
        print('개설완료')
        # 단톡방 리스트 갱신하는 파일 만들기

    def send_file_to_chat_room(self):
        save_excel_dialog = NoFrameMessageBox(self, "파일 업로드", "파일을 업로드합니까?", "question").result
        if save_excel_dialog is True:
            save_path_file_name, _, = QtWidgets.QFileDialog.getSaveFileName(self, '파일 저장', './')
            print(f"{save_path_file_name} send 로직 실행")
        # todo: send 메시지
