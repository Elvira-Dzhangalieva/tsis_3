ll = []
def prime(List):
    for x in List:
        if (int(x)%2==1):
            ll.append(x)
    print(ll)

l = list(input().split())
prime(l)

