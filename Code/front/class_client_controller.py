from Code.domain.class_db_connector import DBConnector
from Code.front.widget_friend_list_page import FriendListWidget
from Code.front.widget_join_page import JoinWidget
from Code.front.widget_login_page import LoginWidget


class WindowController:
    def __init__(self, db_connector=None):
        super().__init__()
        self.db_connector = db_connector    #db연결 인스턴스
        # Domain 인스턴스
        # self.login_user =   # 스케줄러 페이지
        self.login_page = LoginWidget(self)
        self.friend_list_page = FriendListWidget()
        self.join_widge = JoinWidget()
    def show_join_page(self):
        self.join_widge.show()
    def run(self):
        self.login_page.show()

    def assert_login_data(self, login_id, login_pw):
        db_id = '1234'
        db_pw = '1234'
        if  db_id == login_id and db_pw == login_pw :
            return True

    def show_login_success(self):
        self.friend_list_page.show()