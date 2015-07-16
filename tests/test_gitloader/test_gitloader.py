"""Test Jinja2 Git Template Loader"""

import unittest
import sys
import os

# The tool relies on the cwd, this helps support nose from project root.
# Does not use CLI tool.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

sys.path.append('../..')

import deckmaster
from deckmaster.app import GitLoader

app = deckmaster.app.get_instance()

class TestGitLoader(unittest.TestCase):

    basedir = os.path.realpath(
        os.path.join(os.path.abspath(__file__), '..', '..', '..')
    )
    templdir = 'tests/test_gitloader/templates'

    def test_file_load(self):
        """Can the loader get a simple, local file?"""
        with app.test_request_context('/test.txt'):
            src, templ, reload = GitLoader().get_source(
                None, os.path.join(self.basedir, self.templdir, 'test.txt')
            )
            self.assertEqual(src, '{{ burgers }}\n{{ fries }}\n')

    def test_git_load(self):
        """Can the loader get a template at a specific revision?"""
        with app.test_request_context('/test.txt@04b9187f2f322ede2f5e0d77ae535c1f90ed21c9'):
            src, templ, reload = GitLoader().get_source(
                None, os.path.join(self.templdir, 'test.txt')
            )
            self.assertEqual(src, '{{ burgers }}\n{{ fries }}\n')

class TestGitView(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_view_at_revision(self):
        self.app.get('/')
        self.app.get('/static/script.js')


if __name__ == '__main__':
    unittest.main()
