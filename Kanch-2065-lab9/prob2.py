"""
Kanch Ruansiripiyakul 633040206-5
"""

import abc


class Image(abc.ABC):
    @abc.abstractmethod
    def load_image(self):
        pass

    @abc.abstractmethod
    def save_image(self):
        pass


class Bitmap(Image):
    def save_image(self, filename):
        print(f"saving bitmap file {filename}")

    def load_image(self, filename):
        print(f"loading bitmap file {filename}")


class Jpeg(Image):
    def save_image(self, filename):
        print(f"saving jpeg file {filename}")

    def load_image(self, filename):
        print(f"loading jpeg file {filename}")


if __name__ == "__main__":
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")
