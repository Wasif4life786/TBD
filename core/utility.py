import math
def DegToRad(deg):
    return float(deg * math.pi/180)
def RadToDeg(rad):
    return float(rad * 180/math.pi)
def Clamp(x,MIN,MAX):
    if x < MIN:
        return MIN
    elif x > MAX:
        return MAX
    return x