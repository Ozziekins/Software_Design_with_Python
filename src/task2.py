import time
import io
from contextlib import redirect_stdout
import inspect


def decorator2(func):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        start_time = time.time()

        # capture the output from stdout
        f = io.StringIO()
        with redirect_stdout(f):
            func(*args, **kwargs)
        returned_value = f.getvalue()

        # increase the count of function call
        counter += 1

        end_time = time.time()

        # calculate execution time by subtracting start time from end time
        exec_time = end_time - start_time

        # print requirement according to example
        print(func.__name__ + " call " + str(counter) + " executed in " + str(exec_time) + " sec")

        # additional functionality to dump original source code of the function in the given format
        print("Name: \t" + func.__name__ + "\n" +
              "Type: \t" + str(type(func)) + "\n" +
              "Sign: \t" + str(inspect.signature(func)) + "\n" +
              "Args: \tpositional " + str(args) + "\n \t\tkey=worded " + str(kwargs) + "\n" +
              "Doc: \t" + inspect.getdoc(func) + "\n" +
              "Source: \t" + inspect.getsource(func) +
              "Output: \t" + str(returned_value) + "\n")

    return wrapper
