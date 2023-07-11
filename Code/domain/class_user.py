class User:
    def __init__(self, user_id, username, password, nickname):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.nickname = nickname

    # def __str__(self):
    #     return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"
