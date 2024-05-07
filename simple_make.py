import numpy as np
import matplotlib.pyplot as plt


class SimpleMake:
    def __init__(self, arg1):
        self.graph = None
        self.arg1 = arg1
        if arg1.lower() == 'graph':
            arg == "graph"


    if arg1.lower() == 'graph':
        plt.figure()
        ax = plt.gca()

        def make(self, columns, rows, data):
            my_table = plt.table(cellText=data,
                                 colWidths=[0.1] * 3,
                                 rowLabels=rows,
                                 colLabels=columns,
                                 rowColours=None,
                                 loc='upper right')
            self.graph = my_table

        def show(self):
            a = np.random.randn(5)
            plt.plot(a)
            plt.show()