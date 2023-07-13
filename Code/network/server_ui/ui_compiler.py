
import os

if __name__ == '__main__':
    os.system('pyuic5 controller.ui -o ui_server_controller_widget.py')
    os.system('pyuic5 prototype_chat_room.ui -o ui_chat_room.py')
