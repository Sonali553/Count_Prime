num = int(input())
b = int(input())
def anyBase_ToDecimal(num, b):
        res = 0
        i = 0
        while num > 0:
             r = num % 10
             res += ( r * (b ** (i)))
             i += 1
             num = num // 10
             
        return res
print(anyBase_ToDecimal(22, 3))
print(anyBase_ToDecimal(1010, 2))
print(anyBase_ToDecimal(num, b))