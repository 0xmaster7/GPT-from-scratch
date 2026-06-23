import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        list1 = []
        res = 0
        for x in z:
            res = 1/(1+np.exp(-x))
            list1.append(round(res,5))
            res = 0
        return list1

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        list1 = []
        for x in z:
            if x < 0:
                list1.append(0/1.0)
            else:
                list1.append(x/1.0)
        return list1
