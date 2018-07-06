a = {"a": 1, "b": 2, "c": 3}
b = ["a", "c"]

c = [a[x] for x in a]

d = list(a)
del a["a"]
print(list(d)) 