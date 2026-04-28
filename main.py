import random

welcome_messege = "WELCOME TO CUYPY GAMES!!"
cuypy_position = random.randint(1,4)

print("==============================")
print(f"== {welcome_messege} ==")
print("==============================")

user_name = input("INPUT NAME: ")

cave_shape = "[]"
empty_cave = [cave_shape] * 4 #harus tetep kosong
cave = empty_cave.copy() #tempat baru cuypy yg nanti isinya

# menggunakan -1 karena ingin sesuai dengan manusia
# contoh array nya adalah 3 menggunakan -1 jadi 2 maka akan di tampilkan cuypy-nya itu di 2
cave[cuypy_position -1] = "[-_-]"


print(f'''
Hello {user_name}, see the cave below
{" ".join(empty_cave)}
''')

while True:
    user_input = int(input("Which cave do you think Cuypy is in? [1 / 2 / 3 / 4]: "))
    
    confirm = input(f"ARE YOU SURE CHOSE THE NUMBER {user_input}? [y/n]")
    
    if confirm == "y":
        if user_input == cuypy_position:
            print(f"{" ".join(cave)} \n CONGRATULATIONS {user_name} YOU WIN, , CUYPY POSITION IN {cuypy_position}")
            exit()
        else:
            print(f"{" ".join(cave)} \n NO YOU LOSE, , CUYPY POSITION IN {cuypy_position} AND YOU SELECTED IS {user_input}")
            break
    elif confirm == "n":
        exit()
    else:
        print("PLEASE REPEAT AGAIN")
