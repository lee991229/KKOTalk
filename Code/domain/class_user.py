from Common.common_module import *


class User:
    def __init__(self, user_id, username, password, nickname):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.nickname = nickname

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __repr__(self):
        return f'{self.__dict__}'

    def __eq__(self, other):
        if isinstance(other, User) and \
                self.user_id == other.user_id and \
                self.username == other.username and \
                self.password == other.password and \
                self.nickname == other.nickname:
            return True
        return False


