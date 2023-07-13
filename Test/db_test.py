from unittest import TestCase

from Code.domain.class_db_connector import DBConnector
from Code.domain.class_user import User


class UnitTest(TestCase):
    def setUp(self):  # 각 테스트마다 실행되는 함수임, Create tables 하기땜에 싹 밀고 새로 생긴다고 보면됌
        # 운영상 DB를 건들이지 않기위해 테스트용 db를 이용함
        self.conn = DBConnector(test_option=True)
        self.conn.create_tables()

    def test_유저_객체_만들어서_DB_insert_하면_ID가_1부터_시작_AUTO_INCREMENT_USER_OBJ_반환(self):
        user_a = User(None, 'abc1234', '1234', '뿡뿡이')
        user_b = User(None, 'def5678', '5678', '짱구')
        user_a = self.conn.insert_user(user_a)
        user_b = self.conn.insert_user(user_b)

        self.assertEqual(1, user_a.user_id)
        self.assertEqual(2, user_b.user_id)

    def test_유저_객체_만들면_find_all_했을때_다_불러와져야함(self):
        user_a = User(None, 'abc1234', '1234', '뿡뿡이')
        user_b = User(None, 'def5678', '5678', '짱구')
        user_c = User(None, 'charming_park', '1234', '맹구')
        user_a = self.conn.insert_user(user_a)
        user_b = self.conn.insert_user(user_b)
        user_c = self.conn.insert_user(user_c)

        insert_user_list = [user_a, user_b, user_c]

        found_user_list = self.conn.find_all_user()
        self.assertEqual(3, len(found_user_list))  # 3개 넣었으니까 3이 되야함

        # db에 넣은거랑 직접 넣은거랑 갖고 있는 인스턴스 변수값이 같은지 확인

        for (db_instance, insert_instance) in zip(found_user_list, insert_user_list):
            self.assertIsInstance(db_instance, User)
            self.assertEqual(db_instance.user_id, insert_instance.user_id)
            self.assertEqual(db_instance.username, insert_instance.username)
            self.assertEqual(db_instance.password, insert_instance.password)
            self.assertEqual(db_instance.nickname, insert_instance.nickname)

    def test_1(self):
        # given
        # when
        # then
        pass

    def test_2(self):
        # given
        # when
        # then
        pass
