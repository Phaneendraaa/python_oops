class car:
    c =54   #This is a class variable..Same for all objs of this class
    def __init__(self):
        hello=0

    def change(self):
        hello=1
        self.c = 55  #class variables can be changed using self(changes for particular obj)....also declaring with self is only in methods
c1 = car()
print(c1.c)
