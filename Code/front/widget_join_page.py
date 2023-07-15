from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_join_ui import Ui_join_widget
from PyQt5.QtCore import Qt


class JoinWidget(QWidget, Ui_join_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.client_controller = client_controller
        self.set_btn_trigger()  # 버튼 시그널 받는 메서드
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)


    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self,event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self,event)

    # 회원 가입 창 버튼 시그널 메서드
    def set_btn_trigger(self):
        self.btn_join_cancel.clicked.connect(lambda state: self.close())
        self.btn_first_close.clicked.connect(lambda state: self.close())
        self.btn_join_register.clicked.connect(self.register_event)
        self.btn_join_duplicatecheck.clicked.connect(self.duplicate_check_username)

    def assert_not_blank_nickname(self):
        choice_nickname = self.lineedit_join_user_nickname.text()
        if choice_nickname != "":
            return True
        else:
            return False
        #   todo: '닉네임 생성 조건 만들어'

    # 아이디 중복 체크 메서드
    def duplicate_check_username(self):
        join_username = self.lineEdit_join_username.text()
        self.client_controller.assert_same_username(join_username)
    def assert_same_password(self):
        reconfirm_pw = self.lineedit_join_pw_2.text()
        pw = self.lineedit_join_pw.text()
        if pw == reconfirm_pw and pw != "":  # 비밀 번호와 비밀 번호 확인이 일치하면
            return True
        else:
            return False

    def hide_label_condition(self):
        if self.label_join_warning == '아이디 중복체크를 해주세요':
            self.hide_label_join_warning()

    def hide_label_join_warning(self):
        self.label_join_warning.hide()

    def hide_label_id_message(self):
        self.label_id_message.hide()

    def show_label_join_warning(self, text):
        self.label_join_warning.setText(text)
        self.label_join_warning.show()

    def show_label_id_message(self, text):
        self.label_id_message.setText(text)
        self.label_id_message.show()

    # 회원 가입 승인 메서드
    def register_event(self):
        if self.client_controller.valid_duplication_id is False:
            self.show_label_join_warning('아이디 중복체크를 해주세요')
            return
        elif self.assert_same_password() is False:  # 비밀번호 비밀번호 확인 비교
            self.show_label_join_warning('비밀번호를 확인 하세요')
            return
        elif self.assert_not_blank_nickname() is False:  # 사용 가능 닉네임 검사
            self.show_label_join_warning('이름을 확인하세요')
            return
        else:
            self.client_controller.join_access()
            # todo: '유저 가입 만들기 '
            self.close()

    def line_edit_clear(self):
        self.lineEdit_join_username.clear()
        self.lineedit_join_pw.clear()
        self.lineedit_join_pw_2.clear()
        self.lineedit_join_user_nickname.clear()

    def show(self):
        self.line_edit_clear()
        self.hide_label_join_warning()  # 경고 라벨 하이드
        self.hide_label_id_message()  # 아이디 중복 체크 라벨 하이드
        # self.btn_join_register.setDisabled(True)
        super().show()

    def set_window_drag(self):
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)
            event.accept()



