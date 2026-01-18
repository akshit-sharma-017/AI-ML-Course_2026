import random
def guess_game():
    a=random.randint(1,10)
    for i in range(0,3):
        b=int(input("Enter your guess between 1 to 10: "))
        if b==a:
            print("You guessed it right!")
            break
        else:
            if(i==2):
                print("You lost!. The correct number was", a)
            else:
                print(f"Try again!({2-i} attempts left)")

print("Welcome to the Number Guessing Game!")
n=input("Do you want to play the game? (yes/no): ")
if(n=="yes"):
    guess_game()
else:
    print("Thank you! Have a nice day.")