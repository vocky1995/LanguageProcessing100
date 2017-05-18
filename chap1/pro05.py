#!/usr/bin/env python
# -*- coding: utf-8 -*-
def ngram(input,n=2):
    L = []
    end = len(input)-n+1
    for i in range(end):
        L.append(input[i:i+n])
    return L

if __name__ == "__main__":
    string = "I am an NLPer"
    print ngram(string,2)