# Day 51 - Bulk Email Validator

import re

class EmailValidator:

    def __init__(self):
        self.pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def validate_email(self, email):
        return bool(re.match(self.pattern, email))

    def validate_list(self, emails):

        valid_emails = []
        invalid_emails = []

        for email in emails:

            if self.validate_email(email):
                valid_emails.append(email)
            else:
                invalid_emails.append(email)

        return valid_emails, invalid_emails


def main():

    print("===== BULK EMAIL VALIDATOR =====")

    email_input = input(
        "Enter emails separated by commas:\n"
    )

    emails = [email.strip()
              for email in email_input.split(",")]

    validator = EmailValidator()

    valid, invalid = validator.validate_list(emails)

    print("\n✅ Valid Emails")
    for email in valid:
        print(email)

    print("\n❌ Invalid Emails")
    for email in invalid:
        print(email)


if __name__ == "__main__":
    main()