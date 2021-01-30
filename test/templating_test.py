import unittest
 
from templating import PromptTemplate
 
class Test_PromptTemplate(unittest.TestCase):
    def test_render_hi(self):
        t = PromptTemplate('template/example.yaml')
        assert t.render('hi') == 'Hello World!'
    
    def test_render_hi_name(self):
        name = 'Jochen'
        t = PromptTemplate('template/example.yaml')
        assert t.render('hi_name', name=name) == 'Hello Jochen!'

if "__main__" == __name__:
    unittest.main()