class Student:
    def __init__(self, name):
        self._name = name   # protected attribute
    def hello(self):
        print(self._name)  #can be used from wwithin class

s = Student("Alice")
print(s._name)   # ⚠️ Technically allowed to use from out side, but not recommended
