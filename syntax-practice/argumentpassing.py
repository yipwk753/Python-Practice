#https://www.python-course.eu/python3_passing_arguments.php
def a(l = []):
    #If l.append(1) is commented out, l always equals [] and x and z are unchanged
  l.append(1)
    #If l.append(1) and l = [] both run, l equals [] but both x and z are changed
#   l = []
  print(f"Id of l is: {id(l)}")
  print("l: ", l)
  print("locals:", locals())

x = [1,2,3]
print(f"Id of x is: {id(x)}")
z = [4,5,6]
a(z)
a(x)
a(z)
a(x)
print("x:", x)
print(f"Id of z is: {id(z)}")
print("z:", z)