from .pasta import Pasta
from .pasta_saver import PastaSaver
from .pasta_timer import PastaTimer
from simple_term_menu import TerminalMenu

BANNER = """
     ooooooooo.                          .                   .oooooo..o                                          
    `888   `Y88.                      .o8                  d8P'    `Y8                                          
     888   .d88'  .oooo.    .oooo.o .o888oo  .oooo.        Y88bo.       .oooo.   oooo    ooo  .ooooo.  oooo d8b 
     888ooo88P'  `P  )88b  d88(  "8   888   `P  )88b        `"Y8888o.  `P  )88b   `88.  .8'  d88' `88b `888""8P 
     888          .oP"888  `"Y88b.    888    .oP"888            `"Y88b  .oP"888    `88..8'   888ooo888  888     
     888         d8(  888  o.  )88b   888 . d8(  888       oo     .d8P d8(  888     `888'    888    .o  888     
    o888o        `Y888""8o 8""888P'   "888" `Y888""8o      8""88888P'  `Y888""8o     `8'     `Y8bod8P' d888b    
"""


def display_menu() -> int:
    options = ['[] Inserisci nuova pasta', '[] Richiedi quantità di pasta e cottura', '[] Timer per la pasta', '[] Esci']
    terminal_menu = TerminalMenu(options, title="Options")
    return terminal_menu.show()


def add_new_pasta(pasta_saver: PastaSaver):
    name = input("Inserisci il nome della pasta: ")
    weight = int(input("Inserisci il peso della pasta (in grammi): "))
    cook_time = int(input("Inserisci il tempo di cottura della pasta (in minuti): "))

    new_pasta = Pasta(name, cook_time)
    pasta_saver.add_Pasta(new_pasta, weight)


def get_cook_order(pasta_saver):
    try:
        qty = int(input("Inserisci la quantità di pasta desiderata (in grammi): "))
        order = pasta_saver.get_order_cook(qty)
        print("Pasta da cucinare:")
        for weight, pasta in order:
            print(f"\tPasta: {pasta.name}, Peso: {weight}, Tempo di cottura: {pasta.minutes_cook} minuti")

        print("\nPasta nella dispensa")
        for weight, pasta in pasta_saver.food_storage:
            print(f"\tPasta: {pasta.name}, Peso: {weight}")
        input()
        return order
    except ValueError:
        print("!! Non hai abbastanza pasta !!")
        return None


def timer(pasta_to_use):
    if not pasta_to_use:
        print("Preparare prima la pasta")
        return

    pasta_timer = PastaTimer(pasta_to_use)
    input("Attiva quando l'acqua bolle...")

    pasta_timer.timer()

    input("Scolare la pasta...")
