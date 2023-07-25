"""
Title: "Student Grading Program"

Description:
You are tasked with creating a simple student grading program using Python. The program should take input from the user for the marks obtained by a student in a subject and then calculate and display the grade based on the following grading scale:

90 or above: A+
80 to 89: A
70 to 79: B
60 to 69: C
50 to 59: D
Below 50: Fail

Requirements:
Use control statements (if-elif-else) to determine the grade based on the marks obtained by the student.
Handle any potential errors in the user input (e.g., invalid marks) and display appropriate messages to the user.
Implement a loop to allow the user to calculate the grade for multiple students until they decide to exit.
Display the calculated grade for each student.
"""

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

while True:
    try:
        marks = float(input("Enter the marks obtained by the student: "))
        if marks < 0 or marks > 100:
            print("Invalid marks! Marks should be between 0 and 100.")
        else:
            grade = calculate_grade(marks)
            print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    
    another_student = input("Do you want to calculate grade for another student? (yes/no): ")
    if another_student.lower() != "yes":
        break
