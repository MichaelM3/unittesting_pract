import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-5, 5), 0)
        self.assertEqual(calc.add(-20, -20), -40)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-5, 5), -10)
        self.assertEqual(calc.subtract(-20, -20), 0)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-5, 5), -1)
        self.assertEqual(calc.divide(-20, -20), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-5, 5), -25)
        self.assertEqual(calc.multiply(-20, -20), 400)

if __name__ == "__main__":
    unittest.main()