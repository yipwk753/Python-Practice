#https://www.youtube.com/watch?v=cSSpnq362Bk (James Bennett - A Bit about Bytes: Understanding Python Bytecode - PyCon 2018)
import dis
def calculate(x, y):
    try:
        return x/y
    except Exception as e:
        #This will point out that the error happens on line 5 with the instruction BINARY_TRUE_DIVIDE
        dis.distb(e.__traceback__)
    finally:
        print("Traceback was disasembled.")
calculate(1, 0)