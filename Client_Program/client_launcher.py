import time

from Client_Program.client_config import ClientConfigure
from Code.network.class_client import ClientApp
from Code.network.class_client_prototype_2 import ClientPrototypeWidget2
from PyQt5.QtWidgets import QApplication
from Common.common_module import *
import sys


if __name__ == '__main__':
    kkotalk_client = ClientApp()
    configure = ClientConfigure()
    kkotalk_client.set_config(configure)
    # kkotalk_client.start()
    # qt 기본 설정
    app = QApplication(sys.argv)
    client_launcher = ClientPrototypeWidget2(kkotalk_client)
    client_launcher.show()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())

    # time.sleep(10)
    # kkotalk_client.exit()
