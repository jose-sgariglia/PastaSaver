class Pasta:
    def __init__(self, name: str, weight: int, minutes_cook: int):
        self.name = name
        self.weight = weight
        self.minutes_cook = minutes_cook

    def __str__(self):
        return f"({self.name}, {self.weight}, {self.minutes_cook})"
