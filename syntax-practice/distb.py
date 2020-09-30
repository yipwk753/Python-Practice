import dis
def calculate(x, y):
    try:
        return x/y
    except Exception as e:
        dis.distb(e.__traceback__)
    finally:
        print("Traceback was disasembled.")
calculate(1, 0)