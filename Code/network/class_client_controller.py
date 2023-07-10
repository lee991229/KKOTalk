from Code.domain.class_db_connector import DBConnector


class WindowController():
    def __init__(self, db_connector):
        super().__init__()
        self.db_connector = db_connector    #db연결 인스턴스
        # Domain 인스턴스
        # self.login_user =   # 스케줄러 페이지
        #



    def assert_login(self, id, pa):
        if self.db_connector.login(li):
            return True
        else:
            return False
