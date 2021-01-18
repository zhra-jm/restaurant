class Discount:
    def __init__(self, code, count, start_date, end_date, percentage, minimum_order, maximum_order):
        self.code = code
        self.count = count
        self.start_date = start_date
        self.end_date = end_date
        self.percentage = percentage
        self.minimum_order = minimum_order
        self.maximum_order = maximum_order

    @classmethod
    def sample(cls):
        return cls(code=30, count=2, start_date=1, end_date=2,
                   percentage=10, minimum_order=10, maximum_order=30)
