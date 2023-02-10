def Convert(grams):
    ounces = 28.3495231 * grams
    return ounces

g = int(input())
print(Convert(g))



#Ex2
def Temp(F):
    C = (5 / 9) * (F - 32)
    return C

t = float(input())
print(Temp(t))
