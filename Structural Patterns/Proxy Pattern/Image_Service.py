from interface import Image


class Service(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_image()

    def _load_image(self):
        print(f"Loading image from disk: {self.filename}")

    def display_image(self):
        print("Displaying Image:", self.filename)
        