from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_login_ui import Ui_login_widget


class LoginWidget(QWidget, Ui_login_widget):

    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()
        self.start_hide_event()

    def set_btn_trigger(self):
        self.btn_login.clicked.connect(self.assert_login)  # 로그인 승인버튼 클릭시 assert_login메서드 발동
        self.btn_join.clicked.connect(self.assert_join)
        self.btn_close.clicked.connect(self.close_event)


    def start_hide_event(self):
        self.label_warning.hide()

    def close_event(self):
        """
        로그인 화면을 닫는 메서드
        """
        self.close()

    def assert_join(self):
        self.client_controller.show_join_page()  # 클라이언트 컨트롤에 있는 회원가입창을 띄우는 메서드

    def assert_login(self):
        login_id = self.line_edit_id.text()
        login_pw = self.line_edit_pw.text()
        if self.client_controller.assert_login_data(login_id, login_pw) is True:
            self.client_controller.show_login_success() # id,pw가 일치해서 친구창 화면을 띄워준다

    def no_input_id(self):
        self.label_warning.setText("아이디를 적어주세요")

    def none_id(self):
        self.label_warning.setText("아이디가 없거나 일치하지 않습니다")