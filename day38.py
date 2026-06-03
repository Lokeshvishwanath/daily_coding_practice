# Day 38 - QR Code Scanner

from PIL import Image
from pyzbar.pyzbar import decode

class QRScanner:

    def scan_qr(self, image_path):

        image = Image.open(image_path)

        decoded_objects = decode(image)

        if decoded_objects:

            for obj in decoded_objects:
                print("\nQR Code Content:")
                print(obj.data.decode("utf-8"))

        else:
            print("No QR Code found.")


def main():

    print("===== QR CODE SCANNER =====")

    image_path = input("Enter QR image path: ")

    scanner = QRScanner()

    try:
        scanner.scan_qr(image_path)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()