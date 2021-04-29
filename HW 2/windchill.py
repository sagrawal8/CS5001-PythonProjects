from temperature import *

'Converts temp from F to C and speed from mph to kms and then converts the windchill back from C to F'

def calculate_windchill(temperature_f : float, speed_mph : float) -> float:

    temperature_c = float(convert_fahrenheit_to_celsius (temperature_f))
    speed_kms = float(1.61 * speed_mph)
    
    windchill = float(13.12 + 0.6215 * temperature_c - 11.37 * pow(speed_kms, 0.16) + 0.3965 * temperature_c * pow(speed_kms, 0.16))
    return round(convert_celsius_to_fahrenheit(windchill), 1)
    
