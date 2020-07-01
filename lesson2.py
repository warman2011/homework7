from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @abstractmethod
    def square(self):
        pass

    @property
    def consumption(self):
        return round(self.H*2 + 0.3 + self.V/6.5 + 0.5)

class Coat(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)

    def square(self):
        self.sq_c = round(self.V/6.5 + 0.5)
        return self.sq_c


class Suit(Clothes):
    def __init__(self,V, H):
        super().__init__(V, H)

    def square(self):
        self.sq_s = self.H * 2 + 0.3
        return self.sq_s

a = Suit(4, 5)
b = Coat(3, 3)
print(a.square())
print(b.consumption)


