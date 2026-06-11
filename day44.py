# Day 44 - Random Joke Generator

import requests

class JokeGenerator:

    def get_joke(self):

        url = "https://official-joke-api.appspot.com/random_joke"

        response = requests.get(url)

        if response.status_code == 200:

            joke = response.json()

            print("\n🤣 Random Joke")
            print("-------------------------")
            print(joke["setup"])
            print(joke["punchline"])

        else:
            print("Failed to fetch joke.")


def main():

    print("===== RANDOM JOKE GENERATOR =====")

    joke_app = JokeGenerator()

    try:
        joke_app.get_joke()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()