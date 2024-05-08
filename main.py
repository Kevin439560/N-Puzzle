from menu import switch
from assets import utility


def main():
    while(True):
        case = int(input("Digite qual a opção: "))
        switch(case)
        utility.gerar_matriz()

if __name__ == "__main__":
    main()