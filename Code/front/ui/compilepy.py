import os
import sys

if __name__ == '__main__':
    uis = ['page_friend_list_ui', 'page_join_ui', 'page_login_ui', 'page_talk_room_list_ui', 'page_talk_room_ui',
           'widget_make_talk_room_ui', 'widget_search_talk_room_member_list', 'widget_talk_room_member_plus',
           'widget_profile_ui', 'profile_page_ui','invite_member_widget_ui']
    for ui in uis:
        os.system(f'python -m PyQt5.uic.pyuic -x {ui}.ui -o ui_class_{ui}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name2}.ui -o {name2}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name3}.ui -o {name3}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name6}.ui -o {name6}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name7}.ui -o {name7}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name4}.ui -o {name4}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name5}.ui -o {name5}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name3}.ui -o {name3}.py')
