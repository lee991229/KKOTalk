import time

from Code.network.class_server import Server
import server_config
# import Common.common_module # common module 함수, 변수 필요 시


if __name__ == '__main__':
    kkotalk_server = Server()
    configure = server_config.ServerConfigure()
    kkotalk_server.set_config(configure)
    kkotalk_server.run()

    time.sleep(10)
    kkotalk_server.stop()