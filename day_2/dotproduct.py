
def dotproduct(v1, v2):
    dotp = 0
    if len(v1) != len(v2):
        return "Error"
    for i in range(len (v1)):
        dotp = dotp + (v1[i] * v2[i])
    return dotp

print (dotproduct((2, 3, 4), (3, 4, 5)))