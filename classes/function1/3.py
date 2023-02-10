def solve(numheads, numlegs):
    #numlegs = 4 * r + 2 * c
    #numheads = r + c
    r = (numlegs - 2 * numheads)//2
    c= numheads - r
    print(r, c)
heads = int(input()) #35
legs = int(input()) #94
solve(heads,legs)
