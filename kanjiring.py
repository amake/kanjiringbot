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
from collections import defaultdict

directions = ['top', 'right', 'bottom', 'left']

ids_pattern = re.compile(r'^(?P<idc>[\u2ff0-\u2ffb])'
                         r'(?P<parts>[^\[]+)'
                         r'(?P<flags>\[[A-Z]+\])?$')

decomp = defaultdict(list)

center_chars = defaultdict(lambda: defaultdict(set))

joyo_only = False

bmp_only = False

mobile_only = True

non_radicals_only = False

with open('vendor/cjkvi-ids/ids.txt', encoding='utf-8') as f:
    for line in f:
        if line.startswith('#'):
            continue
        fields = line.strip().split('\t')
        char = fields[1]
        idss = fields[2:]
        for ids in idss:
            m = ids_pattern.match(ids)
            if not m:
                continue
            idc, parts = [m.group(g) for g in ['idc', 'parts']]
            if idc not in u'\u2ff0\u2ff1':
                # Only support:
                # - ⿰ U+2FF0 IDEOGRAPHIC DESCRIPTION CHARACTER LEFT TO RIGHT
                # - ⿱ U+2FF1 IDEOGRAPHIC DESCRIPTION CHARACTER ABOVE TO BELOW
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
            center_chars[parts[0]
                         ]['right' if horizontal else 'bottom'].add(char)
            center_chars[parts[1]]['left' if horizontal else 'top'].add(char)
            decomp[char].append(parts)


def is_complete(ring):
    return all(d in ring for d in directions)


def random_center():
    while True:
        c = random.choice(list(center_chars.keys()))
        ring = center_chars[c]
        if is_complete(ring):
            return c


def random_ring(c):
    ring = center_chars[c]
    if not is_complete(ring):
        return None
    return [random.choice(list(ring[d])) for d in directions]


def random_decomp(center, trbl):
    return [random.choice([dec for dec in decomp[c] if center in dec])[off]
            for c, off in zip(trbl, [0, 1, 1, 0])]


def make_snippet(c, trbl, trbl_decomp):
    t, r, b, l = trbl
    ring = (u'\u3000%s\u3000\u3000\u3000\n'
            u'%s\u3000%s\u3000\u2192\n'
            u'\u3000%s\u3000\u3000\u3000') % (t, l, r, b)
    t, r, b, l = trbl_decomp
    decomp_ring = (u'\u3000%s\n'
                   u'%s%s%s\n'
                   u'\u3000%s') % (t, l, c, r, b)
    # Splice rings together
    lines = ['\u3000'.join(line)
             for line in zip(ring.split('\n'), decomp_ring.split('\n'))]
    return '\n'.join(lines)


def random_snippet():
    c = random_center()
    ring = random_ring(c)
    ring_decomp = random_decomp(c, ring)
    return make_snippet(c, ring, ring_decomp)


if __name__ == '__main__':
    print('Rings available for:')
    print(''.join(c for c, w in center_chars.items() if is_complete(w)))
    centers = sys.argv[1:]
    if not centers:
        centers = random_center()
    for c in centers:
        trbl = random_ring(c)
        if trbl is None:
            print('No ring possible for', c)
            continue
        decomp_trbl = random_decomp(c, trbl)
        print(make_snippet(c, trbl, decomp_trbl))
