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
    
    def display2(self):
        outF = open("Students Mark.txt", "a")
        outF.write(self.id)
        outF.write("\t\t")
        outF.write(self.name)
        outF.write("\t\t")
        outF.write(self.course)
        outF.write("\t\t")
        outF.write(str(self.mark))
        outF.write("\t\t")
        outF.write(str(self.course_credit))
        outF.write("\n")