#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):

	floatLen = len(s)-(s.index('.')+1)
	s=s[:floatLen]+s[floatLen+1:]

	def fn(x, y):
		return x * 10 + y

	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

	return reduce(fn, map(char2num, s))/10**floatLen


print('str2float(\'123.456\') =', str2float('123.456'))