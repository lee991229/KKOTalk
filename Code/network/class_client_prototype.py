from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

from Code.network.class_worker_thread import WorkerServerThread
from Code.network.server_ui.ui_chat_room import Ui_prototype
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller


class ClientPrototypeWidget(QtWidgets.QWidget, Ui_prototype):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.qthread = WorkerServerThread(self)
        self.check_timer = None
        self.set_btn_trigger()
        self.set_timer_to_check_server_status()

    def initialize_app(self):
