# Day 36 - Image to ASCII Art Converter

from PIL import Image

class ASCIIConverter:

    def __init__(self):
        self.chars = "@%#*+=-:. "

    def convert(self, image_path, width=100):

        image = Image.open(image_path)

        aspect_ratio = image.height / image.width
        height = int(width * aspect_ratio * 0.55)

        image = image.resize((width, height))
        image = image.convert("L")

        pixels = image.getdata()

        ascii_art = ""

        for i, pixel in enumerate(pixels):

            ascii_art += self.chars[pixel * len(self.chars) // 256]

            if (i + 1) % width == 0:
                ascii_art += "\n"

        return ascii_art


def main():

    print("===== IMAGE TO ASCII CONVERTER =====")

    image_path = input("Enter image path: ")

    converter = ASCIIConverter()

    try:
        result = converter.convert(image_path)

        with open("ascii_art.txt", "w") as file:
            file.write(result)

        print("\nASCII art saved to ascii_art.txt")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()