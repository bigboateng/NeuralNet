class Customer:
    def __init__(self, id):
        self.id = id

    def print_id(self):
        print("Id = {}".format(self.id))

class ReturningCustomer(Customer):
    def __init__(self, someId=None, date_purchased=None):
        Customer.__init__(self, someId)
        self.date = date_purchased


if __name__ == "__main__":
    rc = ReturningCustomer(33,22)
    rc.print_id()