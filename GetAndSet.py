class Student:
    def __init__(self, name):
        self.__name = name  # private attribute

    # Getter
    def get_name(self):
        return self.__name

    # Setter
    def set_name(self, new_name):
        if len(new_name) > 2:
            self.__name = new_name
        else:
            print("Name too short!")


s = Student("Alice")
print(s.get_name())  # Alice
s.set_name("Bo")  # Name too short!
s.set_name("Bob")
print(s.get_name())  # Bob
