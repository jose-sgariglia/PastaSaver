from package.pasta import Pasta
from package.PastaSaver import PastaSaver


if __name__ == '__main__':
    pasta_saver = PastaSaver(150)

    pasta_saver.add_Pasta(Pasta("Bucatini", 40, 10))
    pasta_saver.add_Pasta(Pasta("Penne", 120, 11))
    pasta_saver.add_Pasta(Pasta("Spaghetti", 80, 8))
    pasta_saver.add_Pasta(Pasta("Farfalle", 20, 12))
    pasta_saver.add_Pasta(Pasta("Ditalini", 70, 11))

    print(f"Total Weight: {pasta_saver.weight}")

    for x in pasta_saver.get_order_cook():
        print(x)

    print(f"Leftover Pasta: {pasta_saver.weight}")
