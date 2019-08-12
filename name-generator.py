import random
import sys

def load(s):
    for i in range(len(s) - order):
        try:
            table[s[i:i + order]]
        except KeyError:
            table[s[i:i + order]] = []
        table[s[i:i + order]] += s[i + order]

def generate(start = None, max_length = 20):
    if start == None:
        s = random.choice(list(table.keys()))
    else:
        s = start
    try:
        while len(s) < max_length:
            s += random.choice(table[s[-order:]])
    except KeyError:
        pass
    return s

table = {}
order = int(sys.argv[1])
amount = int(sys.argv[2])
namelist = sys.argv[3]
dwarf_name2_1 = [word.strip() for word in open('dwarf-name2-1', 'r', encoding='utf8').readlines()]
dwarf_name2_2 = [word.strip() for word in open('dwarf-name2-2', 'r', encoding='utf8').readlines()]
orc_name2_1 = [word.strip() for word in open('orc-name2-1', 'r', encoding='utf8').readlines()]
orc_name2_2 = [word.strip() for word in open('orc-name2-2', 'r', encoding='utf8').readlines()]
orc_name3 = [word.strip() for word in open('orc-name3', 'r', encoding='utf8').readlines()]

for line in open(namelist, 'r', encoding='utf8').readlines():
    load(line.strip().lower())

for i in range(amount):
    name = generate(start=None, max_length = random.randint (5, 9))
    name = name[0].upper() + name[1:]
    if namelist == 'dwarf':
        part1 = random.choice(dwarf_name2_1)
        part1 = part1[0].upper() + part1[1:]
        part2 = random.choice(dwarf_name2_2)
        name += ' %s%s' % (part1, part2)
    elif namelist == 'orc':
        name += ' the '
        if random.random() > 0.7:
            part1 = random.choice(orc_name2_1)
            part1 = part1[0].upper() + part1[1:]
            part2 = random.choice(orc_name2_2)
            name += ' %s%s' % (part1, part2)
        else:
            part1 = random.choice(orc_name3)
            name += part1
    print (name)