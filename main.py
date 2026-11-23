"""
Student Grade Management System

A command-line application to manage student grades, calculate grade statistics
(average, highest, and lowest), and interact with users through a clean CLI menu.
"""


class StudentGradeManager:
    """Manages student grade data and performs statistical operations.

    Attributes:
        students (list): A list of student names.
        grades (list): A list of corresponding integer or float grades (0-100).
    """

    def __init__(self):
        """Initialize the students and grades attributes as empty lists."""
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: int) -> bool:
        """Add a student and their grade to the system.

        Validates that the grade is between 0 and 100 before adding.

        Args:
            name (str): The name of the student.
            grade (int): The student's grade (0-100).

        Returns:
            bool: True if student and grade were added successfully, False otherwise.
        """
        # Validate student name
        if not isinstance(name, str) or not name.strip():
            print("Error: Student name cannot be empty.")
            return False

        # Validate grade type and range
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            print("Error: Grade must be a numeric value between 0 and 100.")
            return False

        if not (0 <= grade <= 100):
            print("Error: Grade must be between 0 and 100.")
            return False

        # Append student name and grade to corresponding lists
        self.students.append(name.strip())
        self.grades.append(grade)
        print(f"Student {name.strip()} with grade {grade} added successfully!")
        return True

    def display_results(self):
        """Calculate and display the average, highest, and lowest grades among students.

        If there are no students, displays an informative message.
        """
        if not self.grades:
            print("\nNo student data available. Please add students first.")
            return

        # Calculate statistics using loops / standard operations
        total_grade = 0
        highest_grade = self.grades[0]
        lowest_grade = self.grades[0]

        for grade in self.grades:
            total_grade += grade
            if grade > highest_grade:
                highest_grade = grade
            if grade < lowest_grade:
                lowest_grade = grade

        average_grade = total_grade / len(self.grades)

        print("\nGrade Summary:")
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Highest Grade: {highest_grade}")
        print(f"Lowest Grade: {lowest_grade}")

    def run(self):
        """Continuously prompt the user with a menu to add students, display results, or exit."""
        while True:
            print("\n1. Add Student")
            print("2. Display Results")
            print("3. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                # Prompt for student name
                name = input("Enter the student's name: ").strip()
                while not name:
                    print("Error: Student name cannot be empty.")
                    name = input("Enter the student's name: ").strip()

                # Prompt and validate student grade
                while True:
                    grade_input = input("Enter the student's grade (0-100): ").strip()
                    try:
                        grade = int(grade_input)
                        if 0 <= grade <= 100:
                            self.add_student(name, grade)
                            break
                        else:
                            print("Error: Grade must be between 0 and 100.")
                    except ValueError:
                        print("Error: Invalid input. Please enter an integer between 0 and 100.")

            elif choice == "2":
                self.display_results()

            elif choice == "3":
                print("Exiting the program.")
                break

            else:
                print("Error: Invalid choice. Please enter 1, 2, or 3.")


def main():
    """Entry point for running the Student Grade Management System."""
    manager = StudentGradeManager()
    manager.run()


if __name__ == "__main__":
    main()
