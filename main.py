import unittest
import selenium

class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("I will run before every case")
    def test_methodA(self):
        a= True
        b= True
        print(self.assertEqual(a,b))
    def test_methodB(self):
        print("Test b")
    def tearDown(self):
        print("test done")

if __name__ == '__main__':
    unittest.main()