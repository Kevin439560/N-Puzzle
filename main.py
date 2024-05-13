from menu import menu as menu_module 

def main():
    while(True):
        menu = menu_module()       
        case = int(input("Escolha um algoritmo: "))
        menu.switch(case)
        
if __name__ == "__main__":
    main()