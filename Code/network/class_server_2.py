import os
from socket import *
from threading import Thread, Event

import select


class Server2:
    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 1024
    FORMAT = "utf-8"
    HEADER_LENGTH = 10

    def __init__(self):
        # 서버 소켓 설정
        self.server_socket = socket(AF_INET, SOCK_STREAM)  # AF_INET(ipv4를 의미)
        self.server_socket.bind((self.HOST, self.PORT))
        self.config = None
        self.sockets_list = list()
        self.sockets_list.append(self.server_socket)
        self.clients = dict()
        self.thread_for_run = None
        self.run_signal = True
        self.server_socket.listen()

    def set_config(self, configure):
        self.config = configure
        print('서버 설정 적용됨')

    def start(self):
        if self.thread_for_run is not None:  # 실행중이면 종료 시키기
            self.thread_for_run: Thread
            self.stop()
        self.run_signal = True
        self.thread_for_run = Thread(target=self.run, args=(self.run_signal,))
        self.thread_for_run.start()

    def stop(self):
        self.run_signal = False

    def run(self, signal):
        while True:
            if signal is False:
                break

            read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list)

            for notified_socket in read_sockets:
                if notified_socket == self.server_socket:
                    client_socket, client_address = self.server_socket.accept()
                    user = self.receive_message(client_socket)

                    if user is False:
                        continue
                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user

                else:
                    message = self.receive_message(notified_socket)

                    if message is False:
                        print(f"Closed connection from: {self.clients[notified_socket]['data'].decode('utf-8')}")
                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]
                        continue
                    user = self.clients[notified_socket]
                    print(f"Received message,, {user['data'].decode('utf-8')}> {message['data'].decode('utf-8')}")

                    for client_socket in self.clients:
                        if client_socket != notified_socket:
                            client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]

    def receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(self.HEADER_LENGTH)
            if not len(message_header):
                return False
            message_length = int(message_header.decode('utf-8').strip())

            return {'header': message_header, 'data': client_socket.recv(message_length)}

        except:
            return False
