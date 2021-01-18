import uuid
from datetime import datetime
from khayyam import JalaliDatetime


class Payment:
    def __init__(self, payment_type, is_paid,  price):
        self.uuid = uuid.uuid4()
        self.payment_type = payment_type
        self.is_paid = is_paid
        self.price = price
        self._datetime = datetime.now()

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self._datetime)

    @classmethod
    def sample(cls):
        return cls(payment_type='cash', is_paid=True, price=60)


class Bill:
    def __init__(self, total_price, payment):
        self.uuid = uuid.uuid4()
        self.total_price = total_price
        self.payment = payment

    @classmethod
    def sample(cls):
        return cls(total_price=50, payment=Payment.sample())


# TODO-3: Set valid Payment instance for payment attr in Bill instance
# TODO-3: Add show_unpaid() classmethod to the Bill class which will return a
#       list of all unpaid bills, (Implementation is up to you)
# TODO-3: Add show_paid() classmethod to the Bill as show_unpaid() method
# TODO-3: Add paid_list() classmethod to the Payment class which will just
#       return a list of payments with True `is_paid` flag.
# TODO-3: Add pay() method to the Payment class which set is_paid flag True
# TODO-3: Add total_paid() classmethod to the Payment class which return an int
#       of total paid Payments
