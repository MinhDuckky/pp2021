class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name, end = "\t\t")
        print(self.credit)

    def display2(self):
        outF = open("Courses Info.txt", "a")
        outF.write(str(self.id))
        outF.write("\t\t")
        outF.write(str(self.name))
        outF.write("\t\t")
        outF.write(str(self.credit))
        outF.write("\n")
