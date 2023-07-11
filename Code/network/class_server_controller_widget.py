from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

from Code.network.class_worker_thread import WorkerServerThread
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller


class ServerControllerWidget(QtWidgets.QWidget, Ui_server_controller):
    def __init__(self, server_obj, db_connector):
        super().__init__()
        self.setupUi(self)
        self.server = server_obj
        self.db_conn = db_connector
        self.qthread = WorkerServerThread(self)
        self.check_timer = None
        self.set_initial_label()
        self.set_btn_trigger()
        self.set_timer_to_check_server_status()

    def set_timer_to_check_server_status(self):
        self.check_timer = QtCore.QTimer(self)
        self.check_timer.setInterval(1000)
        self.check_timer.timeout.connect(lambda: self.assert_server_status())
        self.check_timer.start()

    def assert_server_status(self):
        # if self.server.status == ""
        # self.label_server_status.setText("🟢 가동중")
        # self.label_server_status.setText("🟠 시작중")
        # self.label_server_status.setText("🔴 종료됨")
        pass

    def set_initial_label(self):
        # todo check serve status logic
        self.label_server_status.setText("🔴 종료됨")

    def set_btn_trigger(self):
        self.btn_run.clicked.connect(lambda state: self.server_run())
        self.btn_stop.clicked.connect(lambda state: self.server_stop())

    def server_run(self):
        self.qthread.set_work(self.server.run)
        self.qthread.start()  # 쓰레드 동작시킴


    def server_stop(self):
        self.server.stop()
