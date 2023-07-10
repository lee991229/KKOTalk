from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_login_ui import Ui_login_widget


class LoginWidget(QWidget, Ui_login_widget):

    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()
    def set_btn_trigger(self):
        self.btn_login.clicked.connect(self.assert_login)
        self.btn_join.clicked.connect()
    def assert_join(self):
        self.client_controller.show_join_page()
    def assert_login(self):
        login_id = self.line_edit_id.text()
        login_pw = self.line_edit_pw.text()
        if self.client_controller.assert_login_data(login_id, login_pw) is True:
            self.client_controller.show_login_success()


