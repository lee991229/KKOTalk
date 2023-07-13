from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

from Code.domain.class_db_connector import DBConnector
from Code.domain.class_user import User
from Code.network.class_worker_thread import WorkerServerThread
from Code.network.server_ui.ui_chat_room import Ui_prototype
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller
from Common.class_json import KKODecoder, KKOEncoder
from Common.common_module import *


class ClientPrototypeWidget(QtWidgets.QWidget, Ui_prototype):
    ENCODED_DOT = bytes('.', 'utf-8')
    ENCODED_PASS = bytes('pass', 'utf-8')

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

    def set_init_label(self):
        self.initialize_app()
        self.setWindowTitle("성혁이를 위한 프로토타입 위젯")

    def set_btn_trigger(self):
        self.btn_init.clicked.connect(lambda state: self.initialize_app())
        self.btn_check_same_id.clicked.connect(lambda state: self.assert_same_username())
        self.btn_join.clicked.connect(lambda state: self.join_access())
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

    # client function =================================
    def assert_same_username(self):
        input_username = self.line_edit_for_join_id.text()
        return_result = self.client_app.send_join_id_for_assert_same_username(input_username)  # 헤더를 붙이고 보내는 동작(?)
        if return_result is True:
            self.valid_duplication_id = True
            return QtWidgets.QMessageBox.about(self, "가능", "중복 없는 아이디, 써도됌")
        elif return_result is False:
            return QtWidgets.QMessageBox.about(self, "불가능", "중복 아이디, 새로 쓰기")

    def join_access(self):
        if self.valid_duplication_id is False:
            QtWidgets.QMessageBox.about(self, "어허", "아이디 중복확인 먼저 시행해주세요")
            return
        join_username = self.line_edit_for_join_id.text()
        join_pw = self.line_edit_for_join_pw.text()
        join_nickname = self.line_edit_for_join_nick.text()
        return_result = self.client_app.send_join_id_and_pw_for_join_access(join_username, join_pw, join_nickname)
        if return_result is True:
            return QtWidgets.QMessageBox.about(self, "성공", "회원가입 성공")
        elif return_result is False:
            return QtWidgets.QMessageBox.about(self, "실패", "회원가입 실패")

    def login_access(self):
        login_username = self.line_edit_for_login_id.text()
        login_pw = self.line_edit_for_login_pw.text()
        return_result = self.client_app.send_login_id_and_pw_for_login_access(login_username, login_pw)
        if return_result is True:
            return QtWidgets.QMessageBox.about(self, "성공", "login 성공")
        elif return_result is False:
            return QtWidgets.QMessageBox.about(self, "실패", "login 실패")

    def send_message_to_chat_room(self):
        txt_message = self.text_edit_for_send_chat.toPlainText()
        # todo: send 메시지

    def send_file_to_chat_room(self):
        save_excel_dialog = QtWidgets.QMessageBox.question(self, "파일 업로드", "파일을 업로드합니까?")
        if save_excel_dialog == QtWidgets.QMessageBox.Yes:
            save_path_file_name, _, = QtWidgets.QFileDialog.getSaveFileName(self, '파일 저장', './')
            print(f"{save_path_file_name} send 로직 실행")
        # todo: send 메시지
