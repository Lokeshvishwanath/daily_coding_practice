# Day 21 - Quiz Game Project

class QuizGame:
    def __init__(self):
        self.questions = {
            "What is the capital of India?": "Delhi",
            "Which language is used for web apps?": "JavaScript",
            "Who developed Python?": "Guido van Rossum",
            "What does CPU stand for?": "Central Processing Unit"
        }

        self.score = 0

    def start_quiz(self):
        print("=== Welcome to Quiz Game ===\n")

        for question, answer in self.questions.items():
            user_answer = input(question + " ")

            if user_answer.strip().lower() == answer.lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! Correct Answer: {answer}\n")

        print("=== Quiz Finished ===")
        print(f"Your Score: {self.score}/{len(self.questions)}")


def main():
    game = QuizGame()
    game.start_quiz()


if __name__ == "__main__":
    main()