from PyQt5 import QtCore, QtGui, QtWidgets
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller


class ServerControllerWidget(QtWidgets.QWidget, Ui_server_controller):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # todo 🔴 🟢 추가
