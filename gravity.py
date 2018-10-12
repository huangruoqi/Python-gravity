#Oct-12-2018
GRAVITY_EARTH = 9.8
HEIGHT_0 = 16
def calcFallTime(t, v, h):
    h=-0.5*GRAVITY_EARTH*t*t+v*t+h
    return h


print "Calculate the height you will achieve"

time=0.6
velocity=16
height=HEIGHT_0

final=calcFallTime(time, velocity, height)
print "After 1.6 seconds with a starting"
print "velocity of 16 ft/sec and a starting"
print "height of 16 feet"
print ""
print "You will achieve "+str(final)+" feet"
