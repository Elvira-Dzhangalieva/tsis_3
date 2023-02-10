def Temp(F):
    C = (5 / 9) * (F - 32)
    return C

t = float(input())
print(Temp(t))