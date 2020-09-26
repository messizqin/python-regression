"""
constants.py
copyright 2020 @Messiz Qin https://github.com/Weilory

* Perform 0 or positive exponential regression by matrices transformation

<Plane>
    Implement exponential regression with the support from matrices.py
    inited by a vector
    call recurse, assign to formulate to get result
"""

from regression.matrices import Matrix
from regression.modules import Vector


class Plane:
    """ cartesian plane matrix transformation """

    def __init__(self, vector):
        self.coefficient = Matrix([[xx for kk in range(len(vector) - 1)] for xx in vector.x]).exponential_by_index()
        for coe in self.coefficient:
            coe.append(1)
        self.constant = Matrix(*vector.y)
        self.length = len(vector)
        self.coe_record = []
        self.con_record = []
        self.results = []

    # remove 1 at end
    def shrink(self):
        co = self.coefficient[0].concat()
        co.pop()
        self.coe_record.append(co)
        self.con_record.append(self.constant[0][0])
        self.coefficient = self.coefficient.reduce_row_by_subtract()
        self.constant = self.constant.reduce_row_by_subtract()
        sue = 0
        for coe in self.coefficient:
            if coe[-1] == 0:
                sue += 1
        if sue == self.coefficient.__len__():
            for coe in self.coefficient:
                coe.pop()

    # create 1 at end
    def formal(self):
        for ii, coe_row in enumerate(self.coefficient):
            self.constant[ii] /= coe_row[-1]
            coe_row /= coe_row[-1]

    # make both coefficient and constant length equal to 1
    def recurse(self):
        for ii in range(self.length * 2 - 2):
            if ii % 2 == 0:
                self.shrink()
            else:
                self.formal()
        self.results.append(self.constant[0][0] / self.coefficient[0][0])

    def formulate(self):
        self.recurse()
        coefficients = list(reversed(self.coe_record))
        constants = list(reversed(self.con_record))
        for ind, coe in enumerate(coefficients):
            minus = 0
            for ii, dd in enumerate(coe):
                minus += dd * self.results[ii]
            self.results.append(constants[ind] - minus)
        return self.results


if __name__ == '__main__':
    pass
    # 2x^{2}+3x+1
    # [2, 3, 1]
    # dots = Vector(
    #     x_val=[-2, -1, 1],
    #     y_val=[3, 0, 6],
    # )

    # 0.5x^{3}+2x^{2}+3x+1
    # [0.5, 2, 3, 1]
    # dots = Vector(
    #     x_val=[-2, -1, 0, 1],
    #     y_val=[-1, -0.5, 1, 6.5],
    # )

    # xs = [1, 2, 3]
    # dots = Vector(
    #     x_val=xs,
    #     y_val=[2 * x ** 2 + 1 * x + 99 for x in xs],
    # )

    # xs = [1, 2, 3, 4]
    # dots = Vector(
    #     x_val=xs,
    #     y_val=[3 * x ** 3 + 2 * x ** 2 + 1 * x + 99 for x in xs],
    # )

    # xs = [x for x in range(11)]
    # dots = Vector(
    #     x_val=xs,
    #     y_val=[10 * x ** 10 for x in xs],
    # )
    #
    # c = Plane(dots)
    # print(c.formulate())