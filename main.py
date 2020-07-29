#!/usr/bin/env python

import foopkg.foofile

for n in range(1, 11):
    print("%4d %4d %4d" % (n, foopkg.foofile.square(n),  foopkg.foofile.cube(n)))
