from aimacode.utils import (removeall, unique, first, isnumber, issequence, Expr, expr, subexpressions)
from aimacode.logic import *


if __name__ == '__main__':
	expression = Expr('f', 'x', 1, 'y')
	print (expression.__repr__())
	print (associate('&', dissociate('&', [x, y, z])))
	list = [1, 3, 5]
	list.remove(3)
	print (list)