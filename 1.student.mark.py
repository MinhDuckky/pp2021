def student_count():
    s_count = int(input("Enter the number of students : "))
    return s_count

def student_info(s_count):
    s_info = []
    for i in range(s_count):
        s_dict = {}
        s_dict["id"] = input("Student ID : ")
        s_dict["name"] = input("Student Name : ")
        s_dict["DoB"] = input("Student Date of Birth (DD/MM/YYYY) : ")
        s_copy = s_dict.copy()
        s_info.append(s_copy)
    return s_info 

def course_count():
    c_count = int(input("Enter the number of courses : "))
    return c_count

def course_info(c_count):
    c_info = []
    for i in range(c_count):
        c_dict = {}
        c_dict["id"] = input("Course ID : ")
        c_dict["name"] = input("Course Name : ")
        c_copy = c_dict.copy()
        c_info.append(c_copy)
    return c_info

def show(list):
    for i in range(len(list)):
        print(list[i])

def student_mark(c_info, s_info):
    show(c_info)
    c_name = input("Choose the 'name' of the course to update student mark : ")
    while True:
        if not any(dict["name"] == c_name for dict in c_info):
            c_name = input("No course found, please try again : ")
        else:
            break
    s_in_c = input("How many students are there in the course : ")
    print()
    print("Course : " + c_name)
    print("Number of students in the course : " + s_in_c + " students")
    print("Choose the students in the course from the list below :")
    show(s_info)
    print()
    n = int(s_in_c)
    s_mark = []
    for i in range(n):
        m_dict = {}
        m_dict["course"] = c_name
        s_name = input("Student Name : ")
        while True:
            if not any(dict["name"] == s_name for dict in s_info):
                s_name = input("No student found, please try again : ")
            else:
                break
        m_dict["student"] = s_name
        m_dict["mark"] = float(input("Student Mark : "))
        m_copy = m_dict.copy()
        s_mark.append(m_copy)
    return s_mark

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
        s_info = student_info(s_count)
        print()
        show(s_info)
        print()
    elif answer == "B":
        print()
        c_count = course_count()
        print()
        c_info = course_info(c_count)
        print()
        show(c_info)
        print()
    elif answer == "X":
        print()
        s_mark = student_mark(c_info, s_info)
        print()
        show(s_mark)
        print()
    elif answer == "Y":
        print("Bravo Six, we're going dark !.... ")
        break
    else:
        print("Action not recognized")
        print()
        continue

















        




