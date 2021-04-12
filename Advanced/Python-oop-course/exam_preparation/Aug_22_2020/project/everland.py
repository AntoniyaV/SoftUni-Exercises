from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.rooms.alone_old import AloneOld


class Everland:
    def __init__(self):
        self.rooms = []

    @staticmethod
    def get_children_info(children):
        result = ""
        for n in range(len(children)):
            child = children[n]
            cost = child.cost * 30
            result += f"\n--- Child {n + 1} monthly cost: {cost:.2f}$"
        return result

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        rooms_to_remove = []

        for room in self.rooms:
            room_consumption = room.expenses + room.room_cost
            if room_consumption <= room.budget:
                room.budget -= room_consumption
                result.append(f"{room.family_name} paid {room_consumption:.2f}$ and have {room.budget:.2f}$ left.")

            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_remove.append(room)

        for room in rooms_to_remove:
            self.rooms.remove(room)

        return "\n".join(result)

    def status(self):
        total_population = sum([room.members_count for room in self.rooms])
        result = f"Total population: {total_population}"

        for room in self.rooms:
            room_result = f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"

            if isinstance(room, YoungCoupleWithChildren):
                room_result += self.get_children_info(room.children)

            if not isinstance(room, AloneOld):
                appliances_cost = sum([appliance.get_monthly_expense() for appliance in room.appliances])
                room_result += f"\n--- Appliances monthly cost: {appliances_cost:.2f}$"

            result += f"\n{room_result}"

        return result

