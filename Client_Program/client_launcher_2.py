from Client_Program.client_config import ClientConfigure
from Code.network.class_client_2 import ClientApp

if __name__ == '__main__':
    kkotalk_client = ClientApp()
    configure = ClientConfigure()
    kkotalk_client.set_config(configure)
    kkotalk_client.start()

    # time.sleep(10)
    # kkotalk_client.exit()
