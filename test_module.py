#!/usr/bin/python3
import unittest
from calculate import calculate

class TestCalculate(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(calculate('12', '+', '345'), '   12\n+ 345\n----\n  357\n    ')
        self.assertEqual(calculate('9999', '+', '1234'), 'Number cannot be more than four digits')
        self.assertEqual(calculate('1', '+', 'abc'), 'Invalid operands')
    
    def test_subtraction(self):
        self.assertEqual(calculate('1234', '-', '567'), ' 1234\n- 567\n----\n  667\n    ')
        self.assertEqual(calculate('12', '-', '3456'), 'Number cannot be more than four digits')
        self.assertEqual(calculate('1', '-', 'abc'), 'Invalid operands')
    
    def test_invalid_operator(self):
        self.assertEqual(calculate('12', '*', '34'), 'Invalid operator')
    
    def test_invalid_operands(self):
        self.assertEqual(calculate('12a', '+', '34'), 'Invalid operands')
        self.assertEqual(calculate('12', '+', '34a'), 'Invalid operands')
        self.assertEqual(calculate('12345', '-', '6789'), 'Number cannot be more than four digits')
    
if __name__ == '__main__':
    unittest.main()
