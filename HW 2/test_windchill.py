'''
   CS5001
   Fall 2020
   Keith
   Homework 2: Windchill Tests
'''

from windchill import calculate_windchill

def report_results(temperature : float,
                   speed : float,
                   expected : float,
                   actual : float) -> None:
    ''' Function report_results
        Parameters:
            temperature: (float): temperature in Fahrenheit
            speed: (float): speed (velocity) in miles per hour
            expected: (float) expected wci from temp & speed
            actual: (float) actual result from calculation
        Returns: Nothing; user interaction function that prints
                 actual vs expected result
    '''
    print("For inputs temperature =", temperature, "speed =", speed,  "...\n"
          "\tExpected:", expected, "(+/- 0.1)\n"
          "\tActual:", actual )
    

def test_windchill_index(temperature, speed, expected ):
    ''' Function: test_windchill_index
        Parameters:
            temperature: (float): temperature in Fahrenheit
            speed: (float): speed (velocity) in miles per hour
                   REQUIRE: speed >= 3mph and temperature < 50F
            expected: (float) expected wci from temp & speed
        Returns: nothing, calls the report function to see what happened
    '''
    actual = calculate_windchill(temperature, speed)
    report_results(temperature, speed, expected, actual)
    
def main():
    test_windchill_index(22, 10, 11.3)
    test_windchill_index(20, 3, 15.7)
    test_windchill_index(40, 5, 36.5)
    test_windchill_index(49.9, 3, 49.6)

    

main()
