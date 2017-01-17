import os, sys

def windchill(t, ws):
    '''t is temperature in Celsius.
       ws is wind speed in km/h
       wc is the wind chill'''
    wc = 13.12 + 0.6215*t - 11.37*(ws**0.16) + 0.3965*t*(ws**0.16)
    return wc

if __name__=="__main__":
    print ""
    print "+===========================================+"
    print "| W I N D   C H I L L   C A L C U L A T O R |"
    print "+===========================================+"
    print ""
    print "Please, enter the following parameters..."
    temp = float(raw_input("Temperature in Celsius: "))
    wind = float(raw_input("Wind speed in km/h: "))
    print ""
    print "Wind chill: %.1f C" % (windchill(temp, wind))
