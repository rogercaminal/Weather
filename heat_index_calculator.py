import os, sys
import temperature_conversion

def heat_index(t, h):
    '''t is the temperature in fahrenheit
       h is the air humidity in percent
       hi is the heat index
       https://en.wikipedia.org/wiki/Heat_index
       '''
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -6.83783e-3
    c6 = -5.481717e-2
    c7 = 1.22874e-3
    c8 = 8.5282e-4
    c9 = -1.99e-6

    hi = t
    if t>80.:
        hi = c1 + c2*t + c3*h + c4*t*h + c5*(t**2) + c6*(h**2) + c7*(t**2)*h + c8*t*(h**2) + c9*(t**2)*(h**2)
    return hi
       

if __name__=="__main__":
    print ""
    print "+===========================================+"
    print "| H E A T   I N D E X   C A L C U L A T O R |"
    print "+===========================================+"
    print ""
    print "Please, enter the following parameters..."
    temp = float(raw_input("Temperature in Celsius: "))
    humidity = float(raw_input("Relative humidity in percent: "))
    print ""
    temp_fahrenheit = temperature_conversion.celsius_to_fahrenheit(temp)
    heat_index_fahrenheit = heat_index(temp_fahrenheit, humidity)
    print "Heat index: %.1f C" % (temperature_conversion.fahrenheit_to_celsius(heat_index_fahrenheit))
