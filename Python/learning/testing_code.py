class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.purchase = []


c = Customer('jeff')

print(c.is_admin)
print(c.name)
