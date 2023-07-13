import sys

from PyQt5.QtWidgets import QApplication

from Code.network.class_client import ClientApp
from Code.network.class_client_prototype import ClientPrototypeWidget
from Common.common_module import *





if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = ClientApp()
    proto_widget = ClientPrototypeWidget(client) # 전략 패턴
    proto_widget.show()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())