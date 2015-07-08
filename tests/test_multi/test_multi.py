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

    def get_soup(self, url):
    	return BeautifulSoup(self.app.get(url).data, 'html.parser')

    def test_scripts_loaded(self):
    	"""Does the number of scripts match the spec for each route?"""
        cfg = json.load(open('site.json'))
    	soup = self.get_soup('/')
    	self.assertEqual(len(list(soup.find_all('script'))),3)
        soup = self.get_soup('/a')
        self.assertEqual(len(list(soup.find_all('script'))),2)
        soup = self.get_soup('/b')
        self.assertEqual(len(list(soup.find_all('script'))),1)

    def test_scripts_200(self):
        """Are each of the scripts for each route available?"""
        for url in ('/','/a','/b'):
            soup = self.get_soup(url)
            for script in soup.find_all('script'):
                self.app.get(script['src'])


if __name__ == '__main__':
    unittest.main()
