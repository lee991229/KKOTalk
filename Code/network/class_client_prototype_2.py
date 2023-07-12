from PyQt5 import QtCore, QtGui, QtWidgets
from threading import *

from PyQt5.QtCore import pyqtSignal, QThread

from Code.domain.class_db_connector import DBConnector
from Code.domain.class_user import User
from Code.network.class_worker_thread import WorkerServerThread
from Code.network.server_ui.ui_chat_room import Ui_prototype
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller
from Common.class_json import KKODecoder, KKOEncoder
from Common.common_module import *


class ClientPrototypeWidget2(QtWidgets.QWidget, Ui_prototype):
    ENCODED_DOT = bytes('.', 'utf-8')
    ENCODED_PASS = bytes('pass', 'utf-8')

    def __init__(self, client_app):
        super().__init__()
        self.setupUi(self)
        self.client_app = client_app
        self.valid_duplication_id = False
        self.qthread = WorkerServerThread(self)
        self.set_btn_trigger()
        self.plaintext = list()
        self.set_init_label()
        self.encoder = KKOEncoder()
        self.decoder = KKODecoder()

    def set_init_label(self):
        self.initialize_app()
        self.setWindowTitle("성혁이를 위한 프로토타입 위젯")
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(lambda: self.text_edit_chat_room.setPlainText("\n".join(self.plaintext)))
        self.timer.start()

    def set_btn_trigger(self):
        self.btn_init.clicked.connect(lambda state: self.initialize_app())
        self.btn_check_same_id.clicked.connect(lambda state: self.send_join_id_for_assert_same_username())
        self.btn_join.clicked.connect(lambda state: self.send_join_id_and_pw_for_join_access())
        self.btn_login.clicked.connect(lambda state: self.send_login_id_and_pw_for_login_access())
        self.btn_send_message.clicked.connect(lambda state: self.send_message_to_chat_room())
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
        self.plaintext.clear()
        print(self.plaintext)

    # client function =================================
    def send_join_id_for_assert_same_username(self):
        input_username = self.line_edit_for_join_id.text()
        self.client_app.send(b"/assert_username")  # 헤더를 붙이고 보내는 동작(?)
        self.client_app.recv(1024)  # "." 받음
        self.client_app.send(input_username.encode())  # 실제 내용을 붙여서 보내는 동작
        return_result = self.client_app.recv(1024).decode('utf-8')  # 응답 받기
        if return_result == 'pass':
            self.valid_duplication_id = True
            return QtWidgets.QMessageBox.about(self, "가능", "중복 없는 아이디, 써도됌")
        elif return_result == '.':
            return QtWidgets.QMessageBox.about(self, "불가능", "중복 아이디, 새로 쓰기")

    def send_join_id_and_pw_for_join_access(self):
        if self.valid_duplication_id is False:
            QtWidgets.QMessageBox.about(self, "어허", "아이디 중복확인 먼저 시행해주세요")
            return
        join_username = self.line_edit_for_join_id.text()
        join_pw = self.line_edit_for_join_pw.text()
        join_nickname = self.line_edit_for_join_nick.text()
        join_user = User(None, join_username, join_pw, join_nickname)
        user_json_str = join_user.toJSON()
        self.client_app.send("/join_user")
        self.client_app.recv(1024)  # "." 받음
        self.client_app.send(user_json_str.encode())
        return_result = self.client_app.recv(1024).decode('utf-8')  # 응답 받기
        if return_result == 'pass':
            return QtWidgets.QMessageBox.about(self, "성공", "회원가입 성공")
        elif return_result == '.':
            return QtWidgets.QMessageBox.about(self, "실패", "회원가입 실패")

    def send_login_id_and_pw_for_login_access(self):
        self.client_app.connect_to_surver()
        login_username = self.line_edit_for_login_id.text()
        login_pw = self.line_edit_for_login_pw.text()
        sending_message = login_username + '%' + login_pw
        # self.client_app.client.send("/login".encode())
        # self.client_app.client.recv(1024)  # "." 받음
        self.client_app.client.send(sending_message.encode())
        return_result = self.client_app.client.recv(1024).decode('utf-8')  # 응답 받기
        if return_result == 'pass':
            self.client_app.test_start()
            self.test = Thread(target=self.recv_message_to_chat_room)
            self.test.start()
            return QtWidgets.QMessageBox.about(self, "성공", "login 성공")
        elif return_result == '.':
            self.client_app.disconnect_to_surver()
            return QtWidgets.QMessageBox.about(self, "실패", "login 실패")

    def send_message_to_chat_room(self):
        txt_message = self.text_edit_for_send_chat.toPlainText()
        self.text_edit_for_send_chat.clear()
        self.client_app.client.send(txt_message.encode('utf-8'))
        # todo: send 메시지

    def recv_message_to_chat_room(self):
        while True:
            if self.client_app.message is not None:
                recv_message = self.client_app.message
                self.plaintext.append(recv_message)
                # self.text_edit_chat_room.appendPlainText(recv_message)
                self.client_app.message = None

    def send_file_to_chat_room(self):
        save_excel_dialog = QtWidgets.QMessageBox.question(self, "파일 업로드", "파일을 업로드합니까?")
        if save_excel_dialog == QtWidgets.QMessageBox.Yes:
            save_path_file_name, _, = QtWidgets.QFileDialog.getSaveFileName(self, '파일 저장', './')
            print(f"{save_path_file_name} send 로직 실행")
        # todo: send 메시지
