import matplotlib.pyplot as plt


class SimpleMake:
    def __init__(self, arg1):
        self.graph = None
        self.arg1 = arg1
        self.total = 0
        self.avg = 0

    def make(self, columns, rows, data):
        if self.arg1 == 'graph':
            plt.figure()
            my_table = plt.table(cellText=data,
                                colWidths=[0.1] * 3,
                                rowLabels=rows,
                                colLabels=columns,
                                rowColours=None,
                                loc='upper right')
            try:
                items = 0
                for thing in data:
                    self.total += sum(thing)
                    items += len(thing)
                self.avg = self.total/items

            except Exception as e:
                self.total = None
            self.graph = my_table

    def show(self):
        if self.arg1 == 'graph':
            a = 1
            plt.plot(a)
            plt.show()

    def __call__(self, arg3):
        if arg3.lower() == 'total':
            return self.total
        if arg3.lower() == "avg":
            return self.avg
