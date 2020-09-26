"""
matrices.py
copyright 2020 @Messiz Qin https://github.com/Weilory

* similar to numpy.array, treat list as number

<Base>
    to access Array methods

<Variance>
    nested inheritance

<Array> <- <Base>
    treat list as number
    can be inited by following: list, Array, numeric

<Matrix> <- <Variance>
    treat [list, list..] as number
    can be inited by following: list, Array, numeric, [list, list..], [Array, Array..], [list, Array..]
"""

import numpy as np


class Base:
    """
        Variance Separation Architecture
            * can treated as mix-ins from inheritance
            * support n depth matrix operation
                which 1-depth refers to Array
                [1, 2..] + 2 => [3, 5..]
                2-depth refers to Matrix
                [[1, 2]..] + 2 => [[3, 5]..]

        What is the purpose:
            treat array as number, for example, perform following:
            a = [
                [1, 2],
                [3, 4]
            ]
            a + 2 = [
                [3, 5],
                [5, 6],
            ]
            more advanced, for instance:
            a = [1, 2, 3]
            a.exponential_reduce() -> [1^2, 2^1, 3^0]

            It's easy to archive the sample above with a low depth of 2 or 1.
            however, for doing each, we need to create a new class with all methods
            rewritten. VSA support direct inherit from <Variance> class and allow us
            to only redefine the init method and self-duplicating ones.

        How does it works:
            <Base> stores base level operation to a list
            <Variance> dives into nested list and find the minimum array to perform
                calculation
            <Array> different to list, minimum unit of both <Base> and <Variance>
                is supposed to be an instance of <Array>
            <Matrix> 2-nested lists, depth-2-array

        Advantages
            <Array> and <Matrix>, init, append, concat, are well-defined, which
            handles a variety of different params such as list, Array, numeric, etc.
    """

    # init by list
    def __init__(self, li):
        self.li = li

    def forget(self):
        self.li = []

    """ make a copy of Array """

    def __reversed__(self):
        new_array = self.concat()
        new_array.reverse()
        return new_array

    def sorted(self):
        new_array = self.concat()
        new_array.sort()
        return new_array

    """ operations: self-changing and return void """

    def sort(self):
        self.li = list(sorted(self.li))

    def reverse(self):
        self.li = list(reversed(self.li))

    def __iadd__(self, other):
        if isinstance(other, Array):
            self.li += other.li
        elif isinstance(other, int) or isinstance(other, float):
            self.li = [xx + other for xx in self.li]
        return self

    def __isub__(self, other):
        if isinstance(other, Array):
            self.li -= other.li
        elif isinstance(other, int) or isinstance(other, float):
            self.li = [xx - other for xx in self.li]
        return self

    def __imul__(self, other):
        if isinstance(other, Array):
            self.li *= other.li
        elif isinstance(other, int) or isinstance(other, float):
            self.li = [xx * other for xx in self.li]
        return self

    def __itruediv__(self, other):
        if isinstance(other, Array):
            self.li /= other.li
        elif isinstance(other, int) or isinstance(other, float):
            self.li = [xx / other for xx in self.li]
        return self

    def __ifloordiv__(self, other):
        if isinstance(other, Array):
            self.li //= other.li
        elif isinstance(other, int) or isinstance(other, float):
            self.li = [xx // other for xx in self.li]
        return self

    def __imod__(self, other):
        if isinstance(other, Array):
            self.li %= other.li
        elif isinstance(other, int) or isinstance(other, float):
            self.li = [xx % other for xx in self.li]
        return self

    def __ipow__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('<Array> can only be powered by number')
        self.li = [xx ** other for xx in self.li]
        return self

    """ operation on object: self-changing and return self """

    def __neg__(self):
        self.li = [-abs(xx) for xx in self.li]
        return self

    def __pos__(self):
        self.li = [abs(xx) for xx in self.li]
        return self

    def __add__(self, other):
        return self.__iadd__(other)

    def __sub__(self, other):
        return self.__isub__(other)

    def __mul__(self, other):
        return self.__imul__(other)

    def __truediv__(self, other):
        return self.__itruediv__(other)

    def __floordiv__(self, other):
        return self.__ifloordiv__(other)

    def __mod__(self, other):
        return self.__imod__(other)

    def __pow__(self, power, modulo=None):
        return self.__ipow__(power)

    """ length comparison """

    def __bool__(self):
        return len(self.li) == 0

    def __lt__(self, other):
        if isinstance(other, Array):
            return len(self.li) < len(other.li)
        elif isinstance(other, int) or isinstance(other, float):
            return len(self.li) < other

    def __le__(self, other):
        if isinstance(other, Array):
            return len(self.li) <= len(other.li)
        elif isinstance(other, int) or isinstance(other, float):
            return len(self.li) <= other

    def __eq__(self, other):
        if isinstance(other, Array):
            return len(self.li) == len(other.li)
        elif isinstance(other, int) or isinstance(other, float):
            return len(self.li) == other

    def __ne__(self, other):
        if isinstance(other, Array):
            return len(self.li) != len(other.li)
        elif isinstance(other, int) or isinstance(other, float):
            return len(self.li) != other

    def __ge__(self, other):
        if isinstance(other, Array):
            return len(self.li) > len(other.li)
        elif isinstance(other, int) or isinstance(other, float):
            return len(self.li) > other

    def __gt__(self, other):
        if isinstance(other, Array):
            return len(self.li) >= len(other.li)
        elif isinstance(other, int) or isinstance(other, float):
            return len(self.li) >= other

    """ properties and attributes """

    def __len__(self):
        return len(self.li)

    def __str__(self):
        return str(self.li)

    def __repr__(self):
        return str(self.li)

    def __index__(self, arg):
        return self.li.index(arg)

    def __contains__(self, item):
        return item in self.li

    # remove the value at index
    def __delitem__(self, key):
        del self.li[0]

    def __setitem__(self, key, value):
        self.li[key] = value

    def __getitem__(self, item):
        return self.li[item]

    def __iter__(self):
        for ii in self.li:
            yield ii

    def enumerate(self):
        for ii, dd in enumerate(self.li):
            yield ii, dd

    def append(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.li.append(other)
        elif isinstance(other, list):
            self.li += other
        elif isinstance(other, Array):
            self.li += other.li

    def remove(self, other):
        self.li.remove(other)

    def concat(self, *args):
        new_array = Array(self.li)
        for arg in args:
            new_array.append(arg)
        return new_array

    def pop(self, *args):
        if args:
            return self.li.pop(args[0])
        else:
            return self.li.pop()

    # get rid of first one
    def shift(self):
        return self.pop(0)

    def insert(self, __key, __value):
        if (not isinstance(__key, int)) or (not (isinstance(__value, int) or isinstance(__value, float))):
            if isinstance(__value, list) or isinstance(__value, Array):
                for ii in reversed(__value):
                    self.li.insert(__key, ii)
            else:
                raise TypeError('<Array> insert only accepts int key and numeric value')
        else:
            self.li.insert(__key, __value)

    # insert at 0
    def unshift(self, arg):
        self.insert(0, arg)

    # [2, 3, 4] -> [8, 9, 4]
    def index_exponential(self):
        for ii in range(self.__len__()):
            self[ii] **= self.__len__() - ii
        return self

    # [1, 2] - [3, 4] = [-2, -2]
    def subtract(self, other):
        for ii in range(self.__len__()):
            self[ii] -= other[ii]
        return self

    def to_list(self):
        return self.concat().li


class Variance(Base):
    def __init__(self, li):
        super().__init__(li)

    def forget(self):
        super().forget()

    # execute `for` for n times
    @staticmethod
    def loop(arr):
        if type(arr[0]) is Array:
            for aa in arr:
                yield from Variance.loop(aa)
        else:
            yield arr

    """ concat: make a copy of Array """

    def __reversed__(self):
        return super().__reversed__()

    def sorted(self):
        return super().sorted()

    """ operations: self-changing and return void """

    def sort(self):
        for bas in Variance.loop(arr=self.li):
            bas.sort()

    def reverse(self):
        for bas in Variance.loop(arr=self.li):
            bas.reverse()

    def __iadd__(self, other):
        for bas in Variance.loop(arr=self.li):
            bas.__iadd__(other)
        return self

    def __isub__(self, other):
        for bas in Variance.loop(arr=self.li):
            bas.__isub__(other)
        return self

    def __imul__(self, other):
        for bas in Variance.loop(arr=self.li):
            bas.__imul__(other)
        return self

    def __itruediv__(self, other):
        for bas in Variance.loop(arr=self.li):
            bas.__itruediv__(other)
        return self

    def __ifloordiv__(self, other):
        for bas in Variance.loop(arr=self.li):
            bas.__ifloordiv__(other)
        return self

    def __imod__(self, other):
        for bas in Variance.loop(arr=self.li):
            bas.__imod__(other)
        return self

    def __ipow__(self, other):
        for bas in Variance.loop(arr=self.li):
            bas.__ipow__(other)
        return self

    """ operation on object: self-changing and return self """

    def __neg__(self):
        for bas in Variance.loop(arr=self.li):
            bas.__neg__()
        return self

    def __pos__(self):
        for bas in Variance.loop(arr=self.li):
            bas.__pos__()
        return self

    def __add__(self, other):
        return self.__iadd__(other)

    def __sub__(self, other):
        return self.__isub__(other)

    def __mul__(self, other):
        return self.__imul__(other)

    def __truediv__(self, other):
        return self.__imul__(other)

    def __floordiv__(self, other):
        return self.__imul__(other)

    def __mod__(self, other):
        return self.__imul__(other)

    def __pow__(self, power, modulo=None):
        return self.__pow__(power)

    """ length comparison """

    def __bool__(self):
        return super().__bool__()

    def __lt__(self, other):
        return super().__lt__(other)

    def __le__(self, other):
        return super().__le__(other)

    def __eq__(self, other):
        return super().__eq__(other)

    def __ne__(self, other):
        return super().__ne__(other)

    def __ge__(self, other):
        return super().__ge__(other)

    def __gt__(self, other):
        return super().__gt__(other)

    """ properties and attributes """

    def __len__(self):
        return super().__len__()

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    def __index__(self, arg):
        return super().__index__(arg)

    def __contains__(self, item):
        return super().__contains__(item)

    # remove the value at index
    def __delitem__(self, key):
        super().__delitem__(key)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __iter__(self):
        for ii in super().__iter__():
            yield ii

    def enumerate(self):
        for ii, dd in super().enumerate():
            yield ii, dd

    def append(self, other):
        super().append(other)

    def remove(self, other):
        super().remove(other)

    def concat(self, *args):
        return super().concat(*args)

    def pop(self, *args):
        return super().pop(*args)

    # get rid of first one
    def shift(self):
        return super().shift()

    def insert(self, __key, __value):
        super().insert(__key, __value)

    # insert at 0
    def unshift(self, arg):
        super().unshift(arg)

    def exponential_by_index(self, va):
        for bas in Variance.loop(arr=self.li):
            va.append(bas.concat().index_exponential())
        return va

    # [[1, 2], [3, 4], [5, 6]] -> [[-2, -2], [-2, -2]]
    def reduce_row_by_subtract(self, va):
        con = 0
        pt = 0
        for bas in Variance.loop(arr=self.li):
            if con == 0:
                pt = bas.concat()
            else:
                va.append(pt.subtract(bas))
                pt = bas.concat()
            con += 1
        return va

    def to__list(self, va):
        for bas in Variance.loop(arr=self.li):
            va.append(bas.to_list())
        return va


# depth 1 Variance
class Array(Base):
    """
        treat a list as a number
        nested list impossible
    """

    # [1, [2, [3]]] -> [1, 2, 3]
    @staticmethod
    def flatten(array):
        if isinstance(array, Array):
            return array.concat()
        elif isinstance(array, int) or isinstance(array, float):
            return [array]
        elif isinstance(array, list):
            new_array = list()
            for arr in array:
                try:
                    new_array += Array.flatten(arr)
                except TypeError:
                    new_array += (arr,)
            return new_array
        else:
            raise TypeError('<Array> flatten only takes number or list as parameter')

    # list, Array or number
    def __init__(self, *args):
        li = []
        for arg in args:
            if isinstance(arg, list):
                li += Array.flatten(arg)
            elif isinstance(arg, Array):
                li += arg.concat()
            elif isinstance(arg, int) or isinstance(arg, float):
                li.append(arg)
            else:
                raise ValueError('<Array> init only accept list, Array or number')
        super().__init__(li)


# depth 2 Variance
class Matrix(Variance):
    """ perform common features of matrix such as operation and list methods with an inclusive init """

    # create copies in order to maintain original value
    @staticmethod
    def duplicate_matrix(mat):
        return [[oo for oo in pp] for pp in mat]

    @staticmethod
    def duplicate_list(li):
        return [oo for oo in li]

    @staticmethod
    def all_numeric(array_item):
        for aa in array_item:
            if not (isinstance(aa, int) or isinstance(aa, float)):
                return False
        return True

    # can be inited by list, [list, list..], Matrix, [Array, Array..], numeric
    def __init__(self, *args):
        matrix = []
        for arg in args:
            # Array
            if isinstance(arg, Array):
                matrix.append(arg.concat())
            elif isinstance(arg, list):
                # list
                if Matrix.all_numeric(arg):
                    matrix.append(Array(arg))
                else:
                    # list matrix or Array matrix
                    # any potential error handled by Array
                    for li in arg:
                        matrix.append(Array(li))
            # numeric
            elif isinstance(arg, int) or isinstance(arg, float):
                matrix.append(Array(arg))
            # matrix
            if isinstance(arg, Matrix):
                matrix = arg.li
        super().__init__(matrix)

    def __str__(self):
        ss = ''
        for ii in self.li:
            ss += '\t' + f'{str(len(ii))} -> ' + str(ii) + ',\n'
        return f'[\n{ss}]'

    def concat(self, *args):
        ma = Matrix()
        ma.li = [[xx for xx in yy] for yy in self.li]
        for arg in args:
            ma.append(arg)
        return ma

    def append(self, other):
        if isinstance(other, Matrix):
            for array in other:
                self.li.append(array.concat())
        elif isinstance(other, Array):
            self.li.append(other.concat())
        elif isinstance(other, int) or isinstance(other, float):
            self.li.append(Array(other))
        elif isinstance(other, list):
            if Matrix.all_numeric(other):
                self.li.append(Array(other))
            else:
                for aol in other:
                    if isinstance(aol, Array):
                        self.li.append(aol.concat())
                    elif isinstance(aol, list) and Matrix.all_numeric(aol):
                        self.li.append(Array(aol))
                    else:
                        raise TypeError('<Matrix> append only accept Matrix, Array or 1 level nested list')

    def reduce_row_by_subtract(self, va=None):
        return super().reduce_row_by_subtract(Matrix())

    def exponential_by_index(self, va=None):
        return super().exponential_by_index(Matrix())

    def tolist(self):
        ma = list()
        return super().to__list(ma)

    # supported by numpy.linalg.inv
    def inverse(self):
        array = np.array(self.tolist())
        new_li = np.linalg.inv(array)
        ma = Matrix(new_li.tolist())
        return ma


if __name__ == '__main__':
    m = Matrix(
        [1, 2, 3],
        400,
        Array(12, 13, 14)
    )

    print(m)
    # [
    # 	3 -> [1, 2, 3],
    # 	1 -> [400],
    # 	3 -> [12, 13, 14],
    # ]

    m *= 9
    print(m)
    # [
    # 	3 -> [9, 18, 27],
    # 	1 -> [3600],
    # 	3 -> [108, 117, 126],
    # ]

    m[1] = -m[1]
    print(m)
    # [
    # 	3 -> [9, 18, 27],
    # 	1 -> [-3600],
    # 	3 -> [108, 117, 126],
    # ]
