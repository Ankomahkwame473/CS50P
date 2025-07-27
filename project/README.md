# ANKOMAH'S GPA / CWA CALCULATOR
#### Video Demo:  <URL HERE>
#### Description: This GPA/CWA calculator is used to calculate the Grade Point Average (GPA) or Cummulative Weight Average (CWA) of a student. Universities considered are KNUST, UCC, UG, and UDS (Ghanaian Universities). It also gives students the option to convert their CWA to GPA and vice versa depending on the grading system of the selected university.

For this project, the installable libraries used were `pyfiglet` and `tabulate`. These libraries helps in adding some aesthestics and also improve the organization of our ouput in the terminal.

This GPA/CWA calculator has 5 primary functions namely `main()`, `get_course_and_marks()`, `calculate_grade(university,marks,credit_hours)`, `display_knust_results(courses,credit_hours,marks,grade,comment)`, `display_other_results(courses,credit_hours,marks,grade,comment,grade_point)`. How these functions work has been explained in the section below:

### How the program works
```
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
```
In the `main()` function, the first function to be called is the the `get_course_and_marks()`. This function takes no arguments and it returns the courses, credit hours and raw scores inputted by the user. Upon calling the `get_course_and_marks()` in the `main()` function, the first line of code in the function to be excuted is the printing of the name of the program formatted by `pyfiglet` imported library. The font used is `small` with `width = 150`. The next line of code to be excuted is the also a print function which informs the user the required format of the input and also keyboard combinations that would help the user proceed (CTRL + D) or exit the program (CTRL + C). Within `get_course_and_marks()`, another function called `get_mark()` exist. This function when called, asks the user to input the name of the course, the marks obtained in the course, and the credit hours of the course in the format `course,marks,credit_hours`. When the user enters anything other than the required format, the program prints `Invalid input, Try again` and the program reprompts the user to input a valid format. In the case where user accidentally inputs white space either before or after any of the required inputs, the `strip()` function is used to eliminate it. After each successful input, the program splits the input and `append()` them into their respective empty lists after which the user is reprompted for a new input. If the input is complete, the user is required to press CTRL + D which raises `EOFError` exception for the program to proceed. The `get_course_and_marks()` function then returns a tuple containing a list of the course, credit hours, and marks.
```
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
```

In the `main()` function, the return values obtained from `get_course_and_marks()` is unpacked and stored in the variables courses,credit_hours,marks (`courses,credit_hours,marks = get_course_and_marks()`). As stated in the description, this program was designed for only 4 universities in Ghana namely Kwame Nkrumah University of Science and Technology (KNUST), University of Cape Coast (UCC), University of Ghana (UG), and University for Development Studies (UDS). These universities are stored in the the list called universities (`universities = ["knust", "ucc", "uds", "ug"]`). To make the user aware of this, the next line of code that is excuted is the print function which prints out `This program has the grading system for only KNUST, UCC, UG, and UDS`. Within the `main()`, another function called `get_university()` is created. This function returns the name of the university whose grading system is to be used for the the CWA/GPA calculation. Here, `try` and `except` was used in order to give the user the option of exiting the program in case there is a mistake in the input. When the `KeyboardInterrupt` exception is raised the program exits via `sys.exit()` with a message `Program exited`
```
def get_university():
        try:
            return input("Which university's grading system do you want to use? ").lower().strip()
        except KeyboardInterrupt:
            sys.exit("\nProgram exited")
```
Under the same `main()` function, another sub-function called `calculate()` has been created. Within this function, `get_university()` function is called and the return value is stored in the variable `university`. An `if` and `else` condition is used to check if what the user inputted is `in` the list called `universities`. If the condition is True, the function `calculate_grade(university,marks,credit_hours)` is called. This function takes `university`, `marks`and `credit_hours` as its input arguments. The function `calculate_grade(university,marks,credit_hours)` houses multiple conditional statements about the grading system of each university. It is also within this function that the GPA/CWA is calculated and the grade points and interpretations are generated. In the case where `ZeroDivisionError` exception is raised in the function, the program will exit via `sys.exit()`. The `calculate_grade(university,marks,credit_hours)` then returns `grade,comment,honors,average, grade_point` which is a mixed combination of nested lists, strings and integers.
```
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
```
Within the `calculate()` under the `main()` function, the return value of `calculate_grade()` is unpacked and assigned to various variables (`grade,comment,honors,average,grade_point = calculate_grade(university,marks,credit_hours)`). The next stage of the program is to display the results in a presentable and appealing format. This is why the installable libraries `pyfiglet` and `tabulate` were used. The first thing we consider here is the university's grading system. KNUST uses CWA whilst the rest uses GPA. As such, two functions has been created namely `display_knust_results` and `display_other_results`. Before these functions are called, `pyfiglet` is used to print out the "name of the university" plus "grading system" (`print(pyfiglet.figlet_format(f"{university.upper()} GRADING SYSTEM", font= 'small', width = 100))`). After this, either `display_knust_results` or `display_other_results` function will be called based on the condition that would be met (`if` or `else`). The `display_knust_results` function takes in `courses,credit_hours,marks,grade,comment` arguments while `display_other_results` takes in an extra argument called `grade_point`. Within these functions, a heading for the table is generated and a `for` loop is used to append the arranged input arguments to an empty list called `data`. These functions then return `data,heading`. The return values from these functions are unpacked into two varialbles (`data,heading`) in the `main()` function. The unpacked values are passed into the `tabulate` function (`tabulate(data, headers=heading)`). The results is then printed to the terminal. After results is printed, the user is prompted again asking if they would like to calculate their GPAs/CWAs in a different grading system. If the user answers `y` which stands for yes, `calculate()` function is called and the calculation is done again in a the chosen grading system.

### Testing the code
To test if the code works properly, `test_project.py` file has been created. The functions `display_knust_results, display_other_results, calculate_grade` were tested using pytest.



By Ankomah Kwame
