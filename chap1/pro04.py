#!/usr/bin/env python
# -*- coding: utf-8 -*-

string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = string.split(" ")
dic = {}
for i,w in enumerate(word_list,start=1):
    if i in [1,5,6,7,8,9,15,16,19]:
        dic[w[:1]] = i
    else:
        dic[w[:2]] = i
        
print dic