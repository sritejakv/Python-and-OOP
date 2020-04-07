"""
:testcase_name encapsulation_2.py
:source https://github.com/arvimal/Python-and-OOP/blob/master/02-encapsulation-2.py
:description This example builds on top of `encapsulation_1.py`.
Here we see how we can set values in methods without
going through the method itself, ie.. how we can break
encapsulation.

NOTE: BREAKING ENCAPSULATION IS BAD.
"""

class MyClass(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)


a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(1000)
a.value = 100    # <== Overriding `set_value` directly
# <== ie..  Breaking encapsulation

a.get_val()
b.get_val()
