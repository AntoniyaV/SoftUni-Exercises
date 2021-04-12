from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    hardware_type = "Power"
    capacity_coef = 0.25
    memory_coef = 1.75

    def __init__(self, name: str, capacity: int, memory: int):
        capacity *= self.capacity_coef
        memory *= self.memory_coef
        super().__init__(name, self.hardware_type, capacity, memory)
