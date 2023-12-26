class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4
        if photos_count % 4 != 0:
            pages += 1
        return cls(pages)

    def add_photo(self, label: str) -> str:
        for cell_index in range(len(self.photos)):
            if len(self.photos[cell_index]) < 4:
                self.photos[cell_index].append(label)
                return f"{label} photo added successfully on page {cell_index + 1} slot {len(self.photos[cell_index])}"
        return "No more free slots"

    def display(self) -> str:
        photos_repr = "-----------\n"
        for page in self.photos:
            photos_repr += " ".join(["[]" for photo_name in page]) + "\n"
            photos_repr += "-----------\n"
        return photos_repr


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())