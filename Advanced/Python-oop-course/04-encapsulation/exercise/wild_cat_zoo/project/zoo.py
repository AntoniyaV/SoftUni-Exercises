class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    @staticmethod
    def is_capacity_enough(elements, capacity):
        return len(elements) < capacity

    @staticmethod
    def is_budget_enough(expenses, budget):
        return expenses <= budget

    @staticmethod
    def get_element(name, instances):
        match = [instance for instance in instances if instance.name == name]
        return match[0] if match else None

    @staticmethod
    def get_sum_of_salaries(workers):
        return sum([worker.salary for worker in workers])

    @staticmethod
    def get_sum_of_animal_needs(animals):
        return sum([animal.get_needs() for animal in animals])

    @staticmethod
    def get_instances_of_same_type(instances, instance_type):
        return [instance for instance in instances if instance.__class__.__name__ == instance_type]

    @staticmethod
    def join_instances_info(instances):
        return '\n'.join(repr(instance) for instance in instances)

    def get_instances_status(self, all_instances, instances_types, instances_name):
        status = f"You have {len(all_instances)} {instances_name}"

        for instance_type in instances_types:
            instances_of_same_type = self.get_instances_of_same_type(all_instances, instance_type)
            status += f"\n----- {len(instances_of_same_type)} {instance_type}s:\n{self.join_instances_info(instances_of_same_type)}"

        return status

    def add_animal(self, animal, price):
        if not self.is_capacity_enough(self.animals, self.__animal_capacity):
            return "Not enough space for animal"

        if not self.is_budget_enough(price, self.__budget):
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.is_capacity_enough(self.workers, self.__workers_capacity):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker = self.get_element(worker_name, self.workers)
        if not worker:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        workers_salaries = self.get_sum_of_salaries(self.workers)
        if not self.is_budget_enough(workers_salaries, self.__budget):
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= workers_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_needs = self.get_sum_of_animal_needs(self.animals)
        if not self.is_budget_enough(animals_needs, self.__budget):
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_needs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        # lions = self.get_instances_of_same_type(self.animals, 'Lion')
        # lions_info = f"----- {len(lions)} Lions:\n{self.join_instances_info(lions)}"
        # tigers = self.get_instances_of_same_type(self.animals, 'Tiger')
        # tigers_info = f"----- {len(tigers)} Lions:\n{self.join_instances_info(tigers)}"
        # cheetahs = self.get_instances_of_same_type(self.animals, 'Cheetah')
        # cheetahs_info = f"----- {len(cheetahs)} Lions:\n{self.join_instances_info(cheetahs)}"
        # return f"You have {len(self.animals)} animals\n{lions_info}\n{tigers_info}\n{cheetahs_info}"

        animals_types = ['Lion', 'Tiger', 'Cheetah']
        return self.get_instances_status(self.animals, animals_types, 'animals')

    def workers_status(self):
        # keepers = self.get_instances_of_same_type(self.workers, 'Keeper')
        # keepers_info = f"----- {len(keepers)} Keepers:\n{self.join_instances_info(keepers)}"
        # caretakers = self.get_instances_of_same_type(self.workers, 'Caretaker')
        # caretakers_info = f"----- {len(caretakers)} Caretakers:\n{self.join_instances_info(caretakers)}"
        # vets = self.get_instances_of_same_type(self.workers, 'Vet')
        # vets_info = f"----- {len(vets)} Lions:\n{self.join_instances_info(vets)}"
        # return f"You have {len(self.workers)} animals\n{keepers_info}\n{caretakers_info}\n{vets_info}"

        workers_types = ['Keeper', 'Caretaker', 'Vet']
        return self.get_instances_status(self.workers, workers_types, 'workers')
