import os
import shutil
import sys
import unittest
import json

from bs4 import BeautifulSoup

sys.path.append('..')

from deckmaster import app
app = app.app

# Clear the loaded components, but only once is necessary
try:
	shutil.rmtree('./static/components')
except OSError:
	pass

class TestIndex(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def get_index_soup(self):
    	return BeautifulSoup(self.app.get('/').data, 'html.parser')

    def local(self, scriptdef):
    	if isinstance(scriptdev, basestring):
    		return True
    	return False

    def test_scripts_loaded(self):
    	cfg = json.load(open('site.json'))
    	soup = self.get_index_soup()
    	self.assertEqual(
    		len(list(soup.find_all('script'))),
    		len(cfg['scripts'])
    	)

    def test_scripts_200(self):
		soup = self.get_index_soup()
		for script in soup.find_all('script'):
			self.app.get(script['src'])


if __name__ == '__main__':
    unittest.main()
