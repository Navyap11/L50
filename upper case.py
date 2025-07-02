class IOString():

    def __init__(self):
        self.str1= " "


    def get_(self):
        self.str1 = input("Enter String: ")

    def print_String(self):
        self.str1= print("Result is: ", self.str1.upper())


str1= IOString()

str1.get_()
str1.print_String()