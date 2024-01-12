
import unittest
class TestClass(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("SofTWAriCA".upper(), 'SOFTWARICA')

    def test_lower(self):
        self.assertEqual("SOFTWARICA".lower(), 'softwarica')

    def test_isupper(self):
        self.assertTrue("HELLO".isupper())
        self.assertFalse('SoFt'.isupper())

    def test_split(self):
        a="Helloo World"
        self.assertEqual(a.split(),['Helloo','World'])
        with self.assertRaises(TypeError):
            a.split(2)
    
if __name__=="__main__":
    unittest.main()