"""Test the routed `site.json`."""

import os
import shutil
import sys
import unittest
import json

from bs4 import BeautifulSoup

# The tool relies on the cwd, this helps support nose from project root.
# Does not use CLI tool.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# This will now also be relative to the file, not the shell cwd.
sys.path.append('../..')

from deckmaster import app
app = app.get_instance()

# Clear the loaded components, but only once
try:
    shutil.rmtree('./static/components')
except OSError:
    pass

class TestMulti(unittest.TestCase):
    """Test the basic dynamic generation of multiple routes."""

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def get_index_soup(self):
    	return BeautifulSoup(self.app.get('/').data, 'html.parser')

    def test_scripts_loaded(self):
    	"""Does the number of script elements match the route in `site.json`?"""
        cfg = json.load(open('site.json'))
        print cfg
    	soup = self.get_index_soup()
    	self.assertEqual(len(list(soup.find_all('script'))),3)

    def test_scripts_200(self):
        """Are each of the scripts for this route available?"""
        soup = self.get_index_soup()
        for script in soup.find_all('script'):
            self.app.get(script['src'])


if __name__ == '__main__':
    unittest.main()
