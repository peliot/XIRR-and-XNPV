XNPV and XIRR
==============

This module contains python implementations of Microsoft Excel's XNPV and XIRR functions. Please see the docstrings for more info. I will just highlight here one note: the XIRR function uses the numerical solver from the scipy.optimize module. If, however, you do not have scipy installed, this module also contains a quick and dirty implementation of the secant method that works the same as the scipy function when there is an answer but does not fail gracefully when no answer is found. The version of XIRR using the locally defined secant_method is commented out, uncomment to use it.

