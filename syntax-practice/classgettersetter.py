#https://www.python-course.eu/python3_properties.php
class Even():
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, num):
        if num % 2 == 0:
            self.__number = num
        else:
            self.__number = 0
n = Even(4)
print(n.number)