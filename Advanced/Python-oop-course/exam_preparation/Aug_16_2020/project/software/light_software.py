from project.software.software import Software


class LightSoftware(Software):
    software_type = "Light"
    capacity_coef = 1.5
    memory_coef = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        capacity_consumption *= self.capacity_coef
        memory_consumption *= self.memory_coef
        super().__init__(name, self.software_type, capacity_consumption, memory_consumption)
