class SimpleFraction:

    def __init__(self, numerator, denominator):
        '''
        Function: SimpleFraction constructor
        Parameters:
            numerator (int): numerator of fraction
            denominator (int): denominator of fraction
        Returns: None
        Does: creates a simple fraction instance with 'numerator'
              as numerator and 'denominator' as denominator.
        '''
        if(denominator == 0):
            raise ZeroDivisionError("Divison by 0 not allowed")

        if(isinstance(numerator, int) and isinstance(denominator, int)):
            self.numerator = numerator
            self.denominator = denominator            
        else:
            raise ValueError("Only integers are allowed")

    def make_reciprocal(self):
        '''
        Function: make_reciprocal
        Parameters: None
        Returns: Instance of SimpleFraction 
        Does: Returns the reciprocal of itself
        '''
        return SimpleFraction(self.denominator, self.numerator)

    def validate(self):
        '''
        Function: validate
        Parameters: None
        Returns: True or raises ValueError
        Does: Returns True if numerator and denominator are integers
              Raises Value Error if not.
        '''
        if(isinstance(self.numerator, int)
           and isinstance(self.denominator, int)
           ):
            return True
        else:
            raise ValueError("Only integers are allowed")

    def multiply(self, other):
        '''
        Function: multiply
        Parameters:
            other (instance of SimpleFraction):
                Another Fraction
        Returns: An instance of SimpleFraction
        Does: Multiplies the two fraction and returns its product.
              Checks if argument is an integer or an instance of
              SimpleFraction or neither.
        '''
        if(isinstance(other, int)):
            multipliedNumerator = self.numerator * other
            return SimpleFraction(multipliedNumerator, self.denominator)
        
        elif(isinstance(other, SimpleFraction)):
            newNumerator = self.numerator * other.numerator
            newDenominator = self.denominator * other.denominator
            return SimpleFraction(newNumerator, newDenominator)

        else:
            raise ValueError("Number/Fraction to be multiplied with is "
                            + "neither an integer nor an obj of Simple Fraction")

    def divide(self, other):
        '''
        Function: divide
        Parameters:
            other (instance of SimpleFraction):
                Another Fraction
        Returns: An instance of SimpleFraction
        Does: Divides the two fraction and returns its quotient.
              Checks if argument is an integer or an instance of
              SimpleFraction or neither.
        '''
        if(isinstance(other, int)):
            dividedDenominator = self.denominator * other
            return SimpleFraction(self.numerator, dividedDenominator)

        elif(isinstance(other, SimpleFraction)):
            newNumerator = self.numerator * other.denominator
            newDenominator = self.denominator * other.numerator
            return SimpleFraction(newNumerator, newDenominator)

        else:
            raise ValueError("Number/Fraction to be divided with is neither "
                            + "an integer nor an obj of Simple Fraction")

    def __str__(self):
        '''
        Function: divide
        Parameters: None
        Returns: None
        Does: Prints the current instance of SimpleFraction
        '''
        return '{self.numerator}/{self.denominator}'.format(self = self)

    def __eq__(self, other):
        '''
        Function: divide
        Parameters:
            other (instance of SimpleFraction):
                Another Fraction
        Returns: True or False
        Does: Equates the two fractions by cross multiplying
            and returns True if equal and False if not.
        '''
        if(isinstance(other, int)):
            secondFraction = SimpleFraction(other, 1)
        elif(isinstance(other, SimpleFraction)):
            secondFraction = other
        if(
            self.numerator * secondFraction.denominator
            == secondFraction.numerator * self.denominator
        ):
            return True

        else:
            return False

    
        
            

    
