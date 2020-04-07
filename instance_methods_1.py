"""
:testcase_name instance_methods_1.py
:source https://github.com/arvimal/Python-and-OOP/blob/master/17-instance_methods-1.py
:description Instance methods are also known as Bound methods since the methods
within a class are bound to the instance created from the class, via
'self'.
"""


class A(object):
    def method(*argv):
        return argv


a = A()
print(a.method)

# The print() function will print the following :
#  python 17-instance_methods-1.py
# <bound method A.method of <__main__.A object at 0x7fc91d83e790>>

# The output shows that 'method' is a bound method
