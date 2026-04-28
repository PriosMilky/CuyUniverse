import random

welcome_messege = "WELCOME TO CUYPY GAMES!!"
cuypy_position = random.randint(1,4)

print("==============================")
print(f"== {welcome_messege} ==")
print("==============================")

user_name = input("INPUT NAME: ")
    
print(f'''
Hello {user_name}, see the cave below
[] [] [] []
''')


while True:
    user_input = int(input("Which cave do you think Cuypy is in? [1 / 2 / 3 / 4]: "))
    
    confirm = input(f"ARE YOU SURE CHOSE THE NUMBER {user_input}? [y/n]")
    
    if confirm == "y":
        if user_input == cuypy_position:
            print(f"CONGRATULATIONS {user_name} YOU WIN, , CUYPY POSITION IN {cuypy_position}")
            exit()
        else:
            print(f"NO YOU LOSE, , CUYPY POSITION IN {cuypy_position} AND YOU SELECTED IS {user_input}")
            break
    elif confirm == "n":
        exit()
    else:
        print("PLEASE REPEAT AGAIN")
