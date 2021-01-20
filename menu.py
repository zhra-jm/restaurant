import uuid
from datetime import datetime
from khayyam import JalaliDatetime


class Item:
    item_id = 0
    item_type_list = ['f', 'b', 's']
    food_list = []
    beverage_list = []
    starter_list = []

    def __init__(self, name, item_type, price):
        self.uuid = uuid.uuid4()
        self.name = name
        self.item_type = item_type.lower()
        self.check_item_type()
        self.price = price
        self._datetime = datetime.now()
        self.item_id = self.generate_id()

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self._datetime)

    def check_item_type(self):
        if self.item_type not in self.item_type_list:
            print('your item type is incorrect!')

    @classmethod
    def generate_id(cls):
        cls.item_id += 1
        return cls.item_id

    @classmethod
    def sample(cls):
        return cls(name='item1', item_type='f', price=10)

    @classmethod
    def sample2(cls):
        return cls(name='item2', item_type='b', price=1)

# TODO-3: Add show_menu() classmethod to the Item class which will print all
#       items in the menu
# TODO-3: Add prompt() method to the Item class which will get proper dict for
#       creating each single item from user input and return data
