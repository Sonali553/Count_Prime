s = "aabbcd"
d = {}
for e in s:
    if e not in d:
        d[e] = 1
    else:
        d[e] += 1
lst = []
print(len(d))
for ele in d.keys():
    if d[ele] == 1:
        lst.append(ele)
print(lst)
a = "".join(lst)
print(a)

