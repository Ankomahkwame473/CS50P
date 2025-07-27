import sys
import pyfiglet
from tabulate import tabulate

def main():
    courses,credit_hours,marks = get_course_and_marks()
    universities = ["knust", "ucc", "uds", "ug"]
    print("\nThis program has the grading system for only KNUST, UCC, UG, and UDS")
    def get_university():
        try:
            return input("Which university's grading system do you want to use? ").lower().strip()
        except KeyboardInterrupt:
            sys.exit("\nProgram exited")

    def calculate():
        while True:
            university = get_university()
            if university in universities:
                grade,comment,honors,average,grade_point = calculate_grade(university,marks,credit_hours)
                break
            else:
                print("Invalid University input. Try again")
        if university == "knust":
            print(pyfiglet.figlet_format(f"{university.upper()} GRADING SYSTEM", font= 'small', width = 100))
            data,heading = display_knust_results(courses,credit_hours,marks,grade,comment)
            print(tabulate(data, headers=heading))
            print(f"CWA: {average:.2f}/100.00\nClass: {honors}")
        else:
            print(pyfiglet.figlet_format(f"{university.upper()} GRADING SYSTEM", font= 'small', width = 150))
            data,heading = display_other_results(courses,credit_hours,marks,grade,comment,grade_point)
            print(tabulate(data, headers=heading))
            if university == "uds":
                print(f"GPA: {average:.2f}/5.00\nClass: {honors}")
            else:
                print(f"GPA: {average:.2f}/4.00\nClass: {honors}")

    while True:
        try:
            calculate()
            recalculate = input("Would you like to calculate for a different University using the same marks? Press y for yes and n for no: ").strip().lower()
            if recalculate == "y":
                continue
            else:
                sys.exit("Program exited")
        except KeyboardInterrupt:
            sys.exit("\nProgram exited")

def get_course_and_marks():
    print(pyfiglet.figlet_format("ANKOMAH'S GPA / CWA CALC", font= 'small', width = 150))
    print("Enter the course and marks in the form: Course,marks,credit hours\nPress CTRL+D when all courses and marks are inputted OR CTRL+C to end program\n")
    courses = []
    marks = []
    credit_hours = []
    def get_mark():
        course_and_mark = input("Enter the name of the courses, marks, and credit hours: ").split(",")
        if len(course_and_mark) == 3:
            course,mark,credit_hour = course_and_mark[0].strip().title(),course_and_mark[1].strip(),course_and_mark[2].strip()
            courses.append(course),marks.append(float(mark)), credit_hours.append(float(credit_hour))
        else:
            print("Invalid input, Try again!")
    try:
        while True:
            get_mark()

    except ValueError:
        print("Invalid input, Try again!")
        get_mark()
    except KeyboardInterrupt:
        sys.exit("\nProgram exited")
    except EOFError:
        return courses,credit_hours,marks

def calculate_grade(university,marks,credit_hours):
    grade = []
    grade_point = []
    comment = []
    honors = ""
    sum_product = 0
    total_credit = 0

    if university == "knust":
        for i in range(len(marks)):
            if marks[i] < 40 and marks[i] >= 0:
                grade.append("F")
                comment.append("Fail")
            elif marks[i] < 50:
                grade.append("D")
                comment.append("Satisfactory")
            elif marks[i] < 60:
                grade.append("C")
                comment.append("Good")
            elif marks[i] < 70:
                grade.append("B")
                comment.append("Very Good")
            elif marks[i] <= 100:
                grade.append("A")
                comment.append("Excellent")
            else:
                sys.exit(f"Invalid Grade! {marks[i]} is not between 0-100%")
            sum_product += marks[i]*credit_hours[i]
            total_credit += credit_hours[i]
        try:
            average = sum_product/total_credit
            if average < 45 and CWA > 0:
                honors = "Fail"
            elif average < 50:
                honors = "Pass"
            elif average < 60:
                honors = "Second Class (Lower Division)"
            elif average < 60:
                honors = "Second Class (Upper Division)"
            elif average < 100:
                honors = "First Class"
        except ZeroDivisionError:
            sys.exit("Total credit cannot be zero!")
    elif university == "uds":
        for i in range(len(marks)):
            if marks[i] < 40 and marks[i] >= 0:
                grade.append("F")
                comment.append("Fail")
                grade_point.append(0.0)
            elif marks[i] < 45:
                grade.append("D")
                comment.append("Satisfactory")
                grade_point.append(1.5)
            elif marks[i] < 50:
                grade.append("D+")
                comment.append("Satisfactory")
                grade_point.append(2)
            elif marks[i] < 55:
                grade.append("C")
                comment.append("Good")
                grade_point.append(2.5)
            elif marks[i] < 60:
                grade.append("C+")
                comment.append("Good")
                grade_point.append(3)
            elif marks[i] < 65:
                grade.append("B")
                comment.append("Very Good")
                grade_point.append(3.5)
            elif marks[i] < 70:
                grade.append("B+")
                comment.append("Very Good")
                grade_point.append(4)
            elif marks[i] < 80:
                grade.append("A")
                comment.append("Excellent")
                grade_point.append(4.5)
            elif marks[i] <= 100:
                grade.append("A+")
                comment.append("Excellent")
                grade_point.append(5)
            else:
                sys.exit(f"Invalid Grade! {marks[i]} is not between 0-100%")
            sum_product += grade_point[i]*credit_hours[i]
            total_credit += credit_hours[i]
        try:
            average = sum_product/total_credit
            if average < 2 and average >= 1.5:
                honors = "Pass"
            elif average < 2.5:
                honors = "3rd Class"
            elif average < 3.5:
                honors = "Second Class (Lower Division)"
            elif average < 4.5:
                honors = "Second Class (Upper Division)"
            elif average <= 5:
                honors = "First Class"
        except ZeroDivisionError:
            sys.exit("Total credit cannot be zero!")

    elif university == "ucc" or "ug":
        for i in range(len(marks)):
            if marks[i] < 50 and marks[i] >= 0:
                grade.append("E")
                comment.append("Fail")
                grade_point.append(0.0)
            elif marks[i] < 55:
                grade.append("D")
                comment.append("Weak Pass")
                grade_point.append(1.0)
            elif marks[i] < 60:
                grade.append("D+")
                comment.append("Barely Satisfactory")
                grade_point.append(1.5)
            elif marks[i] < 65:
                grade.append("C")
                comment.append("Fair")
                grade_point.append(2.0)
            elif marks[i] < 70:
                grade.append("C+")
                comment.append("Average")
                grade_point.append(2.5)
            elif marks[i] < 75:
                grade.append("B")
                comment.append("Good")
                grade_point.append(3.0)
            elif marks[i] < 80:
                grade.append("B+")
                comment.append("Very Good")
                grade_point.append(3.5)
            elif marks[i] <= 100:
                grade.append("A")
                comment.append("Excellent")
                grade_point.append(4.0)
            else:
                sys.exit(f"Invalid Grade! {marks[i]} is not between 0-100%")
            sum_product += grade_point[i]*credit_hours[i]
            total_credit += credit_hours[i]
        try:
            average = sum_product/total_credit
            if average < 2 and average >= 1:
                honors = "Pass"
            elif average < 2.5:
                honors = "3rd Class"
            elif average < 3:
                honors = "Second Class (Lower Division)"
            elif average < 3.5:
                honors = "Second Class (Upper Division)"
            elif average <= 4:
                honors = "First Class"
        except ZeroDivisionError:
            sys.exit("Total credit cannot be zero!")

    return grade,comment,honors,average, grade_point


def display_knust_results(courses,credit_hours,marks,grade,comment):
    heading = ["Course Name","Credits","Mark","Grade","Interpretation"]
    data = []
    for i in range(len(courses)):
        data.append([courses[i],credit_hours[i],marks[i],grade[i],comment[i]])
    return data,heading

def display_other_results(courses,credit_hours,marks,grade,comment,grade_point):
    heading = ["Course Name","Credits","Mark","Grade Point","Grade","Interpretation"]
    data = []
    for i in range(len(courses)):
        data.append([courses[i],credit_hours[i],marks[i],grade_point[i],grade[i],comment[i]])
    return data,heading

if __name__ == "__main__":
    main()
