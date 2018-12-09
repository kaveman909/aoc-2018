import re
import string

polymer_origin = open("day-5.txt").readline()

# regex: find any two of the same letter, ignoring case
pair = re.compile(r'(.)\1', flags=re.I)
polymers = list()

for unit in '0' + string.ascii_lowercase:
    unit_regex = re.compile(unit, flags=re.I)
    # replace all of one letter (ignorning case) before beginning reduction
    polymer = unit_regex.sub('', polymer_origin)
    m_end = 0
    m_end_last = 0
    while m_end == 0 or m_end != m_end_last:
        m_end_last = m_end
        match = pair.search(polymer, pos=m_end)
        try:
            m_group = match.group()
            m_end = match.end()
        except:
            break

        if m_group[0] != m_group[1]:
            polymer = polymer.replace(m_group, '', 1)
            m_end = 0
    if unit == '0':
        print('Part 1: {}'.format(len(polymer)))
    polymers.append(len(polymer))
print('Part 2: {}'.format(min(polymers)))
