import datetime
from socket import *
from threading import *


class Server:
    # HOST = '10.10.20.115'
    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 1024
    FORMAT = "utf-8"
    connected_clients = ['test1%password', 'test2', 'test3']
    login_user = []

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
            clients_login = client_sock.recv(self.BUFFER).decode(self.FORMAT)
            if self.validate_login(clients_login):
                client_sock.send('pass'.encode(self.FORMAT))
                self.login_user.append(client_sock)
                client_thread = Thread(target=self.message_handler, args=(clients_login[0:5], addr, client_sock))
                client_thread.start()
            else:
                client_sock.send('.'.encode(self.FORMAT))
                # client_sock.close()

            # if self.validate_username(user_id):
            #     client_sock.send('연결됨'.encode(self.FORMAT))

    # 아이디 확인
    def validate_login(self, clients_login):
        if clients_login in self.connected_clients:
            return True
        else:
            return False

    def message_handler(self, user_id, addr, client_sock):
        while True:
            message = client_sock.recv(self.BUFFER).decode(self.FORMAT)
            print(self.login_user)
            message_date = datetime.datetime.now()
            for i in self.login_user:
                i.send(f'{user_id} : {message} > 시간{message_date}'.encode(self.FORMAT))

    def validate_username(self, username):
        if username in self.connected_clients:
            return True
        else:
            return False

    def stop(self):
        print(f'서버 종료 시작 : {datetime.datetime.now()}')
