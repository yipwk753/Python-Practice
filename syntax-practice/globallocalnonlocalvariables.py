def func():
    # if global a is uncommented, innerfunc will have to declare its own local a variable
    # global a
    a = 1
    print(a)
    def innerfunc():
        nonlocal a
        a *= 2
        print("inside innerfunc")
        print(a)
        def innerinnerfunc():
            nonlocal a
            a *=3
            print("inside innerinnerfunc")
            print(a)
        print("calling innerinnerfunc")
        innerinnerfunc()
    print("calling innerfunc")
    innerfunc()
a = 100
print("calling func")
func()
print(f"global a: {a}")