class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name, end = "\t\t")
        print(self.DoB)

def student_count():
    s_count = int(input("Enter the number of students : "))
    return s_count

def student_info(s_count):
    s_list = []
    for i in range(s_count):
        print("Student : ", i +1)
        id = input("\tStudent ID : ")
        name = input("\tStudent Name : ")
        DoB = input("\tStudent Date of Birth (DD/MM/YYYY) : ")
        s_list.append(Student(id, name, DoB))
    return s_list

def show_s_info(s_count, s_list):
    print("Student Information")
    print("ID\t\tName\t\tDoB")
    for i in range(s_count):
        s_list[i].display()

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name)

def course_count():
    c_count = int(input("Enter the number of courses : "))
    return c_count

def course_info(c_count):
    c_list = []
    for i in range(c_count):
        print("Course : ", i +1)
        id = input("\tCourse ID : ")
        name = input("\tCourse Name : ")
        c_list.append(Course(id, name))
    return c_list

def show_c_info(c_count, c_list):
    print("Course Information")
    print("ID\t\tName")
    for i in range(c_count):
        c_list[i].display()

       
class Mark:
    def __init__(self, id, name, course, mark):
        self.id = id
        self.name = name
        self.course = course
        self.mark = mark
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name, end = "\t\t")
        print(self.course, end = "\t\t")
        print(self.mark)

def student_mark(s_count, s_list, c_count, c_list):
    show_c_info(c_count, c_list)
    c_name = input("Choose the 'Name' of the course to update student mark : ")
    while True:
        if not any(course.name == c_name for course in c_list):
            c_name = input("No course found, please try again : ")
        else:
            break
    s_in_c = input("How many students are there in the course : ")
    print()
    print("Course : " + c_name)
    print("Number of students in the course : " + s_in_c + " students")
    print("Choose the students in the course from the list below :")
    show_s_info(s_count, s_list)
    print()
    n = int(s_in_c)
    s_mark = []
    for i in range(n):
        course = c_name
        s_name = input("Student Name : ")
        while True:
            if not any(student.name == s_name for student in s_list):
                s_name = input("No student found, please try again : ")
            else:
                break
        name = s_name
        id = s_list[i].id
        mark = float(input("Student Mark : "))
        s_mark.append(Mark(id, name, course, mark))
    return s_mark

def show_mark(s_mark):
    print("Student Mark")
    print("ID\t\tName\t\tCourse\t\tMark")
    for i in range(len(s_mark)):
        s_mark[i].display()

try:
    while True:
        print("'A' : Update student info")
        print("'B' : Update course info")
        print("'X' : Update student marks for the course (require course and student info)")
        print("'Y' : Exit")
        answer = input("Choose your action : ")
        if answer == "A":
            print()
            s_count = student_count()
            print()
            s_list = student_info(s_count)
            print()
            show_s_info(s_count, s_list)
            print()
        elif answer == "B":
            print()
            c_count = course_count()
            print()
            c_list = course_info(c_count)
            print()
            show_c_info(c_count, c_list)
            print()
        elif answer == "X":
            print()
            s_mark = student_mark(s_count, s_list, c_count, c_list)
            print()
            show_mark(s_mark)
            print()
        elif answer == "Y":
            print("Bravo Six, we're going dark !.... ")
            break
        else:
            print()
            print("Action not recognized")
            print()
            continue
except:
    print("An error occurred !")





