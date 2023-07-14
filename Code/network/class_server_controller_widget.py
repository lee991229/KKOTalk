import datetime
import os
import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

from Code.domain.class_user import User
from Code.network.class_worker_thread import WorkerServerThread
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller


class ServerControllerWidget(QtWidgets.QWidget, Ui_server_controller):
    ENCODED_DOT = bytes('.', 'utf-8')
    ENCODED_PASS = bytes('pass', 'utf-8')
    LOG_PATH = """C:\\Users\\KDT107\\Desktop\\KKOTalk\\log.txt"""
    SERVER_STATUS_PATH = """C:\\Users\\KDT107\\Desktop\\KKOTalk\\server_status.txt"""

    @staticmethod
    def save_server_log():
        os.system("""C:\\Users\\KDT107\\Desktop\\KKOTalk\\Code\\network\\server_logger.bat""")

    @staticmethod
    def check_netstat_via_cmd():
        os.system("""C:\\Users\\KDT107\\Desktop\\KKOTalk\\Code\\network\\check_server_on.bat""")

    def __init__(self, server_obj, db_connector):
        super().__init__()
        self.setupUi(self)
        self.server = server_obj
        self.db_conn = db_connector
        self.server_status_check_timer = None
        self.server_running_timer = None
        self.server_running_second = 0
        self.server_start_time = None
        self.set_initial_label()
        self.set_btn_trigger()
        self.check_netstat_via_cmd()
        self.set_timer_to_check_server_status()
        self.set_timer_to_server_running_timer()
        self.get_last_time_server_and_set_label()

    def set_timer_to_check_server_status(self):
        if self.server_status_check_timer is None:
            self.server_status_check_timer = QtCore.QTimer(self)
            self.server_status_check_timer.setInterval(1000)
            self.server_status_check_timer.timeout.connect(lambda: self.assert_server_status())
            self.server_status_check_timer.start()
        else:
            self.server_status_check_timer.stop()
            self.server_status_check_timer.start()

    def set_timer_to_server_running_timer(self):
        if self.server_running_timer is None:
            self.server_running_timer = QtCore.QTimer(self)
            self.server_running_timer.setInterval(1000)
            self.server_running_timer.timeout.connect(lambda: self.count_running_time())

    def count_running_time(self):
        self.server_start_time: datetime.datetime
        run_time = datetime.datetime.now() - self.server_start_time
        s = run_time.seconds
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.label_run_time.setText(f"{hours:02}:{minutes:02}:{seconds:02}")

    def get_last_time_server_and_set_label(self):
        last_line = None
        try:
            with open(self.LOG_PATH, 'r', encoding="utf-8") as file:
                whole_log = file.read().split('\n')
                line_count = len(whole_log)
                for i in range(line_count - 1, -1, -1):
                    print(i, whole_log[i])
                    if len(whole_log[i]) > 3:
                        last_line = whole_log[i]
                        break
            if last_line is not None:
                temp_list = last_line.split(' ')
                last_date_time = ' '.join(temp_list[:2])
                self.label_last_stop.setText(last_date_time)
            else:
                self.label_last_stop.setText("-")
        except:
            self.label_last_stop.setText("-")

    def is_server_listening(self):
        try:
            with open(self.SERVER_STATUS_PATH, "w", encoding="utf-8") as file:
                file.write('')
            self.check_netstat_via_cmd()
            with open(self.SERVER_STATUS_PATH, "r", encoding="utf-8") as file:
                if "LISTENING" in file.read().split("\n")[0]:
                    return True
        except:
            return False

    def is_server_running(self):
        result = self.is_server_listening()
        if result:  # 서버가 켜저있는 경우
            return True
        else:
            return False

    def assert_server_status(self):
        self.check_netstat_via_cmd()
        if self.is_server_running() is True:
            self.label_server_status.setText("🟢 가동중")
        else:
            self.label_server_status.setText("🔴 종료됨")
        # self.label_server_status.setText("🟠 시작중")

    def set_initial_label(self):
        # todo check serve status logic
        self.label_server_status.setText("🔴 종료됨")
        self.label_start_time.setText("-")
        self.label_run_time.setText("00:00:00")

    def set_btn_trigger(self):
        self.btn_run.clicked.connect(lambda state: self.server_run())
        self.btn_stop.clicked.connect(lambda state: self.server_stop())

    def server_run(self):
        if self.is_server_running() is False:
            self.server.start()
            self.server_start_time = datetime.datetime.now()
            self.server_running_second = 0
            self.server_running_timer.start()
            now_time_str = self.server_start_time.strftime("%Y-%m-%d %H:%M:%S")
            self.label_start_time.setText(now_time_str)
            log_msg = f"{now_time_str} server start"
            with open(self.LOG_PATH, 'a', encoding="utf-8") as file:
                file.write(log_msg)
            print(log_msg)

    def server_stop(self):
        self.server.stop()
        if self.server_running_timer is not None:
            self.server_running_timer.stop()
        self.label_server_status.setText("🔴 종료됨")
        log_msg = f"{datetime.datetime.now()} server stop"
        with open(self.LOG_PATH, 'a', encoding="utf-8") as file:
            file.write(log_msg + '\n')
        print(log_msg)
        self.get_last_time_server_and_set_label()
        self.label_start_time.setText("-")
        # temp_time = QtCore.QTimer(self)s self.task_server_kill())

    def task_server_kill(self):
        last_line = None
        self.check_netstat_via_cmd()
        with open(self.SERVER_STATUS_PATH, "r", encoding="utf-8") as file:
            last_line = file.readline().split("\n")[0].split(' ')[-2].strip()
            os.system(f"taskkill /pid {last_line}")

    def assert_same_join_id(self, input_username):
        return self.db_conn.assert_same_login_id(input_username)

    def join_access(self, join_user_json_str: str):
        join_user_obj = self.decoder.decode(join_user_json_str)
        join_user_obj: User
        if self.db_conn.insert_user(join_user_obj) is not False:
            print(f"유저 {join_user_obj.nickname} 가입 성공")
            return True
        else:
            return False

    def login_access(self, login_message: str):
        username, pw = login_message.split('%')
        if self.db_conn.user_log_in(username, pw):
            print(f"유저 {username} 로그인 성공")
            return True
        else:
            return False
