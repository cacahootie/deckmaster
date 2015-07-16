"""Test Jinja2 Git Template Loader"""

import unittest
import sys
import os

sys.path.append('../..')
from deckmaster.app import GitLoader


class TestGitLoader(unittest.TestCase):

    templdir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'templates'
    )

    def test_load(self):
        print GitLoader().get_source(None, os.path.join(self.templdir, 'test.txt'))


if __name__ == '__main__':
    unittest.main()