from lib import Root


class Supervisor(Root):
    object_list = []
    supervisor_list = []

    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.object_list.append(self)
        super().__init__()

    @classmethod
    def sample(cls, username='user1', password=1234, phone_number='09123456789'):
        return cls(username=username, password=password, phone_number=phone_number)
