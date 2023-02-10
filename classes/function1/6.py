def reverse(s):
    words = s.split()
    string = []
    for word in words:
        string.insert(0, word)

    print(" ".join(string))

x = input()
reverse(x)
