lines = list(map(int, open("one.input", 'r').readlines()))
print(list(map(lambda x, y: 1 if y>x else 0, lines[:-1], lines[1:])).count(1))

print([1 if int(y)>int(x) else 0 for x, y in zip(open("one.input", 'r').readlines()[:-1], open("one.input", 'r').readlines()[1:])].count(1))

b = [x+lines[i+1]+lines[i+2] for i,x in enumerate(lines[:-2])]
print([1 if y > x else 0 for x, y in zip(b[:-1], b[1:])].count(1))
