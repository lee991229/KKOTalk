from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

from Code.domain.class_db_connector import DBConnector
from Code.domain.class_user import User
from Code.network.class_worker_thread import WorkerServerThread
from Code.network.server_ui.ui_chat_room import Ui_prototype
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller
from Common.class_json import KKODecoder, KKOEncoder
from Common.common_module import *
from PyQt5.QtCore import pyqtSignal


class ClientPrototypeWidget(QtWidgets.QWidget, Ui_prototype):
    ENCODED_DOT = bytes('.', 'utf-8')
    ENCODED_PASS = bytes('pass', 'utf-8')

    # signal 클래스 변수

    assert_same_id_signal = pyqtSignal(bool)
    sign_up_signal = pyqtSignal(bool)
    log_in_signal = pyqtSignal(bool)
    enter_square_signal = pyqtSignal(bool)
    all_user_list_signal = pyqtSignal(str)
    user_talk_room_signal = pyqtSignal(str)
    talk_room_user_list_se_signal = pyqtSignal(int, str)
    out_talk_room_signal = pyqtSignal(bool)
    send_msg_se_signal = pyqtSignal(str)
    invite_user_talk_room_signal = pyqtSignal(bool)
    make_talk_room_signal = pyqtSignal(int)
    talk_room_msg_signal = pyqtSignal(str)

    def __init__(self, client_app):
        super().__init__()
        self.setupUi(self)
        self.client_app = client_app
        self.valid_duplication_id = False
        self.qthread = WorkerServerThread(self)
        self.set_btn_trigger()
        self.set_init_label()
        self.encoder = KKOEncoder()
        self.decoder = KKODecoder()
        self.set_client_know_each_other()

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
        self.talk_room_msg_signal.connect(self.talk_room_msg_res)

    def set_client_know_each_other(self):
        self.client_app.set_widget(self)

    def set_init_label(self):
        self.initialize_app()
        self.setWindowTitle("성혁이를 위한 프로토타입 위젯")

    def set_btn_trigger(self):
        self.btn_init.clicked.connect(lambda state: self.initialize_app())
        self.btn_check_same_id.clicked.connect(lambda state: self.assert_same_username())
        self.btn_join.clicked.connect(lambda state: self.join_access())
        self.btn_login.clicked.connect(lambda state: self.login_access())
        self.btn_send_message.clicked.connect(lambda state: self.send_msg_se())
        self.btn_transfer_file.clicked.connect(lambda state: self.send_file_to_chat_room())

    def initialize_app(self):
        self.btn_init.clicked.connect(lambda state: self.initialize_app())
        self.text_edit_chat_room.clear()
        self.text_edit_for_send_chat.clear()
        self.line_edit_for_join_id.clear()
        self.line_edit_for_join_pw.clear()
        self.line_edit_for_join_nick.clear()
        self.text_edit_chat_room.clear()
        self.valid_duplication_id = False

    # client function =================================
    # 클라 -> 서버 아이디 중복 체크 요청
    def assert_same_username(self):
        input_username = self.line_edit_for_join_id.text()
        self.client_app.send_join_id_for_assert_same_username(input_username)  # 헤더를 붙이고 보내는 동작(?)

    # 서버 -> 클라 아이디 중복 체크 결과 대응

    def assert_same_name_res(self, return_result: bool):

        if return_result is True:
            self.valid_duplication_id = True
            return QtWidgets.QMessageBox.about(self, "가능", "중복 없는 아이디, 써도됌")
        elif return_result is False:
            return QtWidgets.QMessageBox.about(self, "불가능", "중복 아이디, 새로 쓰기")

    # 클라 -> 서버 회원가입 요청
    def join_access(self):
        if self.valid_duplication_id is False:
            QtWidgets.QMessageBox.about(self, "어허", "아이디 중복확인 먼저 시행해주세요")
            return
        join_username = self.line_edit_for_join_id.text()
        join_pw = self.line_edit_for_join_pw.text()
        join_nickname = self.line_edit_for_join_nick.text()
        self.client_app.send_join_id_and_pw_for_join_access(join_username, join_pw, join_nickname)

    # 서버 -> 클라 회원가입 결과 체크 결과 대응
    def sign_up_res(self, return_result: bool):
        if return_result is True:
            return QtWidgets.QMessageBox.about(self, "성공", "회원가입 성공")
        elif return_result is False:
            return QtWidgets.QMessageBox.about(self, "실패", "회원가입 실패")

    #  클라 -> 서버 로그인 요청
    def login_access(self):
        login_username = self.line_edit_for_login_id.text()
        login_pw = self.line_edit_for_login_pw.text()
        self.client_app.send_login_id_and_pw_for_login_access(login_username, login_pw)

    # 서버 -> 클라 로그인 결과 체크 결과 대응
    def log_in_res(self, return_result: bool):
        if return_result is True:
            # 모든건 로그인 버튼을 누르면 시작한다. 나중에 수정
            self.enter_square()
            self.all_user_list()
            self.user_talk_room_list()
            self.talk_room_user_list_se()
            # self.out_talk_room()
            self.talk_room_msg()
            return QtWidgets.QMessageBox.about(self, "성공", "login 성공")
        elif return_result is False:
            return QtWidgets.QMessageBox.about(self, "실패", "login 실패")

    # 클라 -> 서버 초기 체팅방 입장, 로그인시 실행
    def enter_square(self):
        self.client_app.send_enter_square()

    # 서버 -> 클라 초기 체팅방 입장 결과 체크
    def enter_square_res(self):
        # 화면 띄우기? 화면전환?
        print("초기방 입장 완료")

    # 클라 -> 서버 유저 리스트 요청, 로그인시 할 수도있음
    def all_user_list(self):
        self.client_app.send_all_user_list()

    # 서버 -> 클라 유저 리스트 정보 받음
    def all_user_list_res(self, return_result: str):
        all_user_list = self.decoder.decode(return_result)
        print('가입한 유저 정보', all_user_list)

    # 클라 -> 서버 채팅방 리스트 요청
    def user_talk_room_list(self):
        self.client_app.send_user_talk_room_list()

    # 서버 -> 클라 채팅방 리스트 정보 받음
    def user_talk_room_list_res(self, return_result: str):
        talk_room_list = self.decoder.decode(return_result)
        print('존재하는 방 리스트', talk_room_list)

    # 클라 -> 서버 채팅방 관련 유저 정보 요청
    # 방 아이디를 넘겨줘야 할듯 하다.
    def talk_room_user_list_se(self):
        # self.client_app.send_talk_room_user_list_se(talk_room_id)
        pass

    # 서버 -> 클라 톡방 유저 객체 정보 획득
    def talk_room_user_list_se_res(self, talk_room_id:int, return_result: str):
        user_list = self.decoder.decode(return_result)

        print('방에 존재하는 유저 정보', user_list)

    # 클라 -> 서버 채팅방 나가기 요청
    # 방 아이디를 넘겨줘야 할듯 하다
    def out_talk_room(self):
        # self.client_app.send_out_talk_room(talk_room_id)
        pass

    # 채팅방 나가기 결과 반환
    # 메세지 박스를 화면 전환 해주세요
    def out_talk_room_res(self, return_result: bool):
        if return_result is True:
            return QtWidgets.QMessageBox.about(self, "성공", "방탈출 성공")
        elif return_result is False:
            return QtWidgets.QMessageBox.about(self, "실패", "방탈출 실패")
        # 화면 전환후 채팅방 목록 불러오기

    # 클라 -> 서버 메시지 전달
    def send_msg_se(self):
        txt_message = self.text_edit_for_send_chat.toPlainText()
        self.text_edit_for_send_chat.clear()
        self.text_edit_chat_room.appendPlainText(txt_message)
        self.client_app.send_send_msg_se(1, txt_message)

    # 서버 -> 클라 메시지 받기
    def send_msg_se_res(self, return_result: str):
        message = self.decoder.decode_any(return_result)
        self.text_edit_chat_room.appendPlainText(
            f"{message.user_obj.nickname} : {message.contents} > {message.send_time_stamp}")
        # todo: send 메시지

    # 클라 -> 서버 단톡방 초대 요청
    def invite_user_talk_room(self):
        # self.client_app.send_invite_user_talk_room(talk_room_id, invite_user)
        pass

    # 서버 -> 클라 단톡방 초대 완료
    def invite_user_talk_room_res(self, return_result: bool):
        print('초대완료')

    # 채팅방 개설하기
    def make_talk_room(self):
        # 시간은 어떻게 받을 지몰라서 그대로 둠. user_id도 같인 이유
        # self.client_app.send_make_talk_room(room_name, guest_list, open_time_stmp)
        pass

    def make_talk_room_res(self, return_result: bool):
        print('개설완료')
        # 단톡방 리스트 갱신하는 파일 만들기

    # 채팅방 입장시 클라 -> 서버 이전 message 내용 전송
    def talk_room_msg(self):
        self.client_app.send_talk_room_msg(talk_room_id=1)
    
    # 서버 -> 클라 message obj 내용 받기
    def talk_room_msg_res(self, return_result: str):
        room_msg = self.decoder.decode_any(return_result)
        # 오브젝트들 잘 나오는지 확인
        for i in room_msg:
            print(i)

    def send_file_to_chat_room(self):
        save_excel_dialog = QtWidgets.QMessageBox.question(self, "파일 업로드", "파일을 업로드합니까?")
        if save_excel_dialog == QtWidgets.QMessageBox.Yes:
            save_path_file_name, _, = QtWidgets.QFileDialog.getSaveFileName(self, '파일 저장', './')
            print(f"{save_path_file_name} send 로직 실행")
        # todo: send 메시지
