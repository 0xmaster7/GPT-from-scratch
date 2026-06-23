import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        list1 = []
        sum1 = 0
        max_val = max(z)
        for x in z:
            list1.append(np.exp(x - max_val))
            sum1 += np.exp(x- max_val)
        for i in range(len(list1)):
            list1[i] = round(list1[i]/sum1,4)
        return list1
