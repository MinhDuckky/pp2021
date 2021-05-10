import input as inp
import output as outp

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
        s_count = inp.student_count() 
        print()
        s_list = inp.student_info(s_count)
        print()
        outp.show_s_info(s_count, s_list) 
        outp.show_s_info2(s_count, s_list) # This will write the output in 'Students Info.txt'
        print()
    elif answer == "B":
        print()
        c_count = inp.course_count()
        print()
        c_list = inp.course_info(c_count)
        print()
        outp.show_c_info(c_count, c_list)
        outp.show_c_info2(c_count, c_list) # This will write the output in 'Courses Info.txt'
        print()
    elif answer == "X":
        print()
        s_mark = inp.student_mark(s_count, s_list, c_count, c_list)
        all_mark.append(s_mark)
        inp.update(all_mark)
        print()
        outp.show_mark(s_mark)
        print()
    elif answer == "Y":
        print()
        outp.show(all_mark)
        outp.show2(all_mark) # This will write the output in 'Students Mark.txt'
        print()
        gpa_list = inp.calculate_gpa(s_count, c_count, all_mark)
        outp.show_gpa(gpa_list) # This also write the output in 'Students GPA.txt'
        print()
    elif answer == "Z":
        print("Bravo Six, we're going dark !.... ")
        break
    else:
        print()
        print("Action not recognized")
        print()
        continue
