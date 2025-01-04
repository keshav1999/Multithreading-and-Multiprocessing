import threading


class SquaredSumWorkers(threading.Thread):
    def __init__(self,n, **kwargs):
        self._n = n
        super(SquaredSumWorkers,self).__init__()

    def calculate_sum_squares(self):
        sum_squares = 0
        for i in range(self._n):
            sum_squares+= i**2
        print(sum_squares)
