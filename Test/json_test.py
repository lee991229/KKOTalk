from unittest import TestCase

from Common.common_module import *
from Code.domain.class_user import User


class UnitTest(TestCase):

    def setUp(self):
        self.encoder = KKOEncoder()
        self.decoder = KKODecoder()

    def test_user_encode_and_decode(self):
        user_1 = User(None, 'hi', '123', 'marrow')
        user_json_str = user_1.toJSON()
        result = KKODecoder().decode(user_json_str)

        self.assertTrue(user_1 == result, True)

    def test_message_encode_and_decode(self):
        pass