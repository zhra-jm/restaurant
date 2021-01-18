import uuid


class Table:
    table_list = []

    def __init__(self, capacity, number, reserved, is_available):
        self.uuid = uuid.uuid4()
        self.capacity = capacity
        self.number = number
        self.reserved = reserved
        self.is_available = is_available

    @classmethod
    def sample(cls):
        return cls(capacity=5, number=7, reserved=True, is_available=False)
