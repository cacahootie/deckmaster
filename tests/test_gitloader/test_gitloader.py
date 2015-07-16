"""Test Jinja2 Git Template Loader"""

import unittest
import sys
import os

sys.path.append('../..')
import deckmaster
from deckmaster.app import GitLoader

app = deckmaster.app.get_instance()

class TestGitLoader(unittest.TestCase):

    templdir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'templates'
    )

    def test_file_load(self):
        """Can the loader get a simple, local file?"""
        with app.test_request_context('/test.txt'):
            src, templ, reload = GitLoader().get_source(
                None, os.path.join(self.templdir, 'test.txt')
            )
            self.assertEqual(src, '{{ burgers }}\n{{ fries }}\n')

    def test_git_load(self):
        """Can the loader get a template at a specific revision?"""
        with app.test_request_context('/test.txt@c89d6c7'):
            src, templ, reload = GitLoader().get_source(
                None, os.path.join(self.templdir, 'test.txt')
            )
            self.assertEqual(src, '{{ burgers }}\n{{ fries }}\n')


if __name__ == '__main__':
    unittest.main()
