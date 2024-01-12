
import unittest
class test_myclass(unittest.TestCase):
    def test_addition(self):
        result=2+2 
        self.assertEqual(result, 4)
    
    def test_sub(self):
        result=5-2
        self.assertEqual(result,3)
    
    def test_multi(self):
        result=5*2
        self.assertEqual(result,10)

    def test_div(self):
        result=10/2
        self.assertEqual(result,5)

if __name__ =="__main__":
    unittest.main()