from libs import welcome_messege, exit_program
from games import cuypy
from tool import shop

# 1. Sambutan cukup sekali di awal
def menu():
    user_option = int(input(f"menu program:\n1.Game\n2.Mini Store\n3.exit\n\nsilahkan pilih:"))
    
    if user_option == 1:
        cuypy.start()
    elif user_option == 2:
        shop.start()
    elif user_option == 3:
         exit_program()
    else:
        print("hanya boleh 1,2,3")
        

def main():
    welcome_messege()
    menu()
    
if __name__ == "__main__":
    main()