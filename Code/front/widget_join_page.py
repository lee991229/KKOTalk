from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_join_ui import Ui_join_widget
from PyQt5.QtCore import Qt


class JoinWidget(QWidget, Ui_join_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.client_controller = client_controller
        self.set_btn_trigger()  # 버튼 시그널 받는 메서드

    # 회원 가입 창 버튼 시그널 메서드
    def set_btn_trigger(self):
        self.btn_join_cancel.clicked.connect(self.close_event)
        self.btn_join_register.clicked.connect(self.register_event)
        self.btn_join_duplicatecheck.clicked.connect(self.duplicate_check_id)

    def ninkname_examine(self):
        choice_ninkname = self.lineedit_join_user_name.text()
        if choice_ninkname != "":
            return True
        else:
            return False
        #   todo: '닉네임 생성 조건 만들어'

    # 아이디 중복 체크 메서드
    def duplicate_check_id(self):
        self.client_controller.join_id = self.lineEdit_join_id_1.text()
        # self.client_controller.id_duplicate_check()
        if self.client_controller.id_duplicate_check() is True:  # 아이디 중복이 없으면
        #     self.client_controller.join_id = self.lineEdit_join_id_1.text()
            self.show_label_id_message('사용 가능한 아이디 입니다')  # 아이디 중복여부 메세지 보여주기
            self.hide_label_condition()  # 하단 경고 라벨이 아이디 중복체크면 하이드
        else:
            self.show_label_id_message('아이디가 중복 됩니다')

    def duplicate_check_pw(self):
        reconfirm_pw = self.lineedit_join_reconfirm_pw.text()
        pw = self.lineedit_join_pw.text()
        # todo:'비밀번호 특문 조건 넣나?'
        if pw == reconfirm_pw and pw != "":  # 비밀 번호와 비밀 번호 확인이 일치하면
            return True
        else:
            return False

    def hide_label_condition(self):
        if self.label_join_Warning == '아이디 중복체크를 해주세요':
            self.hide_label_join_warning()

    def hide_label_join_warning(self):
        self.label_join_Warning.hide()

    def hide_label_id_message(self):
        self.label_id_message.hide()

    def show_label_join_warning(self, text):
        self.label_join_Warning.setText(text)
        self.label_join_Warning.show()

    def show_label_id_message(self, text):
        self.label_id_message.setText(text)
        self.label_id_message.show()

    # 회원 가입 승인 메서드
    def register_event(self):
        if self.client_controller.join_id is None:
            self.show_label_join_warning('아이디 중복체크를 해주세요')
        elif self.duplicate_check_pw() is False:  # 비밀번호 비밀번호 확인 비교
            self.show_label_join_warning('비밀번호를 확인 하세요')
        elif self.ninkname_examine() is False:  # 사용 가능 닉네임 검사
            self.show_label_join_warning('이름을 확인하세요')
        else:
            self.client_controller.join_pw = self.lineedit_join_pw.text()
            self.client_controller.join_nickname = self.lineedit_join_user_name.text()
            self.client_controller.join_success()
            # todo: '유저 가입 만들기 '
            self.close()

    def line_edit_clear(self):
        line_edits = self.frame_4.findChildren(QLineEdit)
        for line_edit in line_edits:
            line_edit.clear()

    def show(self):
        self.line_edit_clear()
        self.hide_label_join_warning()  # 경고 라벨 하이드
        self.hide_label_id_message()  # 아이디 중복 체크 라벨 하이드
        # self.btn_join_register.setDisabled(True)
        super().show()

    # 회원 가입창 닫기 메서드
    def close_event(self):
        """
        로그인 화면을 닫는 메서드
        """
        self.close()
