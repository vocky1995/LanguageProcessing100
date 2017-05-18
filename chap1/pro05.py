#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ngram(string,n=2):
    L = []
    end = len(string)-n+1
    for i in range(end):
        L.append(string[i:i+n])
    return L

string = "I am an NLPer"
print ngram(string,2)