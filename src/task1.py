import time
import io
from contextlib import redirect_stdout


def decorator1(func):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        start_time = time.time()

        # capture the output from stdout
        f = io.StringIO()
        with redirect_stdout(f):
            func(*args, **kwargs)

        # increase the count of function call
        counter += 1

        end_time = time.time()

        # calculate execution time by subtracting start time from end time
        exec_time = end_time - start_time

        # print requirement according to example
        print(func.__name__ + " call " + str(counter) + " executed in " + str(exec_time) + " sec")

    return wrapper
