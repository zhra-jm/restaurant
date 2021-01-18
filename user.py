class Supervisor:
    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number

    @classmethod
    def sample(cls):
        return cls(username='user1', password=1234, phone_number='09123456789')
