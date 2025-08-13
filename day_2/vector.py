
import math

def normalize(v):
    magnitude = math.sqrt(sum(coord**2 for coord in v))
    if magnitude == 0:
        return v
    return tuple(coord/magnitude for coord in v)

print (dotproduct((2, 3, 4), (3, 4, 5)))