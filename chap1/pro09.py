#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def convert(word):
    t = word[1:-1]
    tmp = "".join(random.sample([_ for _ in word[1:-1]],len(word)-2))
    return word[0]+tmp+word[-1]

if __name__ == "__main__":
    res = []
    for w in string.split(" "):
        if len(w)<4:
            res.append(w)
        else:
            res.append(convert(w))
    print " ".join(res)