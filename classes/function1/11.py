def polindrome(word):
    left_w = 0
    right_w = len(word)-1
    while right_w>=left_w:
        if word[right_w] != word[left_w]:
            return False
        left_w += 1
        right_w -= 1
    return True
    
a = input()
print(polindrome(a))
