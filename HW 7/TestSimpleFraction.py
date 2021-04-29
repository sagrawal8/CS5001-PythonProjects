import unittest
from SimpleFraction import SimpleFraction

class TestSimpleFraction (unittest.TestCase):

    def test_zeroDenominator(self):
        """
        Tests whether denominator can be 0.
        """
        with self.assertRaises(ZeroDivisionError):
            fraction = SimpleFraction(5, 0)

    def test_valueError(self):
        """
        Tests whether any combination of arguments
        can be anything but an integer (string in this case).
        """
        with self.assertRaises(ValueError):
            fraction = SimpleFraction(5, 's')
        with self.assertRaises(ValueError):
            fraction = SimpleFraction('5', 's')
        with self.assertRaises(ValueError):
            fraction = SimpleFraction('5', 7)

    def test_initializeFraction(self):
        """
        Tests initialization of SimpleFraction object.
        """
        fraction = SimpleFraction(5, 6)
        self.assertEqual(fraction.numerator, 5)
        self.assertEqual(fraction.denominator, 6)

    def test_reciprocal(self):
        """
        Tests whether a reciprocal is created and
        the original instance is not modified.
        """
        fraction = SimpleFraction(5, 6)
        reciprocal = fraction.make_reciprocal()
        self.assertEqual(fraction.numerator, 5)
        self.assertEqual(fraction.denominator, 6)
        self.assertEqual(reciprocal.numerator, 6)
        self.assertEqual(reciprocal.denominator, 5)

    def test_validate(self):
        """
        Tests the validate function using initializations
        with arguments other than integers.
        """
        fraction = SimpleFraction(5, 6)
        self.assertEqual(fraction.validate(), True)
        with self.assertRaises(ValueError):
            SimpleFraction(5, 's').validate()
        with self.assertRaises(ValueError):
            SimpleFraction('5', 's').validate()
        with self.assertRaises(ValueError):
            SimpleFraction('5', 7).validate()
        

    def test_multiplyScalar(self):
        """
        Tests multiplication with a scalar number.
        """
        fraction = SimpleFraction(5, 6)
        other = 6
        product = fraction.multiply(other)
        self.assertEqual(product.numerator, 30)
        self.assertEqual(product.denominator, 6)        

    def test_multiplyFraction(self):
        """
        Tests multiplication with another instance of
        SimpleFraction.
        """
        fraction = SimpleFraction(5, 6)
        other = SimpleFraction(2, 3)
        product = fraction.multiply(other)
        self.assertEqual(product.numerator, 10)
        self.assertEqual(product.denominator, 18)        

    def test_multiplyString(self):
        """
        Tests multiplication with a String to see
        if it raises a ValueError.
        """
        fraction = SimpleFraction(5, 6)
        other = 's'
        with self.assertRaises(ValueError):
            product = fraction.multiply(other)

    def test_divideScalar(self):
        """
        Tests division with a scalar number.
        """
        fraction = SimpleFraction(5, 6)
        other = 6
        product = fraction.divide(other)
        self.assertEqual(product.numerator, 5)
        self.assertEqual(product.denominator, 36)

    def test_divideFraction(self):
        """
        Tests division with another instance of
        SimpleFraction.
        """
        fraction = SimpleFraction(5, 6)
        other = SimpleFraction(2, 3)
        product = fraction.divide(other)
        self.assertEqual(product.numerator, 15)
        self.assertEqual(product.denominator, 12)

    def test_divideString(self):
        """
        Tests division with a String to see
        if it raises a ValueError.
        """
        fraction = SimpleFraction(5, 6)
        other = 's'
        with self.assertRaises(ValueError):
            product = fraction.divide(other)

    def test_equalsMethod(self):
        """
        Tests whether the __eq__ method correctly
        equates two fractions.
        """
        fraction = SimpleFraction(5, 6)
        secondFraction = SimpleFraction (15, 18)
        self.assertEqual(fraction, secondFraction)
        thirdFraction = SimpleFraction (16, 18)
        assert fraction.__eq__(thirdFraction) == False

def main():
    unittest.main()

main()
    
        
        
            
