from .pasta import Pasta
from copy import copy


class PastaSaver:

    def __init__(self):
        self._collection = []

    @property
    def total_weight(self):
        return sum([w for w, x in self._collection])

    def add_Pasta(self, pasta: Pasta, weight: int):
        """Add new Pasta in the collection"""

        if type(pasta) is not Pasta:
            raise TypeError("Only Pasta Object")

        self._collection.append((weight, pasta))
        self._collection.sort(key=lambda x: x[0])

    def __check_pasta_quantity(self, qty: int) -> bool:
        return sum([w for w, _ in self._collection]) >= qty

    def get_order_cook(self, qty: int) -> []:
        if not self.__check_pasta_quantity(qty):
            raise Exception("These isn't enough pasta")

        sum_weight = 0
        pasta_list = []
        while sum_weight <= qty:
            # pasta: Pasta

            weight, pasta = self._collection.pop(0)
            sum_weight += weight
            pasta_list.append((weight, pasta))

        if sum_weight > qty:
            weight, pasta = pasta_list.pop(len(pasta_list) - 1)
            copy_pasta = copy(pasta)

            excessive_pasta = sum_weight - qty
            pasta_list.append((weight - excessive_pasta, pasta))
            self.add_Pasta(copy_pasta, excessive_pasta)

        return sorted(pasta_list, key=lambda x: x[1].minutes_cook, reverse=True)

    def __str__(self):
        output = "Pasta Saver"
        for weight, pasta in self._collection:
            output += f"\n\tPasta: {pasta.name}, Weight: {weight}"
        return output
