from collections import OrderedDict
d = OrderedDict()
d['foo'] , d['bar'], d['spam'], d['grok']= 1, 2, 3, 4
for key in d:
    print(key, d[key])

# foo 1
# bar 2
# spam 3
# grok 4
