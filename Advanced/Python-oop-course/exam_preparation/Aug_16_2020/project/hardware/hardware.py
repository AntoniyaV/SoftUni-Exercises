from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hw_type: str, capacity: int, memory: int):
        self.name = name
        self.type = hw_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @staticmethod
    def is_enough(hw_value, sw_value):
        return hw_value >= sw_value

    def install(self, software: Software):
        if not self.is_enough(self.capacity, software.capacity_consumption) \
                or not self.is_enough(self.memory, software.memory_consumption):
            raise Exception("Software cannot be installed")

        self.software_components.append(software)
        self.capacity -= software.capacity_consumption
        self.memory -= software.memory_consumption

    def uninstall(self, software: Software):
        self.software_components.remove(software)
        self.capacity += software.capacity_consumption
        self.memory += software.memory_consumption
