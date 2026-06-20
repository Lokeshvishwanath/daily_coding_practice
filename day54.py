# Day 54 - QR Code Generator with Image Save

import qrcode

class QRCodeGenerator:

    def generate_qr(self, data, filename):

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )

        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(fill_color="black",
                              back_color="white")

        image.save(filename)

        print(f"\nQR Code saved as '{filename}'")


def main():

    print("===== QR CODE GENERATOR =====")

    data = input("Enter text or URL: ")

    filename = input(
        "Enter output filename (e.g., myqr.png): "
    )

    generator = QRCodeGenerator()

    try:

        generator.generate_qr(
            data,
            filename
        )

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()