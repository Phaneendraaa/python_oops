class Student:
    def __init__(self, name):
        self.name = name  # public attribute

s = Student("Alice")
print(s.name)   # ✅ Can access directly
s.name = "Bob"  # ✅ Can modify directly
print(s.name)
