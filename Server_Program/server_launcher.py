

from Code.network.class_server import Server
import server_config
from Code.network.class_server_controller_widget import ServerControllerWidget
from PyQt5.QtWidgets import QApplication
from Common.common_module import *
import sys


if __name__ == '__main__':
    kkotalk_server = Server() # 서버 인스턴스화
    configure = server_config.ServerConfigure() # 서버 설정 인스턴스화
    kkotalk_server.set_config(configure) # 서버 설정 적용
    kkotalk_server.run()

    # qt 기본 설정
    app = QApplication(sys.argv)
    server_launcher = ServerControllerWidget(kkotalk_server)
    server_launcher.show()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())
