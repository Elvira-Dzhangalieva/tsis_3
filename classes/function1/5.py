import itertools

def Permutation(s):
    perm_set = itertools.permutations(s)
    for x in perm_set:
        print(x)
    
string = input()
Permutation(string)


