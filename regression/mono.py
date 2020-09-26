"""
mono.py
copyright 2020 @Messiz Qin https://github.com/Weilory

* manipulate data by monotonicity

<Poly>
    support changing additional lists based on how initial list is changed

<Mono>
    extract the largest sample of data based on passed in operator, for example, mono-increasing when operator is <
"""


class Poly:
    # get new to_change based on how original changed
    @staticmethod
    def mirror(original, changed, to_change):
        res = []
        for ii in changed:
            res.append(to_change[original.index(ii)])
        return res

    def __init__(self, array, along):
        self.array = [xx for xx in array]
        if along is None:
            self.along = None
        elif isinstance(along[0], list):
            self.along = [[oo for oo in qq] for qq in along]
        else:
            self.along = [qq for qq in along]

    # changed array
    def publish(self, ca):
        res = {'array': ca}
        if self.along is None:
            pass
        elif isinstance(self.along[0], list):
            res['along'] = []
            for al in self.along:
                res['along'].append(Poly.mirror(self.array, ca, al))
        else:
            res['along'] = Poly.mirror(self.array, ca, self.along)
        return res


class Mono(Poly):
    """
    Monotonicity Branch Algorithm
        Aim
            select the longest branch from data within certain mono feature

        Take mono-increase as an example
            for a list of data, iterate it, separate at current. for the
            first half, check if any of the previous has any that is less than
            the current item, if condition satisfied, which indicates previous
            branches can be appended, there's no need to restart a new branch.
            if condition fails, then check if any of the next half is
            greater than current value, if so, then we need to prepare
            a new branch for future, therefore append the item within a
            new list to branches.
    """

    # determine the major trend of an array
    @staticmethod
    def is_increasing(arr):
        inc = 0
        for ii in range(len(arr) - 1):
            if arr[ii] < arr[ii + 1]:
                inc += 1
        rat = inc / (len(arr) - 1)
        return rat > 0.5

    # get the longest array out of a list of arrays
    @staticmethod
    def longest(arr):
        lengths = []
        for ar in arr:
            lengths.append(len(ar))

        return arr[lengths.index(max(lengths))]

    # only return true of any of the array is less than arg
    @staticmethod
    def compare(array, arg, func):
        for ar in array:
            if func(ar, arg):
                return True
        return False

    """
        following are not magic methods
        since they are used as callbacks associated by operator param in Mono initializer 
    """

    # greater than
    @staticmethod
    def gt(arg1, arg2):
        return arg1 > arg2

    # greater than or equal to
    @staticmethod
    def ge(arg1, arg2):
        return arg1 >= arg2

    # less than
    @staticmethod
    def lt(arg1, arg2):
        return arg1 < arg2

    # less than or equal to
    @staticmethod
    def le(arg1, arg2):
        return arg1 <= arg2

    # return mono increasing
    @staticmethod
    def branch(arr, fir, sec):
        branches = []

        for ii, dd in enumerate(arr):
            if Mono.compare(arr[:ii], dd, fir):
                for bran in branches:
                    # if the branch last item is less than current, then append
                    if fir(bran[-1], dd):
                        bran.append(dd)
                    # elif the branch contains gt and lt, then insert and recreate
                    else:
                        for pp in range(len(bran)):
                            # count from last to first
                            oo = len(bran) - 1 - pp
                            # once target is find, kill the loop
                            if fir(bran[oo], dd):
                                bra = bran[:oo]
                                bra.append(dd)
                                branches.append(bra)
                                break
            elif Mono.compare(arr[ii:], dd, sec):
                # add branch
                branches.append([dd])

        return Mono.longest(branches)

    @staticmethod
    def operation(sign):
        if sign == '<':
            return [Mono.lt, Mono.gt]
        elif sign == '>':
            return [Mono.gt, Mono.lt]
        elif sign == '<=':
            return [Mono.le, Mono.ge]
        elif sign == '>=':
            return [Mono.ge, Mono.le]
        else:
            raise ValueError(f'Mono: invalid operate: {sign}\nAvailable: < > <= >=')

    def __init__(self, array, operate, along=None):
        super().__init__(array, along)
        self.opt = Mono.operation(operate.strip())

    def __setitem__(self, key, value):
        if key == 'operate':
            self.opt = Mono.operation(value.strip())

    @property
    def mono(self):
        ca = Mono.branch(self.array, *self.opt)
        return super().publish(ca)


if __name__ == '__main__':
    cols = [-100, -1000, 0, 1, 1, 2, -100, 3, -200, -200, -300, -1000, -12000]
    brr = [x for x in range(len(cols))]

    # Mono init:
    #   takes an array and an operate as essential params
    #   along is a list of array of the same length compare to array
    #   along will be changed if change occurs to array
    m = Mono(array=cols, operate='<', along=[brr for x in range(2)])
    print(m.mono)
    # {'array': [-100, 0, 1, 2, 3], 'along': [[0, 2, 3, 5, 7], [0, 2, 3, 5, 7]]}

    m['operate'] = '>'
    print(m.mono)
    # {'array': [0, -100, -200, -300, -1000, -12000], 'along': [[2, 0, 8, 10, 1, 12], [2, 0, 8, 10, 1, 12]]}

    m['operate'] = '>='
    print(m.mono)
    # {
    #   'array': [1, 1, -100, -200, -200, -300, -1000, -12000],
    #   'along': [[3, 3, 0, 8, 8, 10, 1, 12], [3, 3, 0, 8, 8, 10, 1, 12]]
    # }

