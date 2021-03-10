class Gym:
    customers = []
    trainers = []
    equipment = []
    plans = []
    subscriptions = []

    @staticmethod
    def element_is_present(element, collection):
        return element in collection

    @staticmethod
    def get_element(id, collection):
        element = [el for el in collection if el.id == id]
        return element[0]

    def add_customer(self, customer):
        if not self.element_is_present(customer, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not self.element_is_present(trainer, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not self.element_is_present(equipment, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not self.element_is_present(plan, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not self.element_is_present(subscription, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_element(subscription_id, self.subscriptions)
        customer = self.get_element(subscription.customer_id, self.customers)
        trainer = self.get_element(subscription.trainer_id, self.trainers)
        plan = self.get_element(subscription.exercise_id, self.plans)
        equipment = self.get_element(plan.equipment_id, self.equipment)
        info = [subscription.__repr__(), customer.__repr__(), trainer.__repr__(), equipment.__repr__(), plan.__repr__()]
        return '\n'.join(info)
