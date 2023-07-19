s = input()
def toggle_Case(s):
    res = ""
    for i in range(0, len(s)):
        ascii = ord(s[i])
        if (ascii >= 65 and ascii <= 90):
               res +=  chr(ascii + 32)
        if (ascii >= 97 and ascii <= 122):
               res +=  chr(ascii - 32)
    return res
print(toggle_Case("Hello"))
print(toggle_Case("tHiSiSaStRiNg"))
print(toggle_Case("lLZ"))
print(toggle_Case(s))