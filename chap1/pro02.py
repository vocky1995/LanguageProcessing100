#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

string1 = u"パトカー"
string2 = u"タクシー"

for s1,s2 in zip(string1,string2):
    sys.stdout.write(s1+s2)
print 