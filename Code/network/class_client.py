import datetime


class ClientApp:
    def __init__(self):
        # self.controller =  ClientController()
        pass


    def set_config(self, configure):
        print('클라이언트 설정 적용됨')

    def start(self):
        print(f'클라이언트 프로그램 가동 시작 : {datetime.datetime.now()}')

    def exit(self):
        print(f'클라이언트 프로그램 종료 시작 : {datetime.datetime.now()}')
