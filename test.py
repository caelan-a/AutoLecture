a = {"a": 1, "b": 2, "c": 3}
d = a.copy()
del a["a"]
print(list(d)) 