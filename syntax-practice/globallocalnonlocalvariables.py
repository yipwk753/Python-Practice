#https://www.python-course.eu/python3_global_vs_local_variables.php
def func():
    # if global a is uncommented, innerfunc will have to declare its own local a variable
    # global a
    a = 1
    print(a)
    print("func locals:", locals())
    def innerfunc():
        nonlocal a
        a *= 2
        print("inside innerfunc")
        print(a)
        print("innerfunc locals:", locals())
        def innerinnerfunc():
            nonlocal a
            a *=3
            print("inside innerinnerfunc")
            print(a)
            print("innerinnerfunc locals:", locals())
        print("calling innerinnerfunc")
        innerinnerfunc()
    print("calling innerfunc")
    innerfunc()
a = 100
print("calling func")
func()
print(f"global a: {a}")
print(globals())