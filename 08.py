# 8. Write a Python script to merge two Python dictionaries.


#####Python 3.5 ######

# def merge_two_dicts(x,y):
#    z = {**x, **y}
#    return z
#z = merge_two_dicts({1:2},{3:4})


d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)
