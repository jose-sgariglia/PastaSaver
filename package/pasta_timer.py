from .observer_pattern.observed import Observed
from time import time, sleep


class PastaTimer(Observed):

    def __init__(self, pasta_to_cook: list):
        super().__init__()
        self.__max_time = pasta_to_cook[0][1].minutes_cook
        for _, pasta in pasta_to_cook:
            self._attach(pasta)

    def timer(self):
        start_timer = time()

        print("Timer Start")
        while int(time() - start_timer) <= self.__max_time:
            cooking_time = int(self.__max_time - (time() - start_timer)) + 1
            print(f"----------- Minute {cooking_time} ------------------")
            self._notify(cooking_time)
            sleep(1)

        print("Timer End")
