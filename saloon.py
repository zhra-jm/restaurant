import uuid

from lib import Root


class Table(Root):
    table_list = []
    object_list = []

    def __init__(self, capacity, number, reserved, is_available):
        self.uuid = uuid.uuid4()
        self.capacity = capacity
        self.number = number
        self.reserved = reserved
        self.is_available = is_available
        self.object_list.append(self)
        super().__init__()

    @classmethod
    def sample(cls, capacity=5, number=7, reserved=True, is_available=False):
        return cls(capacity=capacity, number=number, reserved=reserved, is_available=is_available)
