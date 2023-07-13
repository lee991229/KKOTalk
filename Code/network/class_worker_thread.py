from PyQt5 import QtCore
class WorkerServerThread(QtCore.QThread):
    def __init__(self, *args):
        super().__init__(*args)
        self.work = None

    def set_work(self, func):
        """
        실행 시킬 함수를 인자로 전달합니다. 여기선 () 통해 호출하지 않습니다.
        :param func:
        :return:
        """
        self.work = func

    def run(self):
        """
        q_thread.start()를 통해 동작시킬 로직을 작성합니다.
        :return:
        """
        self.work()
