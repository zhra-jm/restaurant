import uuid
from khayyam import JalaliDatetime
from datetime import datetime

from lib import Root
from menu import Item
from saloon import Table
from finance import Bill, Payment


class Order(Root):
    order_list = []
    in_out_list = ["I", "O"]
    unpaid_orders = []
    orders = []
    object_list = []

    def __init__(self, item_dict, in_out, table):
        self.uuid = uuid.uuid4()
        self.item_dict = item_dict
        self.in_out = in_out.upper()
        self.table = table
        self._datetime = datetime.now()
        self.store_orders()
        self.bill = self.set_bill()
        self.store_unpaid_orders()
        self.object_list.append(self)
        super().__init__()

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self._datetime)

    @classmethod
    def sample(cls, item_dict=None, in_out="i", table=Table.sample()):
        if item_dict is None:
            item_dict = {Item.sample: 2}
        return cls(item_dict=item_dict, in_out=in_out, table=table)

    def store_orders(self):
        self.orders.append(self)
        Bill.orders_list.append(self)

    def store_unpaid_orders(self):
        for order in self.orders:
            if not order.bill.payment.is_paid:
                self.unpaid_orders.append(self)
                Bill.unpaid_list.append(self)

    def assign_table(self, table_num):
        if self.table.reserved(table_num) is False:
            self.table.number = table_num
        self.table.is_available = True

    def check_in_out(self):
        if self.in_out not in self.in_out_list:
            print('your in out type is incorrect!')

    def set_bill(self):
        all_prices = 0
        for item in self.item_dict:
            all_prices += item.price * self.item_dict[item]
        return Bill(total_price=all_prices, payment=Payment(
            price=all_prices,
            payment_type='cash',
            is_paid=False))
