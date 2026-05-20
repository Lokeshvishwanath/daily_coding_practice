# Day 31 - AI Text Summarizer

from textwrap import shorten

class TextSummarizer:

    def summarize_text(self, text, max_length=100):

        summary = shorten(text, width=max_length, placeholder="...")

        return summary


def main():

    print("===== AI TEXT SUMMARIZER =====\n")

    paragraph = input("Enter a long paragraph:\n\n")

    summarizer = TextSummarizer()

    result = summarizer.summarize_text(paragraph)

    print("\n===== SUMMARY =====")
    print(result)


if __name__ == "__main__":
    main()