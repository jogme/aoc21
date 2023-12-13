print([o * int(''.join([str(0b1&~(0^int(s))) for s in '{0:012b}'.format(o)]), 2) for o in [int(''.join(['1' if y1 > y0 else '0' for y1, y0 in [(sum([int(x[i]) for x in open("three.input", 'r')]), sum([int(not int(x[i])) for x in open("three.input", 'r')])) for i in range(12)]]), 2)]][0])

#import re
#skipping oneliner thing
#print([pattern+","+s[:-1]+","+str(pat_i) for pat_i, pattern in enumerate([''.join(['1' if y1 > y0 else '0' for y1, y0 in [(sum([int(x[i]) for x in open("three.input", 'r')]), sum([int(not int(x[i])) for x in open("three.input", 'r')])) for i in range(12)]])] *12) for s in open("three.input", 'r') if (pattern[:-pat_i] is not [] and pat_i != 0) and (re.match(pattern[:-pat_i], s[:-1]) is not None)])# or re.match(''.join([str(0b1&~(0^int(rev))) for rev in '{0:012b}'.format(int(pattern, 2))]), s) is not None])

from copy import deepcopy

lines = [x for x in open("three.input", 'r')]
oxygen_generator_r = deepcopy(lines)
co2_scrubber_r = deepcopy(lines)
for i in range(12):
    if len(oxygen_generator_r) > 1:
        bit = (sum([int(x[i]) for x in oxygen_generator_r]), sum([int(not int(x[i])) for x in oxygen_generator_r]))
        most_common = '1' if bit[0] >= bit[1] else '0'
        oxygen_generator_r = [x for x in oxygen_generator_r if x[i] == most_common]
    if len(co2_scrubber_r) > 1:
        bit = (sum([int(x[i]) for x in co2_scrubber_r]), sum([int(not int(x[i])) for x in co2_scrubber_r]))
        most_common = '1' if bit[0] >= bit[1] else '0'
        co2_scrubber_r = [x for x in co2_scrubber_r if x[i] != most_common]
print(int(oxygen_generator_r[0][:-1],2) * int(co2_scrubber_r[0][:-1],2))
