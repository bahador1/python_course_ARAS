import module2
#The import statement creates a new namespace (or environment) and executes
#all the statements in the associated .py file within that namespace.

print(__name__)
# The __name__ is a special variable in Python.
# Python assigns a different 
# value to it depending on how its containing script executes
def func1():
    print("func1")
def func2():
    print("func2")
def func3():
    print("func3")

if __name__ == "__main__" :
    func1()
    func2()
    raise SystemExit("something is wrong")
    func3()
