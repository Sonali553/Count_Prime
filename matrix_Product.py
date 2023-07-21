def Matrix_Product(lst, ele):
    res = []
    for l in lst:
        l = [ele * e for e in l]
        res.append(l)
    return res
print(Matrix_Product([[1,2,3], [4,5,6]], 3))