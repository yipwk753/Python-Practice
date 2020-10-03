#https://icodemag.com/understanding-python-dunder-magic-methods/
#https://medium.com/python-features/magic-methods-demystified-3c9e93144bf7
class Dunder(object):
    def __new__(cls, x, y, l):
        print("New")
        #If both return statements are commented out, None is returned and the program breaks
        return super(Dunder, cls).__new__(cls)
        # return object.__new__(cls)

    def __init__(self, x, y, l):
        print("Init")
        print(self.a)
        self.x = x
        self.y = y
        self.l = l

    def __str__(self):
        return f"Dunder({self.x}, {self.y}, {self.l})"

    #if __str__ is not defined, this will run
    def __repr__(self):
        return f"Dunder: {self.x}, {self.y}, {self.l}"

    def __len__(self):
        return len(self.l)

    def __call__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l

    def __getitem__(self, index):
        if len(self.l) == 0:
            return 0
        return self.l[index]

    def __setitem__(self, index, value):
        if len(self.l) <= index:
            print("Index out of range")
        else:
            self.l[index] = value

dunder = Dunder(1, 2, [])
print(dunder)
print(len(dunder))
print(dunder[0])
dunder(9, 9, [1,2,3])
print(dunder)
print(len(dunder))
print(dunder[0])
dunder[3] = 1
dunder[2] = 999
print(dunder)