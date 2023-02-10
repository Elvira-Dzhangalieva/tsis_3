def IsPrime(num):
    if num == 0 or num == 1:
        return False
    cnt = True
    for i in range(2, num):
        if(num % 2 == 0):
            cnt = False 
    if(cnt):
        return True 
    else:
        return False 
    
def filter_prime(all_num):
    prime_num = list()
    for i in all_num:
        if(IsPrime(i)):
            prime_num.append(i)
    return prime_num


size_list = int(input())
list_1 = list()
for i in range(size_list):
    list_1.append(int(input()))

print(filter_prime(list_1))