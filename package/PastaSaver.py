from .pasta import Pasta
from copy import copy


class PastaSaver:

    def __init__(self, total):
        self._collection = []
        self.total = total

    @property
    def weight(self):
        return sum([w for w, x in self._collection])

    def add_Pasta(self, pasta: Pasta):
        """Add new Pasta in the collection"""

        if type(pasta) is not Pasta:
            raise TypeError("Only Pasta Object")

        self._collection.append((pasta.weight, pasta))
        self._collection.sort(key=lambda x: x[0])

    def __check_pasta_quantity(self):
        return sum([x.weight for n, x in self._collection]) >= self.total

    def get_order_cook(self) -> []:
        if not self.__check_pasta_quantity():
            raise Exception("These isn't enough pasta")

        sum_weight = 0
        pasta_list = []
        while sum_weight <= self.total:
            pasta: Pasta

            name, pasta = self._collection.pop(0)
            sum_weight += pasta.weight
            pasta_list.append(pasta)

        if sum_weight > self.total:
            pasta = pasta_list[-1]
            copy_pasta = copy(pasta)

            excessive_pasta = sum_weight - self.total
            pasta.weight = pasta.weight - excessive_pasta
            copy_pasta.weight = excessive_pasta
            self.add_Pasta(copy_pasta)

        return sorted(pasta_list, key=lambda x: x.minutes_cook, reverse=True)

    def __str__(self):
        output = "Pasta Saver"
        for name, pasta in self._collection:
            output += f"\n\tName: {name}, Pasta: {pasta}"
        return output
