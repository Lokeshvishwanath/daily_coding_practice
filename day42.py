# Day 42 - Website Status Checker

import requests

class WebsiteChecker:

    def check_website(self, url):

        try:

            response = requests.get(url, timeout=5)

            print(f"\nWebsite: {url}")
            print(f"Status Code: {response.status_code}")

            if response.status_code == 200:
                print("Website is UP ✅")
            else:
                print("Website returned an issue ⚠️")

        except requests.exceptions.RequestException:
            print("Website is DOWN ❌")


def main():

    print("===== WEBSITE STATUS CHECKER =====")

    url = input("Enter website URL: ")

    checker = WebsiteChecker()

    checker.check_website(url)


if __name__ == "__main__":
    main()