# Day 59 - Image Resizer Tool

from PIL import Image

class ImageResizer:

    def resize_image(self, input_path, output_path, width, height):

        image = Image.open(input_path)

        resized_image = image.resize((width, height))

        resized_image.save(output_path)

        print(f"\nImage resized successfully!")
        print(f"Saved as: {output_path}")


def main():

    print("===== IMAGE RESIZER TOOL =====")

    input_path = input("Enter image path: ")

    output_path = input("Enter output image name: ")

    width = int(input("Enter new width: "))

    height = int(input("Enter new height: "))

    resizer = ImageResizer()

    try:

        resizer.resize_image(
            input_path,
            output_path,
            width,
            height
        )

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()# Day 59 - Image Resizer Tool

from PIL import Image

class ImageResizer:

    def resize_image(self, input_path, output_path, width, height):

        image = Image.open(input_path)

        resized_image = image.resize((width, height))

        resized_image.save(output_path)

        print(f"\nImage resized successfully!")
        print(f"Saved as: {output_path}")


def main():

    print("===== IMAGE RESIZER TOOL =====")

    input_path = input("Enter image path: ")

    output_path = input("Enter output image name: ")

    width = int(input("Enter new width: "))

    height = int(input("Enter new height: "))

    resizer = ImageResizer()

    try:

        resizer.resize_image(
            input_path,
            output_path,
            width,
            height
        )

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()