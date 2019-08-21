class Value:
    def __set__(self, instance, value):
        self.value = value * (1 - instance.commission)

    def __get__(self, instance, owner):
        return self.value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission