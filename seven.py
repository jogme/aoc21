from statistics import median
from math import ceil
from math import floor
import statistics

inp = list(map(int, open("seven.example", 'r').read()[:-1].split(',')))
m, me = median(inp), statistics.mean(inp)
o0 = int(sum([(int(ceil(abs(x-me)))*(int(ceil(abs(x-me)))+1))/2 for x in inp]))
o1 = int(sum([(int(floor(abs(x-me)))*(int(floor(abs(x-me)))+1))/2 for x in inp])) 
print(o0, o1)
print(int(sum([abs(x-m) for x in inp])), int(sum([(int(round(abs(x-me)))*(int(round(abs(x-me)))+1))/2 for x in inp])))
