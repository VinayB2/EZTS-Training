class Student:
    def __init__(self):
        self.__Name = None
        self.__USN = None
        self.__Marks = []
        self.__Percentage = None
        self.__Grade = None
        self.take_input()
    def take_input(self):
        self.__Name = input("Enter Name: ")
        self.__USN = input("USN: ")
        for i in range(5):
            marks = int(input("Enter marks of a subject: "))
            self.__Marks.append(marks)
    def get_percentage(self):
        self.__Percentage = ( sum(self.__Marks) / len(self.__Marks) / 100 ) * 100
        return self.__Percentage
    def get_grade(self):
        percnt = self.get_percentage()
        if(percnt < 35):
            self.__Grade = "C"
        elif(percnt >=35 and percnt < 75):
            self.__Grade = "B"
        else:
            self.__Grade = "A"
        return self.__Grade
    def display_details(self):
        print("Name: ", self.__Name)
        print("USN", self.__USN)
        print("Marks: ", self.__Marks)
        print("Percentage: ", self.get_percentage())
        print("Grade: ", self.get_grade())
    def make_list(self):
        lst = f"{[self.__Name, self.__USN, self.__Marks, self.get_percentage(), self.get_grade()]}"
        return lst
    def add_to_file(self):
        lst = self.make_list().encode()
        with open("student.bin", "wb") as file:
            file.write(lst)