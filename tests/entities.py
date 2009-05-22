import unittest

from trml2pdf import parse_string

class EntitiesTestCase(unittest.TestCase):
    def test_entities(self):
        # test that a paragraph can have a "&amp;"
        # TODO: write a proper test
        self.failUnless(parse_string(file("entities.rml", 'r').read()))
        
if __name__ == '__main__':
    unittest.main()

