import os, sys, math

def dew_point(t, rh):
    '''t is the air temperaturs
       rh is the relative humidity
       tdp is temperature of dew point
       https://en.wikipedia.org/wiki/Dew_point
       '''

    a = 6.1121
    b = 18.678
    c = 257.14
    d = 234.5
    gamma = math.log(rh/100. * math.exp((b-t/d)*(t/(c+t))))
    tdp = (c*gamma) / (b-gamma)
    return tdp


if __name__=="__main__":
    print ""
    print "+==========================================+"
    print "| D E W    P O I N T   C A L C U L A T O R |"
    print "+==========================================+"
    print ""
    print "Please, enter the following parameters..."
    temp = float(raw_input("Temperature in Celsius: "))
    humidity = float(raw_input("Relative humidity in percent: "))
    print ""
    print "Dew point: %.1f C" % (dew_point(temp, humidity))
