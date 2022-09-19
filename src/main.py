import math
from task1 import decorator1
from task2 import decorator2
from task3 import ClassFuncDecorator, rankings
from task4 import ClassFuncDecorator2


@decorator1
def even_odd():
    """Function that created a list and categorizes the elements as even or odd"""
    lst = [lambda n=x: n * 7 for x in range(1, 11)]

    for item in lst:
        if item() % 2 == 0:
            print("{} is even".format(item()))
        else:
            print("{} is odd".format(item()))


@decorator1
def solve_quadratic(a, b, c):
    """Function that solves a quadratic equation given a, b and c"""
    D = b*b-4*a*c
    if D < 0:
        print(None)
    elif D == 0:
        print(-b / (2 * a))
    else:
        d_sqrt = math.sqrt(D)
        print((-b + d_sqrt) / (2 * a), (-b - d_sqrt) / (2 * a))


@decorator1
def pascal(n):
    """Function that prints the pascal triangle pattern given n as number of rows"""
    rows = []
    for i in range(1, n+1):
        if i == 1:
            rows.append([1])
        else:
            rows.append([1] +  # one in the beginning
                        [rows[-1][j]+rows[-1][j+1] for j in range(len(rows[-1])-1)] +  # summing the pairs in the middle
                        [1])   # one in the end
        print(*rows[-1])


if __name__ == "__main__":
    even_odd()

    solve_quadratic(1, 2, c=-15)
    pascal(8)

    solve_quadratic(1, -8, 12)
    pascal(5)

    pascal(3)
    rankings()
