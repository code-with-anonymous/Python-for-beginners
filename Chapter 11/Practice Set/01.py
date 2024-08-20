class TwoDimVector:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    def showVector(self):
        print(f"i is {self.i} and j is {self.j}")


class ThreeDimVector(TwoDimVector):
    def __init__(self, i, j, k) -> None:
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


# Creating instances of TwoDimVector and ThreeDimVector
a = TwoDimVector(1, 2)
a.showVector()  # This will print "i is 1 and j is 2"

b = ThreeDimVector(5, 2, 3)
b.show()  # This will print "The vector is 5i + 2j + 3k"
