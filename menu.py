import uuid
from datetime import datetime
from khayyam import JalaliDatetime

from lib import Root


class Item(Root):
    item_list = []
    object_list = []
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
        self.object_list.append(self)
        super().__init__()

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
    def sample(cls, name='item1', item_type='f', price=10):
        return cls(name=name, item_type=item_type, price=price)

    @classmethod
    def show_menu(cls):
        print("FOOD MENU")
        for food in cls.food_list:
            print(food)
        print("BEVERAGE MENU")
        for beverage in cls.beverage_list:
            print(beverage)
        print("STARTER MENU")
        for starter in cls.starter_list:
            print(starter)

    def prompt(self):
        return {'name': input('name: '), 'item_type': input("item type: "), 'price': input('price: ')}

# TODO-3: Add prompt() method to the Item class which will get proper dict for
#       creating each single item from user input and return data
