class Gpa:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name, end = "\t\t")
        print(self.gpa)