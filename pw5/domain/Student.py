class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name, end = "\t\t")
        print(self.DoB)

    def display2(self):
        outF = open("Students Info.txt", "a")
        outF.write(self.id)
        outF.write("\t\t")
        outF.write(self.name)
        outF.write("\t\t")
        outF.write(self.DoB)
        outF.write("\n")