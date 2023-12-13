coordinates = [list(map(int, coord.split(','))) for line in open("five.input", 'r') for coord in line[:-1].split(' -> ')]

coord = dict()

def generate_nums(p0,p1):
    if p0[0] == p1[0] and p0[1] == p1[1]:
            key = (p0[0], p0[1])
            coord[key] = coord[key]+1 if key in coord else 1
    elif p0[0] == p1[0]:
        r = range(p0[1], p1[1]+1) if p0[1] < p1[1] else range(p1[1], p0[1]+1)
        for y0 in r:
            key = (p0[0], y0)
            coord[key] = coord[key]+1 if key in coord else 1
    elif p0[1] == p1[1]:
        r = range(p0[0], p1[0]+1) if p0[0] < p1[0] else range(p1[0], p0[0]+1)
        for x0 in r:
            key = (x0, p0[1])
            coord[key] = coord[key]+1 if key in coord else 1

for ci, c in enumerate(coordinates[::2]):
    generate_nums(c, coordinates[ci*2+1])
print(len([val for val in coord.values() if val > 1]))

coord_b = dict()

def generate_nums_b(p0,p1):
    if not(p0[0] == p1[0] or p0[1] == p1[1]):
        rx = 1 if p0[0] < p1[0] else -1
        ry = 1 if p0[1] < p1[1] else -1
        r = range(((p1[0]-p0[0])*rx)+1)
        for d in r:
            key = (p0[0]+d*rx, p0[1]+d*ry)
            coord[key] = coord[key]+1 if key in coord else 1


for ci, c in enumerate(coordinates[::2]):
    generate_nums_b(c, coordinates[ci*2+1])
print(len([val for val in coord.values() if val > 1]))
