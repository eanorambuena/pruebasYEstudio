import lists as l

a = l.List()
a.append(78)
a.append(56)
[print(i) for i in a]
a.reverse()
print(a[1])