import datetime
import threading
from socket import *
from threading import *


class Server:
    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 1024
    FORMAT = "utf-8"
    connected_clients_id = ['test1', 'test2', 'test3']
    connected_user = [('test1', 'password'), ('test2', 'password1'), ('test3', '123')]
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

    # 일단 대충 만들어 놓은것
    def server_status(self, status):
        # ready = 0, run = 1, close = -1
        if status == 0:
            print('준비중')
        elif status == 1:
            print('가동중')
        elif status == -1:
            print('종료중')

    def run(self):
        print(f'서버 가동 시작 : {datetime.datetime.now()}')
        while True:
            client_sock, addr = self.server.accept()  # 클라이언트에 접속할때 두개의 결값을 돌려준다. ip주소랑, 클라이언트 소켓
            print(f"{addr}가 서버에 연결 되었습니다.")
            # 로그인 기능
            user_id = client_sock.recv(self.BUFFER).decode(self.FORMAT)
            if self.validate_id(user_id):
                client_sock.send('아이디존재'.encode(self.FORMAT))
                user_pw = client_sock.recv(self.BUFFER).decode(self.FORMAT)
                if self.validate_pw(user_id, user_pw):
                    # 로그인 상태의 아이디를 리스트에 추가
                    self.login_user.append(client_sock)
                    client_sock.send('연결됨'.encode(self.FORMAT))
                    print(f'{user_id}가 접속')
                    # 로그인이 성공하면 톡방 정보랑 계정 정보들?을 전종해줘야한다.
                    # 메시지의 동작이 있을떄 작동하는 듯?
                else:
                    # 로그인 실패시임
                    print('로그인 실패')
            else:
                print('로그인 실패')
            client_thread = threading.Thread(target=self.message_handler, args=(user_id, addr, client_sock))
            client_thread.start()
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

    def message_handler(self, user_id, addr, client_sock):
        connect = True
        while connect:
            message = client_sock.recv(self.BUFFER).decode(self.FORMAT)
            message_date = datetime.datetime.now()
            for i in self.login_user:
                i.send(f'{user_id} : {message} > 시간{message_date}'.encode(self.FORMAT))

    def stop(self):
        print(f'서버 종료 시작 : {datetime.datetime.now()}')
