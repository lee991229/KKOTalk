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
        self.connect = False
        self.client = socket(AF_INET, SOCK_STREAM)
        self.receive_thread = Thread(target=self.receive_thread)
        self.connect_to_surver()

    def set_config(self, configure):
        print('클라이언트 설정 적용됨')

    def connect_to_surver(self):
        self.client.connect(self.SERVER)


    def start(self):
        print(f'클라이언트 프로그램 가동 시작 : {datetime.datetime.now()}')

    def exit(self):
        print(f'클라이언트 프로그램 종료 시작 : {datetime.datetime.now()}')
