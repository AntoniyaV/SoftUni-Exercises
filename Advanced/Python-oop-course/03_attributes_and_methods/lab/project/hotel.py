class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room_match = [room for room in self.rooms if room.number == room_number]
        if room_match:
            room_match[0].take_room(people)

    def free_room(self, room_number):
        room_match = [room for room in self.rooms if room.number == room_number]
        room_match[0].free_room()

    def print_status(self):
        self.guests = sum([room.guests for room in self.rooms])
        free_rooms = ', '.join(str(n) for n in [room.number for room in self.rooms if not room.is_taken])
        taken_rooms = ', '.join(str(n) for n in [room.number for room in self.rooms if room.is_taken])

        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {free_rooms}")
        print(f"Taken rooms: {taken_rooms}")
