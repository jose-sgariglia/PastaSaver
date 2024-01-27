from .observer_pattern.observer import Observer


class Pasta(Observer):
    def __init__(self, name: str, minutes_cook: int):
        self.name = name
        self.minutes_cook = minutes_cook

    def update(self, info=None):
        if info is None:
            raise ValueError

        if self.minutes_cook == info:
            print(f"\t\aCalare: {self.name}")
        pass

    def __str__(self):
        return f"({self.name}, {self.minutes_cook})"
