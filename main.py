import random
from libs import welcome_messege

# 1. Sambutan cukup sekali di awal
welcome_messege("WELCOME TO CUYPY GAMES!!")

user_name = input("INPUT NAME: ")
while user_name == "":
    user_name = input("NAME CANNOT BE EMPTY: ")

# LOOP UTAMA GAME (Supaya bisa main lagi)
while True:
    # 2. PR KEDUA: Pindahkan settingan game ke dalam loop agar di-reset setiap ronde
    cuypy_position = random.randint(1, 4)
    cave_shape = "[]"
    
    # List awal (mentah)
    empty_cave_list = [cave_shape] * 4 
    cave_list = empty_cave_list.copy() 
    cave_list[cuypy_position - 1] = "[-_-]" # Letakkan Cuypy

    # Ubah list jadi string rapi pakai .join()
    empty_cave_string = " ".join(empty_cave_list)
    cave_string = " ".join(cave_list)

    print(f"\nHello {user_name}, see the cave below\n{empty_cave_string}\n")

    # 3. PR PERTAMA: Loop validasi input (harus 1, 2, 3, atau 4)
    user_input = 0
    while user_input not in [1, 2, 3, 4]:
        try:
            user_input = int(input("Which cave do you think Cuypy is in? [1 / 2 / 3 / 4]: "))
            if user_input not in [1, 2, 3, 4]:
                print("OPS! Only choose between 1, 2, 3, or 4.")
        except ValueError:
            print("PLEASE INPUT A NUMBER!")

    # 4. Logika Konfirmasi
    confirm = input(f"ARE YOU SURE CHOSE THE NUMBER {user_input}? [y/n]: ").lower()
    
    if confirm == "y":
        if user_input == cuypy_position:
            print(f"\n{cave_string} \nCONGRATULATIONS {user_name} YOU WIN! CUYPY WAS IN {cuypy_position}")
        else:
            print(f"\n{cave_string} \nNOOO! YOU LOSE. CUYPY WAS IN {cuypy_position}")
        
        # Tanya mau main lagi atau tidak setelah selesai satu ronde
        play_again = input("\nDO YOU WANT TO PLAY AGAIN? [y/n]: ").lower()
        if play_again == "n":
            break
            
    elif confirm == "n":
        print("Okay, let's pick again!")
        continue # Balik ke atas (pilih angka lagi)
    else:
        print("INVALID INPUT, RESTARTING ROUND...")

print("\nTHANK FOR PLAYING THIS GAME!")