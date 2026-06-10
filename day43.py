# Day 43 - Currency Converter

import requests

class CurrencyConverter:

    def convert_currency(self, from_currency, to_currency, amount):

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

        response = requests.get(url)

        data = response.json()

        rates = data["rates"]

        if to_currency in rates:

            converted_amount = amount * rates[to_currency]

            print(f"\n{amount} {from_currency} = "
                  f"{converted_amount:.2f} {to_currency}")

        else:
            print("Invalid target currency.")


def main():

    print("===== CURRENCY CONVERTER =====")

    from_currency = input("From Currency (e.g. USD): ").upper()

    to_currency = input("To Currency (e.g. INR): ").upper()

    amount = float(input("Enter Amount: "))

    converter = CurrencyConverter()

    try:
        converter.convert_currency(
            from_currency,
            to_currency,
            amount
        )

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()