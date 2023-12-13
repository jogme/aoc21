def check_board(b):
    for r in b:
        if sum(r) == -5:
            return 1
    for c in [[r[y] for r in b] for y in range(5)]:
        if sum(c) == -5:
            return 1

with open("four.input", 'r') as file:
    numbers = list(map(int, file.readline()[:-1].split(',')))
    boards = [[list(map(int, z.split())) for z in y] for y in [x.split('\n') for x in file.read()[1:-1].split('\n\n')]]

last = []

for n in numbers:
    for bi, b in enumerate(boards):
        for ri, row in enumerate(b):
            for ci, col in enumerate(row):
                if n == col:
                    boards[bi][ri][ci] = -1
        if bi not in last and check_board(b):
            last.append(bi)
            if len(last) == 1 or len(last) == len(boards):
                print(sum([c for r in b for c in r if c > 0])*n)
