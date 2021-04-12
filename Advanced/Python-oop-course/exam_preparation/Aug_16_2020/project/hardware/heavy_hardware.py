from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    hardware_type = "Heavy"
    capacity_coef = 2
    memory_coef = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        capacity *= self.capacity_coef
        memory *= self.memory_coef
        super().__init__(name, self.hardware_type, capacity, memory)
