from itertools import chain


class Observed:
    def __init__(self):
        self.__observers = set()

    def _attach(self, observer, *observers):
        for observer in chain((observer, ), observers):
            self.__observers.add(observer)
            observer.update(self)

    def _discard(self, observer):
        self.__observers.remove(observer)

    def _notify(self, info=None):
        for observer in self.__observers:
            observer.update(info)
