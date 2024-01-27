from pasta_saver.pasta_saver import PastaSaver
from pasta_saver.design import BANNER, display_menu, add_new_pasta, get_cook_order, timer
from time import sleep
import os


def main():
    pasta_saver = PastaSaver()
    pasta_to_use = None

    while True:
        os.system('clear')
        print(BANNER)
        option = display_menu()

        match option:
            case 0:
                add_new_pasta(pasta_saver)
                print("Pasta inserita con successo!")
            case 1:
                print("-------- Preparazione --------")
                pasta_to_use = get_cook_order(pasta_saver)
            case 2:
                print("-------- Cottura --------")
                timer(pasta_to_use)
            case 3:
                os.system('clear')
                break
            case _:
                print("-------- Opzione non valida, riprova --------")

        sleep(2)


if __name__ == '__main__':
    main()
