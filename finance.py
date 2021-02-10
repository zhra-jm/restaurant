import uuid
from datetime import datetime
from khayyam import JalaliDatetime

from lib import Root


class Payment(Root):
    payment_list =[]
    object_list = []
    pay_list = []

    def __init__(self, payment_type, is_paid, price):
        self.uuid = uuid.uuid4()
        self.payment_type = payment_type
        self.is_paid = is_paid
        self.price = price
        self._datetime = datetime.now()
        self.paid_list()
        self.object_list.append(self)
        super().__init__()

    def paid_list(self):
        if self.is_paid:
            self.pay_list.append(self)

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self._datetime)

    @classmethod
    def sample(cls, payment_type='cash', is_paid=True, price=60):
        return cls(payment_type=payment_type, is_paid=is_paid, price=price)

    def pay(self):
        self.is_paid = True

    @classmethod
    def total_paid(cls):
        return len(cls.pay_list)


class Bill(Root):
    bill_list = []
    object_list = []
    unpaid_list = []
    orders_list = []

    def __init__(self, total_price, payment):
        self.uuid = uuid.uuid4()
        self.total_price = total_price
        self.payment = payment
        self.object_list.append(self)
        super().__init__()

    @classmethod
    def sample(cls, total_price=50, payment=Payment.sample()):
        return cls(total_price=total_price, payment=payment)

    @classmethod
    def show_unpaid(cls):
        return cls.unpaid_list

    @classmethod
    def paid_list(cls):
        true_flag = []
        for payment in Payment.object_list:
            if payment.is_paid is True:
                true_flag.append(payment)
        return true_flag

    @classmethod
    def show_paid(cls):
        result = []
        for order in cls.orders_list:
            if order not in cls.unpaid_list:
                result.append(order)
        return result

# Set valid Payment instance for payment attr in Bill instance
