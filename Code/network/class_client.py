import datetime
import threading
from socket import *
from threading import *


class ClientApp:
    HOST = '10.10.20.115'
    PORT = 9999
    BUFFER = 1024
    FORMAT = "utf-8"
    SERVER = (HOST, PORT)

    def __init__(self):
        # self.controller =  ClientController()
        self.connected = False
        self.client = socket(AF_INET, SOCK_STREAM)
        self.receive_thread = Thread(target=self.receive_message)
        self.connect_to_surver()
        # 임의로 지정
        self.user_id = 'test1'
        self.validate_user(self.user_id)

    def set_config(self, configure):
        print('클라이언트 설정 적용됨')

    def connect_to_surver(self):
        self.client.connect(self.SERVER)

    def validate_user(self, user_id):
        self.client.send(user_id.encode(self.FORMAT))
        if self.client.recv(self.BUFFER).decode(self.FORMAT) == "Valid":
            self.connected = True
            print("로그인 됨")
            # 로그인되면 크크오톡 화면 뜨는건가? UI뜨게 변경되는 느낌인가?
            self.receive_thread.start()

    def send_message(self):
        message = self.textEdit.toPlainText().strip()  # 이건 뭔지 아직 이해 못했음

    def start(self):
        print(f'클라이언트 프로그램 가동 시작 : {datetime.datetime.now()}')

    def exit(self):
        print(f'클라이언트 프로그램 종료 시작 : {datetime.datetime.now()}')
