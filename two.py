print(sum([int(x.split()[1]) if x.split()[0] == 'down' else int(x.split()[1])*-1 for x in open("two.input", 'r') if x.split()[0] != 'forward']) * sum([int(x.split()[1]) for x in open("two.input", 'r') if x.split()[0] == 'forward']))

aim, depth = 0, 0
print(sum([0&(aim:=aim+int(y)) if x == 'down' else 0&(aim:=aim-int(y)) if x != 'forward' else 0&(depth:=depth+(aim*int(y)))|int(y) for x, y in map(lambda x: x.split(), open("two.input", 'r'))])*depth)
