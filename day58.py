# Day 58 - URL Shortener using TinyURL API

import requests

class URLShortener:

    def shorten_url(self, long_url):

        api_url = f"https://tinyurl.com/api-create.php?url={long_url}"

        response = requests.get(api_url)

        if response.status_code == 200:

            print("\nOriginal URL:")
            print(long_url)

            print("\nShort URL:")
            print(response.text)

        else:
            print("Failed to shorten URL.")


def main():

    print("===== URL SHORTENER =====")

    long_url = input("Enter URL: ")

    shortener = URLShortener()

    try:

        shortener.shorten_url(long_url)

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()