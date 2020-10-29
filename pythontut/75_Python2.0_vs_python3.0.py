
'''

google search:
python 2 code to python 3


'''

'''
python2.0

print 'Hello world!'

exec code
exec code in globals
exec code in (globals, locals)

/ and //:
5 / 2 = 2

raise:
1. raise Exception, args
2. raise Exception, args, traceback
3. raise "Error"

except:
except Exception, variable:

def:
def function(arg1, (x, y)):

expr
x = `355/113`

String Formatting:
1. "%d %s" % (i, s)
2. "%d/%d=%f" % (355, 113, 355/113)

class:
1. class MyClass(object):
    pass
    
2. class MyClass:
        __metaclass__ = MyMeta
    class MyClass(MyBase):
        __metaclass__ = MyMeta 
'''

'''
python 3.0

print("Hello world!")

exec(code)
exec(code, globals)
exec(code, globals, locals)

/ and //:
5 / 2 = 2.5
5 // 2 = 2

raise:
1. raise Exception
   raise Exception(args)
2. raise Exception(args).with_traceback(traceback)
3. raise Exception("Error")


except:
1. except AnException as variable:
2. except (OneException, TwoException) as variable:

def:
def function(arg1, x_y): x, y = x_y

expr:
x = repr(355/113):

String Formatting:
1. "{} {}".format(i, s)
2. "{:d}/{:d}={:f}".format(355, 113, 355/113)

class:
1. class MyClass:
    pass

2.  class MyClass(metaclass=type):
        pass
    class MyClass(MyBase, metaclass=MyMeta):
        pass
    
'''

import timeit

# n = 10000
# def test_range(n):
    # return for i in range(n):
    #     pass

# def test_xrange(n):
    # for i in xrange(n):
    #     pass