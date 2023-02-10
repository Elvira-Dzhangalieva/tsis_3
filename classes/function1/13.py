def play(num):
    print("Hello! What is your name?")
    name = input()
    print("Well,",name,"I am thinking of a number between 1 and 20.")
    print("Take a guess.")

    n = int(input())
    k = 1
    while num != n:
        if num > n:
            print("Your guess is too low.")
        elif num < n:
            print("Your guess is too big.")
        print("Take a guess.")
        n = int(input())
        k += 1
    print("Good job,",name,"! You guessed my number in",k,"guesses!")


x = int(input())
play(x)