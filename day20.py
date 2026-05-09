# Day 20 - Student Grade Management System

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def display_result(self):
        average = self.calculate_average()

        print("\n--- Student Report ---")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print(f"Average : {average:.2f}")

        if average >= 90:
            grade = "A+"
        elif average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        print(f"Grade   : {grade}")


def main():
    marks = [85, 92, 78, 88, 90]

    student = Student("Vishwanath", marks)

    student.display_result()


if __name__ == "__main__":
    main()