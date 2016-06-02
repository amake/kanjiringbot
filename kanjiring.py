# -*- coding: utf-8 -*-

'''
Generate randomize rings of kanji with a shared component a la the classic
吾、唯、足るを知る:

　五
矢口隹
　止

Requires cjk-decomp data from
https://cjkdecomp.codeplex.com/wikipage?title=cjk-decomp
to be present in the CWD.
'''

from __future__ import print_function
import sys
import random
import re
import cjkinfo
from codecs import open
from collections import defaultdict

directions = ['top', 'right', 'bottom', 'left']

format = re.compile(r'^(?P<char>[^:]+):(?P<dtype>[^\(]+)'
                    r'\((?P<dchars>[^\)]*)\)\s*$')

decomp = {}

center_chars = defaultdict(lambda: defaultdict(set))

joyo_only = False

bmp_only = False

mobile_only = True

non_radicals_only = True

with open('cjk-decomp/cjk-decomp.txt', encoding='utf-8') as f:
    for line in f:
        m = format.match(line)
        char, dtype, dchars = [m.group(field)
                               for field in ['char', 'dtype', 'dchars']]
        dchars = dchars.split(',')
        if dtype not in ['a', 'ra', 'd', 'rd']:
            # Ignore entries with decomposition type other than
            # 'across', 'down', 'repeated across', or 'repeated down'
            continue
        if dtype in ['a', 'd'] and len(dchars) != 2:
            # Ignore a, d entries with more than two components
            continue
        if any(len(c) == 5 for c in dchars + [char]):
            # Ignore entries with intermediate components
            continue
        if bmp_only and any(ord(c) > 0xffff for c in dchars + [char]):
            continue
        if joyo_only and any(c not in cjkinfo.joyo for c in dchars + [char]):
            continue
        if mobile_only and any(not cjkinfo.mobile_ok.match(c)
                               for c in dchars + [char]):
            continue
        if non_radicals_only and any(c in cjkinfo.radicals
                                     for c in dchars + [char]):
            continue
        if dtype in ['ra', 'rd']:
            dchars += dchars
        horizontal = dtype in ['a', 'ra']
        center_chars[dchars[0]]['right' if horizontal else 'bottom'].add(char)
        center_chars[dchars[-1]]['left' if horizontal else 'top'].add(char)
        decomp[char] = dchars


def is_complete(ring):
    return all(d in ring for d in directions)

def random_center():
    while True:
        c = random.choice(center_chars.keys())
        ring = center_chars[c]
        if is_complete(ring):
            return c

def random_ring(c):
    ring = center_chars[c]
    if not is_complete(ring):
        return None
    return [random.choice(list(ring[d])) for d in directions]

def make_ring_text(center, trbl):
    t, r, b, l = [decomp[c][off] for c, off in zip(trbl, [0, 1, 1, 0])]
    return u'\u3000%s\n%s%s%s\n\u3000%s' % (t, l, center, r, b)

def make_snippet(c, trbl):
    return u'%s\n\n%s' % (' + '.join(trbl), make_ring_text(c, trbl))

def random_snippet():
    c = random_center()
    return make_snippet(c, random_ring(c))


if __name__ == '__main__':
    print('Rings available for:')
    print(''.join(c for c, w in center_chars.iteritems() if is_complete(w)))
    centers = [arg.decode('utf-8') for arg in sys.argv[1:]]
    if not centers:
        centers = random_center()
    for c in centers:
        trbl = random_ring(c)
        if trbl is None:
            print('No ring possible for', c)
            continue
        print(make_snippet(c, trbl))
