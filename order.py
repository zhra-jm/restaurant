import uuid
from khayyam import JalaliDatetime
from datetime import datetime

from menu import Item
from saloon import Table
from finance import Bill, Payment


class Order:
    in_out_list = ["I", "O"]
    unpaid_orders = []
    orders = []

    def __init__(self, item_dict, in_out, table):
        self.uuid = uuid.uuid4()
        self.item_dict = item_dict
        self.in_out = in_out.upper()
        self.table = table
        self._datetime = datetime.now()
        self.store_orders()
        self.bill = self.set_bill()
        self.store_unpaid_orders()

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self._datetime)

    @classmethod
    def sample(cls):
        return cls(item_dict={Item.sample(): 2, Item.sample2(): 2},
                   in_out="i", table=Table.sample())

    def store_orders(self):
        self.orders.append(self)

    def store_unpaid_orders(self):
        for order in self.orders:
            if not order.bill.payment.is_paid:
                self.unpaid_orders.append(self)

    def assign_table(self, table_num):
        if self.table.reserved(table_num) is False:
            self.table.number = table_num
        self.table.is_available = True

    def check_in_out(self):
        if self.in_out not in self.in_out_list:
            print('your in out type is incorrect!')

    @classmethod
    def set_bill(cls):
        s = 0
        for order in cls.orders:
            'absolutely wrong'
            s += order.item_dict.keys['price'] * order.item_dict.values
        pay = Payment('cash', True, s)
        return Bill(s, pay)

# TODO-2: Add set_bill method to the Order class which create proper Bill
#       instance according to the items in the order

