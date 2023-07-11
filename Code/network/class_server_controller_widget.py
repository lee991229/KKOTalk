from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller


class ServerControllerWidget(QtWidgets.QWidget, Ui_server_controller):
    def __init__(self, server_obj):
        super().__init__()
        self.setupUi(self)
        self.server = server_obj
        self.set_initial_label()
        self.set_btn_trigger()

    def set_initial_label(self):
        # todo check serve status logic
        self.label_server_status.setText("🔴 종료됨")

    def set_btn_trigger(self):
        self.btn_run.clicked.connect(lambda state: self.server_run())
        self.btn_stop.clicked.connect(lambda state: self.server_stop())

    def server_run(self):
        self.label_server_status.setText("🟠 시작중")
        Thread()
        # self.server.run()
        self.label_server_status.setText("🟢 가동중")

    def server_stop(self):
        self.server.stop()
        self.label_server_status.setText("🔴 종료됨")

    # todo 🔴 🟠 🟢 추가
