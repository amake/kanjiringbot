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

ids_pattern = re.compile(ur'^(?P<idc>[\u2ff0-\u2ffb])'
                         ur'(?P<parts>[^\[\s]+)'
                         ur'(?P<flags>\[[A-Z]+\])?$')

decomp = defaultdict(list)

center_chars = defaultdict(lambda: defaultdict(set))

joyo_only = False

bmp_only = False

mobile_only = True

non_radicals_only = False

with open('cjkvi-ids/ids.txt', encoding='utf-8') as f:
    for line in f:
        if line.startswith('#'):
            continue
        fields = line.split('\t')
        char = fields[1]
        idss = fields[2:]
        for ids in idss:
            m = ids_pattern.match(ids)
            if not m:
                continue
            idc, parts = [m.group(g) for g in ['idc', 'parts']]
            if idc not in u'\u2ff0\u2ff1':
                # Only support LEFT TO RIGHT and ABOVE TO BELOW
                continue
            if len(parts) > 2:
                # Only support simple 2-part compositions
                continue
            if any(c >= u'\u2460' and c <= u'\u2473' for c in char + parts):
                # Don't support unencoded DCs
                continue
            if bmp_only and any(ord(c) > 0xffff for c in char + parts):
                continue
            if joyo_only and any(c not in cjkinfo.joyo for c in char + parts):
                continue
            if mobile_only and any(not cjkinfo.mobile_ok.match(c)
                                   for c in char + parts):
                continue
            if non_radicals_only and any(c in cjkinfo.radicals
                                         for c in char + parts):
                continue
            horizontal = idc == u'\u2ff0'
            center_chars[parts[0]]['right' if horizontal else 'bottom'].add(char)
            center_chars[parts[1]]['left' if horizontal else 'top'].add(char)
            decomp[char].append(parts)


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
    t, r, b, l = [random.choice(decomp[c])[off] for c, off in zip(trbl, [0, 1, 1, 0])]
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
