"""
:testcase_name method_overloading_2.py
:source https://github.com/arvimal/Python-and-OOP/blob/master/38-method-overloading-2.py
:description Reference: O'Reilly Learning Path:
http://shop.oreilly.com/product/0636920040057.do
Chapter 24 : Method Overloading - Extending and Providing
"""

import abc


class GetSetParent(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return


class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print("GetSetList object, len {0}, store history of values set".format(
            len(self.vallist)))


my_instance = GetSetList()
my_instance.set_val(100)
print(my_instance.get_val())
print(my_instance.get_vals())
print(my_instance.showdoc())
