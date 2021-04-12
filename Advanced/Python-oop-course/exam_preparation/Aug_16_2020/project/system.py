from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hw = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hw)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hw = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hw)

    @staticmethod
    def return_component_match(component_name, components):
        match = [component for component in components if component.name == component_name]
        return match

    @staticmethod
    def register_express_software(hw_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_match = System.return_component_match(hw_name, System._hardware)
        if not hardware_match:
            return "Hardware does not exist"

        hardware = hardware_match[0]
        express_sw = ExpressSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(express_sw)
            System._software.append(express_sw)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hw_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_match = System.return_component_match(hw_name, System._hardware)
        if not hardware_match:
            return "Hardware does not exist"

        hardware = hardware_match[0]
        light_sw = LightSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(light_sw)
            System._software.append(light_sw)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hw_name, sw_name):
        hardware_match = System.return_component_match(hw_name, System._hardware)
        software_match = System.return_component_match(sw_name, System._software)

        if not hardware_match or not software_match:
            return "Some of the components do not exist"

        hardware = hardware_match[0]
        software = software_match[0]
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def calculate_capacity(components, component_type):
        if component_type == "HW":
            return sum([component.capacity for component in components])
        return sum([component.capacity_consumption for component in components])

    @staticmethod
    def calculate_memory(components, component_type):
        if component_type == "HW":
            return sum([component.memory for component in components])
        return sum([component.memory_consumption for component in components])

    @staticmethod
    def analyze():
        hw_n = len(System._hardware)
        sw_n = len(System._software)
        result = f"System Analysis\nHardware Components: {hw_n}\nSoftware Components: {sw_n}"

        used_memory = System.calculate_memory(System._software, "SW")
        total_memory = used_memory + System.calculate_memory(System._hardware, "HW")
        result += f"\nTotal Operational Memory: {int(used_memory)} / {int(total_memory)}"

        used_capacity = System.calculate_capacity(System._software, "SW")
        total_capacity = used_capacity + System.calculate_capacity(System._hardware, "HW")
        result += f"\nTotal Capacity Taken: {int(used_capacity)} / {int(total_capacity)}"

        return result

    @staticmethod
    def get_components_of_given_type(components, component_type):
        return [component for component in components if isinstance(component, component_type)]

    @staticmethod
    def get_sw_components_names_as_string_or_none(components):
        names = [component.name for component in components]
        return None if not names else ', '.join(names)

    @staticmethod
    def system_split():
        result = ""
        for hw in System._hardware:
            hw_result = f"Hardware Component - {hw.name}"

            express_components = System.get_components_of_given_type(hw.software_components, ExpressSoftware)
            hw_result += f"\nExpress Software Components: {len(express_components)}"
            light_components = System.get_components_of_given_type(hw.software_components, LightSoftware)
            hw_result += f"\nLight Software Components: {len(light_components)}"

            used_memory = System.calculate_memory(hw.software_components, "SW")
            total_memory = used_memory + hw.memory
            hw_result += f"\nMemory Usage: {int(used_memory)} / {int(total_memory)}"

            used_capacity = System.calculate_capacity(hw.software_components, "SW")
            total_capacity = used_capacity + hw.capacity
            hw_result += f"\nCapacity Usage: {int(used_capacity)} / {int(total_capacity)}"

            sw_components = System.get_sw_components_names_as_string_or_none(hw.software_components)
            hw_result += f"\nType: {hw.type}\nSoftware Components: {sw_components}"

            result += hw_result
        return result








