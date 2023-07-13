import json
import random


class User:
    def __init__(self, user_id, username, password, nickname):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.nickname = nickname


    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __eq__(self, other):
        if isinstance(other, User) and \
                self.user_id == other.user_id and \
                self.username == other.username and \
                self.password == other.password and \
                self.nickname == other.nickname:
            return True
        return False

    def __lt__(self, other):
        return self.nickname < other.nickname

# if __name__ == '__main__':
#     user1 = User(1, 'abc', 'muyaho', '갑')
#     user2 = User(2, 'abc', 'muyaho', '을')
#     user3 = User(3, 'abc', 'muyaho', '병')
#     user4 = User(4, 'abc', 'muyaho', 'aa')
#     user5 = User(5, 'abc', 'muyaho', 'ab')
#     user6 = User(6, 'abc', 'muyaho', 'ac')
#     user7 = User(7, 'abc', 'muyaho', '111')
#     user8 = User(8, 'abc', 'muyaho', '121')
#     user9 = User(9, 'abc', 'muyaho', '123')
#     user10 = User(10, 'abc', 'muyaho', '호롤로')
#     user_list = [user1,
#                  user2,
#                  user3,
#                  user4,
#                  user5,
#                  user6,
#                  user7,
#                  user8,
#                  user9,
#                  user10]
#     random.shuffle(user_list)
#     user_list.sort()
#     for i in user_list:
#         print(i)
#     # print(user_list)
#     # print(user_list.sort())