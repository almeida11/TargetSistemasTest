guess = int(input("Digite um número: "))

LastTerm, LastButOne = 0, 1
while True:
    Fibonacci = LastTerm + LastButOne
    LastButOne = LastTerm
    LastTerm = Fibonacci
    if guess == Fibonacci:
        print(f"Your guess was in the sequel: {guess}")
        break
    elif Fibonacci > guess:
        print("Your guess was out of sequence!!")
        break
