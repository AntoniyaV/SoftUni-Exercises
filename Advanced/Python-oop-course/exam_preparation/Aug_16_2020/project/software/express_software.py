from project.software.software import Software


class ExpressSoftware(Software):
    software_type = "Express"
    memory_coef = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        memory_consumption *= self.memory_coef
        super().__init__(name, self.software_type, capacity_consumption, memory_consumption)
