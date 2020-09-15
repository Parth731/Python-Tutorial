
'''
special variable __name__
special method __init__

__main__ is starting point of execution

when calc is used as module to the other program so print to the module
name
'''


from cal import *

# __name__ == "__main__"
# first module is always main

print("demo says : " + __name__)

def main():
    print("Hello")
    print("Welcome User")

if __name__ == "__main__":
    main()