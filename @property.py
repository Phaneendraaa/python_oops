class Student:
    def __init__(self, name):
        self.__nam = name

    @property
    def name(self):  # acts like a getter
        return self.__nam

    @name.setter
    def name(self, new_name):  # acts like a setter
        if len(new_name) > 2:
            self.__nam = new_name
        else:
            print("Name too short!")


s = Student("Alice")
print(s.name)  # calls getter

s.name = "Bo"  # calls setter (Name too short!)
s.name = "Charlie"  #instead of directly accessing variable location ...uses methods
print(s.name)  # Charlie
