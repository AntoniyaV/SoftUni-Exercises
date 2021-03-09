class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        customers = '\n'.join([customer.__repr__() for customer in self.customers])
        dvds = '\n'.join([dvd.__repr__() for dvd in self.dvds])
        return f'{customers}\n{dvds}'

    @staticmethod
    def dvd_capacity():
        dvd_capacity = 15
        return dvd_capacity

    @staticmethod
    def customer_capacity():
        customer_capacity = 10
        return customer_capacity

    @staticmethod
    def capacity_exceeded(capacity, items):
        return capacity == items

    @staticmethod
    def find_object(obj_id, objs_list):
        match = [obj for obj in objs_list if obj.id == obj_id]
        return match[0] if match else None

    def add_customer(self, customer):
        if not self.capacity_exceeded(self.customer_capacity(), len(self.customers)):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if not self.capacity_exceeded(self.dvd_capacity(), len(self.dvds)):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.find_object(customer_id, self.customers)
        dvd_by_customer = self.find_object(dvd_id, customer.rented_dvds)
        dvd = self.find_object(dvd_id, self.dvds)

        if dvd_by_customer:
            return f"{customer.name} has already rented {dvd_by_customer.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_object(customer_id, self.customers)
        dvd = self.find_object(dvd_id, customer.rented_dvds)

        if not dvd:
            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"
