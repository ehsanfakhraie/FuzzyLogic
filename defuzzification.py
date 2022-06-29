from scipy.integrate import quad


# return m and c in a linear equation with two points input
def linear_equation(point1, point2):
    m = (point2[1] - point1[1]) / (point2[0] - point1[0])
    c = point1[1] - m * point1[0]
    return m, c


# calculate integrated value of a function
def calc_integrate(m, c, a, b):
    def f(x):
        return m * x + c

    return quad(f, a, b)[0], quad(f, a, b)[1]


def health_defuzzification(input):
    m, c = linear_equation((0.25, 1), (1, 0))
    if input == 1:
        num1, denom1 = calc_integrate(0, 1, 0, 0.25)
        num2, denom2 = calc_integrate(m, c, 0.25, 1)
        return num1 + num2, denom1 + denom2
    else:
        x = (input - c) / m
        num1, denom1 = calc_integrate(0, input, 0, x)
        num2, denom2 = calc_integrate(m, c, x, 1)
        return num1 + num2, denom1 + denom2


def sick1_deffuzification(input):
    m1, c1 = linear_equation((0, 0), (1, 1))
    m2, c2 = linear_equation((1, 1), (2, 0))

    if input == 1:
        num1, denom1 = calc_integrate(m1, c1, 0, 1)
        num2, denom2 = calc_integrate(m2, c2, 1, 2)
        return num1 + num2, denom1 + denom2
    else:
        # y = mx + c; x = (y - c) / m
        x1 = (input - c1) / m1
        x2 = (input - c2) / m2
        num1, denom1 = calc_integrate(m1, c1, 0, x1)
        num2, denom2 = calc_integrate(0, input, x1, x2)
        num3, denom3 = calc_integrate(m2, c2, x2, 2)
        return num1 + num2 + num3, denom1 + denom2 + denom3


def sick2_deffuzification(input):
    m1, c1 = linear_equation((1, 0), (2, 1))
    m2, c2 = linear_equation((2, 1), (3, 0))

    if input == 1:
        num1, denom1 = calc_integrate(m1, c1, 1, 2)
        num2, denom2 = calc_integrate(m2, c2, 2, 3)
        return num1 + num2, denom1 + denom2
    else:
        # y = mx + c; x = (y - c) / m
        x1 = (input - c1) / m1
        x2 = (input - c2) / m2
        num1, denom1 = calc_integrate(m1, c1, 1, x1)
        num2, denom2 = calc_integrate(0, input, x1, x2)
        num3, denom3 = calc_integrate(m2, c2, x2, 3)
        return num1 + num2 + num3, denom1 + denom2 + denom3


def sick3_deffuzification(input):
    m1, c1 = linear_equation((2, 0), (3, 1))
    m2, c2 = linear_equation((3, 1), (4, 0))

    if input == 1:
        num1, denom1 = calc_integrate(m1, c1, 2, 3)
        num2, denom2 = calc_integrate(m2, c2, 3, 4)
        return num1 + num2, denom1 + denom2
    else:
        # y = mx + c; x = (y - c) / m
        x1 = (input - c1) / m1
        x2 = (input - c2) / m2
        num1, denom1 = calc_integrate(m1, c1, 2, x1)
        num2, denom2 = calc_integrate(0, input, x1, x2)
        num3, denom3 = calc_integrate(m2, c2, x2, 4)
        return num1 + num2 + num3, denom1 + denom2 + denom3


def sick4_deffuzification(input):
    m, c = linear_equation((3, 0), (3.75, 1))
    if input == 1:
        num1, denom1 = calc_integrate(0, 1, 3, 3.75)
        num2, denom2 = calc_integrate(m, c, 3.75, 4)
        return num1 + num2, denom1 + denom2
    else:
        # y = mx + c; x = (y - c) / m
        x = (input - c) / m
        num1, denom1 = calc_integrate(m, c, 3, x)
        num2, denom2 = calc_integrate(0, input, x, 4)
        return num1 + num2, denom1 + denom2


def defuzzification(output_dict):
    result = ''
    num, denom = 0, 0
    def_value = 0
    i = 0
    if output_dict['healthy'] > 0:
        result += 'healthy'
        res = health_defuzzification(output_dict['healthy'])
        num += res[0]
        denom += res[1]
        i += 1
    if output_dict['sick_1'] > 0:
        if i > 0:
            result += ' & '
        result += 'sick1'
        res = sick1_deffuzification(output_dict['sick_1'])
        num += res[0]
        denom += res[1]
        i += 1
    if output_dict['sick_2'] > 0:
        if i > 0:
            result += ' & '
        result += 'sick2'
        res = sick2_deffuzification(output_dict['sick_2'])
        num += res[0]
        denom += res[1]
        i += 1
    if output_dict['sick_3'] > 0:
        if i > 0:
            result += ' & '
        result += 'sick3'
        res = sick3_deffuzification(output_dict['sick_3'])
        num += res[0]
        denom += res[1]
        i += 1
    if output_dict['sick_4'] > 0:
        if i > 0:
            result += ' & '
        result += 'sick4'
        res = sick4_deffuzification(output_dict['sick_4'])
        num += res[0]
        denom += res[1]
        i += 1
    def_value = num / denom
    result += ': ' + str(def_value)
    return result
