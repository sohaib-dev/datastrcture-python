from collections import Counter, defaultdict, ChainMap

a = (1,2,3,1,2,4)
a = [1,2,3,1,2,4]
a = {1,2,3,4,5,1,2,3}
a = {'a':2, 'b':2, 'b':1}
a = 'abccd'
c = Counter(a)
print(c, type(c))
print(c.pop('a'))
print(c.values())
print(c.items())
print(c.keys())
print(sorted(c.elements()))
print(c.most_common())
print(c.clear())
print(c, type(c))

di = defaultdict(lambda : 'Not Present')
di['a'] = 1
print(di['b'])

cm = ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'a': 5})
print(cm)
print(list(cm.values()))
print(list(cm.keys()))
print(cm.maps)
# print(cm.fromkeys())
# print(cm.pop())
print(cm['c'])
cd = cm.new_child({'a': 6})
print(cd['a'])
print(cd.parents)


for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = ChainMap(for_adoption, vet_treatment)
print(pets.pop('dogs'))
for key, value in pets.items():
    print(key, "->", value)

pets1 = {}
pets1.update(for_adoption)
print(pets1)
pets1.update(vet_treatment if vet_treatment.keys() in ['turtles'] else {'a':1})
print(pets1)
