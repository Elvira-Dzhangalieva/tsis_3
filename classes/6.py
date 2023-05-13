def is_prime(n):
    """
    Функция проверяет, является ли число простым.
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True 
    
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
