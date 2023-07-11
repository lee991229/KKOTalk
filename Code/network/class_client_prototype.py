from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

from Code.domain.class_db_connector import DBConnector
from Code.domain.class_user import User
from Code.network.class_worker_thread import WorkerServerThread
from Code.network.server_ui.ui_chat_room import Ui_prototype
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller


class ClientPrototypeWidget(QtWidgets.QWidget, Ui_prototype):
    def __init__(self, client, db_conn: DBConnector):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.server = client
        self.db_conn = db_conn
        self.valid_duplication_id = False
        self.qthread = WorkerServerThread(self)
        self.set_btn_trigger()
        self.set_init_label()

    def set_init_label(self):
        self.initialize_app()
        self.setWindowTitle("성혁이를 위한 프로토타입 위젯")

    def set_btn_trigger(self):
        self.btn_init.clicked.connect(lambda state: self.initialize_app())
        self.btn_check_same_id.clicked.connect(lambda state: self.send_join_id_for_assert_same_username())
        self.btn_join.clicked.connect(lambda state: self.join_access())
        self.btn_login.clicked.connect(lambda state: self.login_access())
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

    # server function =================================

    def listening(self):
        while True:
            msg = self.server.recv(1024).decode("utf-8")
            if msg == '/assert_username':
                self.server.send(bytes(".", "utf-8"))
                response = self.server.recv(1024).decode("utf-8")
                if self.assert_same_join_id(response) is True:
                    self.server.send('pass'.encode())
            elif msg == '/login_':
                pass

    def assert_same_join_id(self, input_username):
        return self.db_conn.assert_same_login_id(input_username)

    def join_access(self):
        pass

    # client function =================================
    def send_join_id_for_assert_same_username(self):
        input_username = self.line_edit_for_join_id.text()
        self.client.send("/assert_username")  # 헤더를 붙이고 보내는 동작(?)
        self.client.send(input_username.encode())  # 실제 내용을 붙여서 보내는 동작
        return_result = self.client.recv(1024)  # 응답 받기
        if return_result:
            self.valid_duplication_id = True
            return QtWidgets.QMessageBox.about(self, "가능", "중복 없는 아이디, 써도됌")
        else:
            return QtWidgets.QMessageBox.about(self, "불가능", "중복 아이디, 새로 쓰기")

    def send_join_id_and_pw_for_join_access(self):
        if self.valid_duplication_id is False:
            QtWidgets.QMessageBox.about(self, "어허", "아이디 중복확인 먼저 시행해주세요")
            return
        join_username = self.line_edit_for_join_id.text()
        join_pw = self.line_edit_for_join_pw.text()
        join_nickname = self.line_edit_for_join_nick.text()
        join_user = User(None, join_username, join_pw, join_nickname)
        try:
            self.db_conn.insert_user(join_user)
            print(f"user {join_nickname} 가입 성공")
        except Exception:
            print("user join 실패")

    def login_access(self):
        username = self.line_edit_for_login_id
        password = self.line_edit_for_login_pw

        user_obj = self.db_conn.user_log_in(username, password)
        if user_obj is not False:
            print('login 성공!')
        else:
            print('login 실패!')

    def send_message_to_chat_room(self):
        txt_message = self.text_edit_for_send_chat.toPlainText()
        print(txt_message)

    def send_file_to_chat_room(self):
        save_excel_dialog = QtWidgets.QMessageBox.question(self, "파일 업로드", "파일을 업로드합니까?")
        if save_excel_dialog == QtWidgets.QMessageBox.Yes:
            save_path_file_name, _, = QtWidgets.QFileDialog.getSaveFileName(self, '파일 저장', './')
            print(f"{save_path_file_name} send 로직 발동")
