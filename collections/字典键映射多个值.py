from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)
d['b'].append(1)
print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['a'].add(4)
e['b'].add(1)
print(e['a'])
