from diggame import *
import numpy as np

class Mesh():
    def __init__(self) -> None:
        self.hits = (i for i in np.random.choice(np.arange(900), 
                                    size = (100), 
                                    replace=False))

    def __call__(self) -> int:
        return next(self.hits)

for i in range(1):
    playGame(Mesh(), dir = "./data/mesh")
