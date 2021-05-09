import math
import numpy as np 

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
        s_list = sorted(s_list, key = lambda x: x.id)
    return s_list

def show_s_info(s_count, s_list):
    print("Student Information")
    print("ID\t\tName\t\tDoB")
    for i in range(s_count):
        s_list[i].display()

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name, end = "\t\t")
        print(self.credit)

def course_count():
    c_count = int(input("Enter the number of courses : "))
    return c_count

def course_info(c_count):
    c_list = []
    for i in range(c_count):
        print("Course : ", i + 1)
        id = input("\tCourse ID : ")
        name = input("\tCourse Name : ")
        cre = float(input("\tCourse Credit : "))
        credit = float(math.floor(cre))
        c_list.append(Course(id, name, credit))
        c_list = sorted(c_list, key = lambda x: x.id)
    return c_list

def show_c_info(c_count, c_list):
    print("Course Information")
    print("ID\t\tName\t\tCredit")
    for i in range(c_count):
        c_list[i].display()

       
class Mark:
    def __init__(self, id, name, course, mark, course_credit):
        self.id = id
        self.name = name
        self.course = course
        self.mark = mark
        self.course_credit = course_credit
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name, end = "\t\t")
        print(self.course, end = "\t\t")
        print(self.mark, end = "\t\t")
        print(self.course_credit)

def student_mark(s_count, s_list, c_count, c_list):
    show_c_info(c_count, c_list)
    c_id = input("Choose the 'ID' of the course to update student mark : ")
    while True:
        if not any(course.id == c_id for course in c_list):
            c_id = input("No course found, please try again : ")
        else:
            break
    for i in range(len(c_list)):
            if c_list[i].id == c_id:
                c_name = c_list[i].name
                c_credit = c_list[i].credit
    print()
    print("Course : " + c_name)
    print("Update students marks from the list below :")
    show_s_info(s_count, s_list)
    print()
    s_mark = []
    for i in range(s_count):
        course = c_name
        course_credit = c_credit
        s_id = input("Student ID : ")
        while True:
            if not any(student.id == s_id for student in s_list):
                s_id = input("No student found, please try again : ")
            else:
                break
        id = s_id
        for j in range(len(s_list)):
            if s_list[j].id == s_id:
                name = s_list[j].name
        m = float(input("Student Mark : "))
        mark = float(math.floor(m))
        s_mark.append(Mark(id, name, course, mark, course_credit))
        s_mark = sorted(s_mark, key = lambda x: x.id)
    return s_mark

def show_mark(s_mark):
    print("Student Mark")
    print("ID\t\tName\t\tCourse\t\tMark\t\tCredit")
    for i in range(len(s_mark)):
        s_mark[i].display()

def update(all_mark):
    for i in range(len(all_mark)):
        for j in range(i + 1, len(all_mark)):
            if all_mark[i][0].course == all_mark[j][0].course:
                del all_mark[i]
    return all_mark

def show(all_mark):
    for i in range(len(all_mark)):
        show_mark(all_mark[i])

class Gpa:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name, end = "\t\t")
        print(self.gpa)

def calculate_gpa(s_count, c_count, all_mark):
    gpa_list = []
    for i in range(s_count):
        id = all_mark[0][i].id
        name = all_mark[0][i].name
        mark = []
        weight = []
        for j in range(c_count):
            mark.append(all_mark[j][i].mark)
            weight.append(all_mark[j][i].course_credit)
        a = np.array(mark)
        b = np.array(weight)
        gpa = np.average(a, weights = b)
        gpa_list.append(Gpa(id, name, gpa))
    gpa_list = sorted(gpa_list, key = lambda x: x.gpa, reverse = True)
    return gpa_list

def show_gpa(gpa_list):
    print("Student GPA")
    print("ID\t\tName\t\tGPA")
    for i in range(len(gpa_list)):
        gpa_list[i].display()
    
try:
    all_mark = []
    while True:
        print("'A' : Update student info")
        print("'B' : Update course info")
        print("'X' : Update student marks for the course (require course and student info)")
        print("'Y' : Show student marks of all courses and GPA")
        print("'Z' : Exit")
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
            all_mark.append(s_mark)
            update(all_mark)
            print()
            show_mark(s_mark)
            print()
        elif answer == "Y":
            print()
            show(all_mark)
            print()
            gpa_list = calculate_gpa(s_count, c_count, all_mark)
            show_gpa(gpa_list)
            print()
        elif answer == "Z":
            print("Bravo Six, we're going dark !.... ")
            break
        else:
            print()
            print("Action not recognized")
            print()
            continue
except:
    print("An error occurred !")