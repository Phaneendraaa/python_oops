class Student:
    def __init__(self, name):
        self.__name = name  # private attribute


s = Student("Alice")
# print(s.__name)   # ❌ AttributeError
print(s._Student__name)  # ✅ Access using name mangling
