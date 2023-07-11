from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_join_ui import Ui_join_widget


class JoinWidget(QWidget, Ui_join_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()  # 버튼 시그널 받는 메서드
        self.start_hide_event()  # 창 띄울때 발생하는 하이드 이벤트

    # 회원가입 창 버튼 시그널 메서드
    def set_btn_trigger(self):
        self.btn_join_close.clicked.connect(self.close_event)
        self.btn_join_cancel.clicked.connect(self.close_event)
        self.btn_join_register.clicked.connect(self.register_event)
        self.btn_join_duplicatecheck.clicked.connect(self.duplicatecheck_id)
    # 아이디 중복체크 메서드
    def duplicatecheck_id(self):
        make_id = self.lineEdit_join_id.text()
        if self.client_controller.id_duplicate_check(make_id) is True:
            self.label_id_message.setText('중복아이디가 없어용')
        self.label_id_message.show() # 아이디 중복여부 메세지 보여주기

    # 회원가입 승인 메서드
    def register_event(self):
        self.client_controller.join_pw = self.lineEdit_join_pw.text()

        pass
    # 시작시 라벨들 숨기기 메서드
    def start_hide_event(self):
        self.label_join_Warning.hide()
        self.label_id_message.hide()

    # 회원가입창 닫기 메서드
    def close_event(self):
        """
        로그인 화면을 닫는 메서드
        """
        self.close()
