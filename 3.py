import random
b=random.randint(0,9)
for i in range(0,3):
    a=int(input("guess the number(0-9)"))
    if(i<=1):
        if(a==b):
            print("you guessed the right number")
        else:
            print("Wrong!,take another guess")
    else:
        if(a==b):
            print("you guessed the right number")
        else:
            print("Wrong!,the right number was",b)