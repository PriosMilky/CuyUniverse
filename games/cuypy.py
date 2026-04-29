import random
import main

# LOOP UTAMA GAME
def start():
    while True:
        # 2. Reset posisi Cuypy dan tampilan cave setiap ronde baru
        cuypy_position = random.randint(1, 4)
        cave_shape = "[]"
        
        empty_cave_list = [cave_shape] * 4 
        cave_list = empty_cave_list.copy() 
        cave_list[cuypy_position - 1] = "[-_-]" 

        empty_cave_string = " ".join(empty_cave_list)
        cave_string = " ".join(cave_list)

        print(f"\nSee the cave below:\n{empty_cave_string}\n")

        # 3. Loop Validasi Input (Hanya 1-4)
        user_input = 0
        while user_input not in [1, 2, 3, 4]:
            try:
                user_input = int(input("Which cave do you think Cuypy is in? [1/2/3/4]: "))
                if user_input not in [1, 2, 3, 4]:
                    print("OPS! Only choose between 1, 2, 3, or 4.")
            except ValueError:
                print("PLEASE INPUT A NUMBER!")

        # 4. Logika Menang/Kalah (Di luar loop validasi)
        if user_input == cuypy_position:
            print(f"\n{cave_string}")
            print(f"CONGRATULATIONS! YOU WIN! CUYPY WAS IN {cuypy_position}")
        else:
            print(f"\n{cave_string}")
            print(f"NOOO! YOU LOSE. CUYPY WAS IN {cuypy_position}")
        
        # 5. Fitur Keluar Game Langsung
        play_again = input("\nDO YOU WANT TO PLAY AGAIN? [y/n]: ").lower()
        if play_again == "n":
            main.menu()

    # Pesan penutup (di luar while True)
    print("\nTHANK FOR PLAYING THIS GAME!")
    
if __name__ == "__main__":
    start()