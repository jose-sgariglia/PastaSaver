from package.pasta import Pasta
from package.pasta_saver import PastaSaver
from package.pasta_timer import PastaTimer


if __name__ == '__main__':
    pasta_saver = PastaSaver()

    pasta_saver.add_Pasta(Pasta("Bucatini", 10), 40)
    pasta_saver.add_Pasta(Pasta("Penne", 15), 120)
    pasta_saver.add_Pasta(Pasta("Spaghetti", 5), 80)
    pasta_saver.add_Pasta(Pasta("Farfalle", 20), 20)
    pasta_saver.add_Pasta(Pasta("Ditalini", 15), 70)

    # print(f"Total Weight: {pasta_saver.total_weight}")
    # print(pasta_saver, '\n')
    #
    # print('Order of cooking')
    # for w, x in pasta_saver.get_order_cook(300):
    #     print(f"Minute: {x.minutes_cook}\t {x.name} - {w} g")
    #
    # print(f"\nTotal Pasta: {pasta_saver.total_weight}")
    # print(pasta_saver)

    pasta_timer = PastaTimer(pasta_saver.get_order_cook(300))

    pasta_timer.timer()
