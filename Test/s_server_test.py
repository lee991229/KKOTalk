import sys

from PyQt5.QtWidgets import QApplication

from Code.domain.class_db_connector import DBConnector
from Code.front.class_client_controller import WindowController
from Code.network.class_client_prototype import ClientPrototypeWidget
from Code.network.class_server import Server
from Code.network.class_server_2 import Server2
from Code.network.class_server_controller_widget import ServerControllerWidget
from Code.network.class_server_fix_head import ServerFixHead
from Common.common_module import *





if __name__ == '__main__':
    app = QApplication(sys.argv)
    db_conn = DBConnector(test_option=True)
    db_conn.create_tables()
    # server = Server2(db_conn)
    server = ServerFixHead(db_conn)
    proto_widget = ServerControllerWidget(server, db_conn)
    proto_widget.show()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())