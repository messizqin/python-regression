class Write:

    """ default to 3 decimal places """
    DEFAULT = 3

    @staticmethod
    def rit(num):
        return round(num, Write.DEFAULT)

    @staticmethod
    def linear(coe):
        # [k, b]
        return f'y = {Write.rit(coe[0])} * x + {Write.rit(coe[1])}'

    @staticmethod
    def exponential_plus(coe):
        ss = ''
        for ii in range(len(coe) - 1):
            ss += ' + ' + str(Write.rit(coe[ii])) + ' * x' + '**' + str(len(coe) - ii - 1)
        return ss[3:] + ' + ' + str(Write.rit(coe[-1]))

    @staticmethod
    def exponential_parabola(coe):
        # [a, b, c..]
        return 'y = ' + Write.exponential_plus(coe)

    @staticmethod
    def inverse_exponential_parabola(coe):
        # [a, b, c ... pro, y_exp]
        return 'y ** ' + str(Write.rit(coe[-1])) + ' = ' + str(Write.rit(coe[-2])) + ' / (' + Write.exponential_plus(coe[:-2]) + ')'


if __name__ == '__main__':
    pass

    # print(Write.linear([2, 3]))
    # # y = 2 * x + 3
    #
    # print(Write.exponential_parabola([4, 3, 2, 1]))
    # # y = 4 * x**3 + 3 * x**2 + 2 * x**1 + 1

    print(Write.inverse_exponential_parabola([3, 1, 2, 4, 10]))
    # y ** 10 = 4 / (3 * x ** 2 + 1 * x ** 1 + 2)


