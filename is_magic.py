s = int(input())
def Is_Magic(s):
    while(len(str(s)) > 1):
        Sum_val = 0
        for ele in str(s):
             Sum_val += int(ele)
        s = Sum_val
    return 1 if s == 1 else 0
print(Is_Magic(s))
print(Is_Magic(1291))
