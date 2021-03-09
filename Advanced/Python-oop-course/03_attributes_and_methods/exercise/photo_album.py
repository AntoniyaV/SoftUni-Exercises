class PhotoAlbum:
    max_photos_on_page = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for n in range(pages)]

    @staticmethod
    def check_for_free_slots(album, pages, max_slots_on_page):
        result = sum([len(page) for page in album])
        return result < max_slots_on_page * pages

    @staticmethod
    def get_added_photo_position(album, pages, max_slots_on_page, name):
        for page_number in range(pages):
            for slot_number in range(max_slots_on_page):
                if slot_number not in range(len(album[page_number])):
                    album[page_number].append(name)
                    return page_number + 1, slot_number + 1


    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        if not self.check_for_free_slots(self.photos, self.pages, PhotoAlbum.max_photos_on_page):
            return "No more free spots"

        page_number, slot_number = self.get_added_photo_position(self.photos, self.pages, PhotoAlbum.max_photos_on_page, label)
        return f"{label} photo added successfully on page {page_number} slot {slot_number}"

    def display(self):
        separator = f"{'-' * 11}\n"
        result = separator
        for row in self.photos:
            joined_row = ' '.join('[]' for _ in row)
            result += joined_row + '\n' + separator
        return result


# Test code
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
