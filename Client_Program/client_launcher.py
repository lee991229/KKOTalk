import time

from Code.network.class_client import ClientApp

if __name__ == '__main__':
    kkotalk_client = ClientApp()
    configure = kkotalk_client.ServerConfigure()
    kkotalk_client.set_config(configure)
    kkotalk_client.start()

    time.sleep(10)
    kkotalk_client.exit()
