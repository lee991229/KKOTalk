import datetime
from socket import *
from threading import *


class Server:
    HOST = '10.10.20.115'
    PORT = 9999
    BUFFER = 1024
    FORMAT = "utf-8"
    connected_clients_id = ['test1', 'test2', 'test3']
    connected_user = [('test1', 'password'), ('test2', 'password1'), ('test3', '123')]

    def __init__(self):
        # 서버 소켓 설정
        self.server = socket(AF_INET, SOCK_STREAM)  # AF_INET(ipv4를 의미)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen()

    def set_config(self, configure):
        print('서버 설정 적용됨')

    def user_add(self, user_id):
        pass

    def run(self):
        print(f'서버 가동 시작 : {datetime.datetime.now()}')
        while True:
            client_sock, addr = self.server.accept()  # 클라이언트에 접속할때 두개의 결값을 돌려준다. ip주소랑, 클라이언트 소켓
            print(f"{addr}가 서버에 연결 되었습니다.")
            user_id = client_sock.recv(self.BUFFER).decode(self.FORMAT)
            if self.validate_id(user_id):
                client_sock.send('아이디존재'.encode(self.FORMAT))
                user_pw = client_sock.recv(self.BUFFER).decode(self.FORMAT)
                if self.validate_pw(user_id, user_pw):
                    client_sock.send('연결됨'.encode(self.FORMAT))
                    print(f'{user_id}가 접속')
            # if self.validate_username(user_id):
            #     client_sock.send('연결됨'.encode(self.FORMAT))

    # 아이디 확인
    def validate_id(self, user_id):
        if user_id in self.connected_clients_id:
            return True
        else:
            return False

    # 비밀번호 아이디 일치하는지 확인
    def validate_pw(self, user_id, user_pw):
        user_info = (user_id, user_pw)
        if user_info in self.connected_user:
            return True
        else:
            return False

    def validate_username(self, username):
        if username in self.connected_clients:
            return True
        else:
            return False


    def stop(self):
        print(f'서버 종료 시작 : {datetime.datetime.now()}')
