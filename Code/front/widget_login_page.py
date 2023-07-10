
class LoginWidget():

    def __init__(self):

        pass


    def assert_login(self):
        login_id = self.line_edit_id.text()
        login_pw = self.line_edit_pw.text()
        if self.main_controller.assert_login(login_id, login_pw) is True:
            self.main_controller.show_login_success()
