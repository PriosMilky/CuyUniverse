import socket
from time import sleep
pc_name = socket.gethostname()

def welcome_messege():
    style = "=" * (len(pc_name)+6)
    
    print(style)
    print(f"== {pc_name} ==")
    print(style)
    
def exit_program():
    print("the program is stopped")
    sleep(1)
    print("3..")
    sleep(1)
    print("2..")
    sleep(1)
    print("1..")
    sleep(1)
    print("sistem is shutdown")
    exit()
    
if __name__ == "__main__":
    welcome_messege()
    exit_program()