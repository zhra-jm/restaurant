from lib import Root


class Discount(Root):
    discount_list = []
    object_list = []

    def __init__(self, code, count, start_date, end_date, percentage,
                 minimum_order, maximum_order):
        self.code = code
        self.count = count
        self.start_date = start_date
        self.end_date = end_date
        self.percentage = percentage
        self.minimum_order = minimum_order
        self.maximum_order = maximum_order
        self.object_list.append(self)
        super().__init__()
    @classmethod
    def sample(cls, code=30, count=2, start_date=1, end_date=2,
               percentage=10, minimum_order=10, maximum_order=30):
        return cls(code=code, count=count, start_date=start_date, end_date=end_date,
                   percentage=percentage, minimum_order=minimum_order, maximum_order=maximum_order)
