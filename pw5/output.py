def show_s_info(s_count, s_list):
    print("Student Information")
    print("ID\t\tName\t\tDoB")
    for i in range(s_count):
        s_list[i].display()

def show_s_info2(s_count, s_list):
    outF = open("Students Info.txt", "w")
    outF.write("Student Information")
    outF.write("\n")
    outF.write("ID\t\tName\t\tDoB")
    outF.write("\n")
    outF = open("Students Info.txt", "a")
    for i in range(s_count):
        s_list[i].display2()
    outF.close()

def show_c_info(c_count, c_list):
    print("Course Information")
    print("ID\t\tName\t\tCredit")
    for i in range(c_count):
        c_list[i].display()

def show_c_info2(c_count, c_list):
    outF = open("Courses Info.txt", "w")
    outF.write("Course Information")
    outF.write("\n")
    outF.write("ID\t\tName\t\tCredit")
    outF.write("\n")
    outF = open("Courses Info.txt", "a")
    for i in range(c_count):
        c_list[i].display2()
    outF.close()

def show_mark(s_mark):
    print("Student Mark")
    print("ID\t\tName\t\tCourse\t\tMark\t\tCredit")
    for i in range(len(s_mark)):
        s_mark[i].display()

def show(all_mark):
    for i in range(len(all_mark)):
        show_mark(all_mark[i])

def show_gpa(gpa_list):
    outF = open("Students GPA.txt", "w")
    print("Student GPA")
    print("ID\t\tName\t\tGPA")
    outF.write("Student GPA")
    outF.write("\n")
    outF.write("ID\t\tName\t\tGPA")
    outF.write("\n")
    outF = open("Students GPA.txt", "a")
    for i in range(len(gpa_list)):
        gpa_list[i].display()
    outF.close()

def show_mark2(s_mark):
    outF = open("Students Mark.txt", "a")
    outF.write("Student Mark")
    outF.write("\n")
    outF.write("ID\t\tName\t\tCourse\t\tMark\t\tCredit")
    outF.write("\n")
    for i in range(len(s_mark)):
        s_mark[i].display2()

def show2(all_mark):
    outF = open("Students Mark.txt", "w")
    outF = open("Students Mark.txt", "a")
    for i in range(len(all_mark)):
        show_mark2(all_mark[i])
    outF.close()