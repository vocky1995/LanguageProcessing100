#!/usr/bin/env python
# -*- coding: utf-8 -*-

string = "Atbash is a simple substitution cipher for the Hebrew alphabet."
def cipher(input):
    ret = ""
    for c in input:
        if c.islower():
            ret += chr(219-ord(c))
        else:
            ret += c
    return ret

if __name__ == "__main__":
    print cipher(string)



"""
参照： http://qiita.com/gamma1129/items/37bf660cf4e4b21d4267
いわゆる「アトバシュ暗号」なので，同一関数で暗号化と復号が可能．
chr() はASCIIコードから具体的な文字に変換してくれる関数（chr(97) -> 'a'）．
ord() はその逆だけど，Unicode であれば Unicode コードポイントを返してくれる．
chr() の Unicode 版が unichr()．
"""