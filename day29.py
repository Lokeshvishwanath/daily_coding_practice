# Day 29 - QR Code Generator

import qrcode

class QRCodeGenerator:

    def generate_qr(self, data, filename):
        qr = qrcode.make(data)

        qr.save(filename)

        print(f"QR Code saved as '{filename}'")


def main():
    print("===== QR Code Generator =====")

    data = input("Enter text or URL: ")

    filename = input("Enter file name (example: qr.png): ")

    generator = QRCodeGenerator()

    generator.generate_qr(data, filename)


if __name__ == "__main__":
    main()