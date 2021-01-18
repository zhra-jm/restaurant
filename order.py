import uuid
from khayyam import  JalaliDatetime
from datetime import datetime
from menu import Item
from saloon import Table
from finance import Bill


class Order:
    in_out_list = ["I", "O"]
    unpaid_orders = []
    orders = []

    def __init__(self, item_dict, in_out, bill, table):
        self.uuid = uuid.uuid4()
        self.item_dict = item_dict
        self.in_out = in_out.upper()
        self.bill = bill
        self.table = table
        self._datetime = datetime.now()
        self.store()

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self._datetime)

    @classmethod
    def sample(cls):
        return cls(item_dict={Item.sample()}, bill=cls.set_bill(cls.unpaid_orders[0]),
                   in_out="i", table=Table.sample())

    def store(self):
        if self.bill.payment.is_paid:
            self.unpaid_orders.append(self)
        self.orders.append(self)

    def assign_table(self, table_num):
        if self.table.reserved(table_num) is False:
            self.table.number = table_num
        self.table.is_available = True

    def check_in_out(self):
        if self.in_out not in self.in_out_list:
            print('your in out type is incorrect!')

    def set_bill(self):
        s = 0
        for order in self.orders:
            s += order.item.price
        pay = self.bill.payment.sample()
        return Bill(s, pay)

# TODO-2: Add set_bill method to the Order class which create proper Bill
#       instance according to the items in the order
