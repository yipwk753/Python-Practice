#https://www.python-course.eu/python3_class_and_instance_attributes.php
class A:
    a = "class attribute"

x = A()
y = A()
#A, x, and y all have the same id
print("x id:", id(x.a))
print("y id:", id(y.a))
print("A id:", id(A.a))
x.a = "new instance attribute"
A.a = "Class attribute changed."
#A and y have the same id, x has a different id
print("x id:", id(x.a))
print("y id:", id(y.a))
print("A id:", id(A.a))