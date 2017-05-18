#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pro05 import ngram

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngram(str1))
Y = set(ngram(str2))

print X
print Y

print X.union(Y)#和集合
print X.intersection(Y)#積集合
print X.difference(Y)#差集合

print "se" in X
print "se" in Y

