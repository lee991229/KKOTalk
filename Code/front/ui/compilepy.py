import os
import sys

if __name__ == '__main__':
    os.system(f"pyrcc5 ../src_img/my_qrc.qrc -o my_qrc_rc.py")

    uis = ['page_friend_list_ui', 'page_join_ui', 'page_login_ui', 'page_talk_room_list_ui', 'page_talk_room_ui',
           'widget_talk_room_invite_user_list', 'widget_search_talk_room_member_list',
           'widget_profile_item_ui', 'widget_chat_room_item_ui', 'profile_page_ui',
           'widget_invite_user_item','widget_talk_room_invite_user_list_in_chat_room',
           "widget_custom_message_box", 'message_label']
    for ui in uis:
        # os.system(f'python  -m PyQt5.uic.pyuic --from-imports -x {ui}.ui -o ui_class_{ui}.py')
        os.system(f'python  -m PyQt5.uic.pyuic --import-from=Code.front.ui -x {ui}.ui -o ui_class_{ui}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name2}.ui -o {name2}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name3}.ui -o {name3}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name6}.ui -o {name6}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name7}.ui -o {name7}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name4}.ui -o {name4}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name5}.ui -o {name5}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name3}.ui -o {name3}.py')
