import unittest

import foopkg.foofile

class TestFoopkgFoofile(unittest.TestCase):
    def test_foopkg_foofile(self):
        assert (foopkg.foofile.square(1) == 1)
        assert (foopkg.foofile.square(9) == 81)
        assert (foopkg.foofile.cube(1) == 1)
        assert (foopkg.foofile.cube(9) == 729)
