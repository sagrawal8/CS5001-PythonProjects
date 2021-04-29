from temperature import *
'Two test cases: First one uses 100.1F and the second uses 49.04C'

def test_fahrenheit_to_celsius_1 ():
    print("Fahrenheit to Celisus:\nEntered input to convert is 100.1F.\nExpected result is 37.83.")
    print("Actual result is ", round(convert_fahrenheit_to_celsius(100.1), 2))


def test_celsius_to_fahrenheit_1 ():
    print("\nCelsius to Fahrenheit:\nEntered input is 49.04C.\nExpected result is 120.27.")
    print("Actual result is ", round(convert_celsius_to_fahrenheit(49.04), 2))

def main():
    test_fahrenheit_to_celsius_1 ()
    test_celsius_to_fahrenheit_1 ()
main()
